#cython: language_level=3, annotation_typing=True, embedsignature=True, boundscheck=False, wraparound=False, cdivision=True
#distutils: language = c++
cimport cython
from libcpp.vector cimport vector
from libc.stdio cimport printf, snprintf, sscanf
from libc.stdlib cimport malloc, free
from libc.string cimport strcpy, memset, strncmp, strlen
from sat_toolkit.types cimport *

cdef extern from "fmt.h":
    ctypedef struct fmt_buf:
        size_t len, capacity
        char *buf

    fmt_buf make_buf()
    void free_buf(fmt_buf *buf)
    int buf_printf(fmt_buf *buf, const char *fmt, ...)


cdef extern from *:
    """
    #define ffs(x) __builtin_ffsll(x)
    #define popcount(x) __builtin_popcountll(x)
    """
    int ffs(int x) nogil
    int popcount(unsigned int x) nogil
    int likely(int) nogil
    int unlikely(int) nogil


import io, sys
import numpy as np
import subprocess as sp
from tempfile import NamedTemporaryFile
from typing import *

from dataclasses import dataclass

cdef int startswith(const unsigned char[:] buf, const char *start) nogil:
    cdef ssize_t l = strlen(start)
    if buf.shape[0] < l:
        return 0
    return strncmp(<const char *> &buf[0], <const char *> &start[0], l) == 0


cdef class Clause:
    cdef vector[int] clause
    def __init__(self, clause):
        cdef int c
        for c in clause:
            if c == 0:
                raise ValueError('cannot use 0 as part of clause')
            self.clause.push_back(c)
        self.clause.shrink_to_fit()

    @staticmethod
    cdef Clause from_memview(const int[:] clause):
        cdef size_t i
        cdef Clause res = Clause.__new__(Clause)

        res.clause.resize(clause.shape[0])
        for i in range(res.clause.size()):
            if clause[i] == 0:
                raise ValueError('cannot use 0 as part of clause')
            res.clause[i] = clause[i]

        return res

    def apply_to_variables(self, variables: list, true_op: Callable, false_op: Callable):
        cdef size_t nvars = 0
        cdef size_t i
        cdef int c

        if <size_t> len(variables) < self._maxvar() + 1:
            raise ValueError(f'too few variables supplied (need to include dummy variable for 0)')

        res = [None] * (<ssize_t> self.clause.size())

        for i in range(self.clause.size()):
            c = self.clause[i]
            if c > 0:
                res[i] = true_op(variables[c])
            if c < 0:
                res[i] = false_op(variables[-c])
        return res


    cdef size_t _maxvar(self):
        cdef size_t i
        cdef int c, res = 0
        for i in range(self.clause.size()):
            c = abs(self.clause[i])
            if c > res:
                res = c
        return res

    @property
    def maxvar(self):
        return self._maxvar()

    def __repr__(self):
        return f'Clause({self.clause})'

    def __getitem__(self, ssize_t idx):
        if idx < 0:
            idx += self.clause.size()
        if idx < 0 or <size_t> idx >= self.clause.size():
            raise IndexError('index out of range')
        return self.clause[idx]

    def __len__(self):
        return self.clause.size()

    def __iter__(self):
        cdef size_t i = 0
        for i in range(self.clause.size()):
            yield self.clause[i]


cdef class CNF:
    """
    Class for storing and manipulating CNF formulas.
    The CNF is represented in a format closely related to the DIMACS format.
    Therefore, indices start with 1.
    """
    cdef readonly vector[int] clauses
    cdef readonly vector[size_t] start_indices

    cdef readonly int nvars

    #used for the buffer support
    cdef ssize_t shape[1]
    cdef ssize_t strides[1]
    cdef ssize_t view_count

    def __init__(self, clauses = None, nvars = -1):
        pass

    def __cinit__(self, int[:] clauses = None, int nvars = -1):
        cdef ssize_t i, l = 0
        if clauses is not None:
            l = clauses.shape[0]
        self.shape[0] = l
        self.strides[0] = sizeof(self.clauses[0])
        self.view_count = 0
        self.nvars = 0

        if clauses is not None:
            self._add_clauses(clauses)
        if nvars != -1:
            if nvars < self.nvars:
                raise ValueError(f"explicitly given nvars too small ({nvars} < {self.nvars})")
            self.nvars = nvars




    @staticmethod
    cdef CNF _from_dimacs(const uint8_t[::1] dimacs):
        cdef CNF res = CNF.__new__(CNF)
        cdef const char *buf = <const char *> &dimacs[0]

        cdef size_t off = -1, nclauses
        cdef int nvars, tmp

        while (sscanf(buf, "c %*[^\n]\n%zn", &off) or 1) and off != -1ULL:
            buf += off
            off = -1


        off = -1
        if (sscanf(buf, "p cnf %d %zd\n%zn", &nvars, &nclauses, &off) or 1) and off == -1ULL:
            raise ValueError('file format error')
        buf += off

        cdef size_t remaining_len = dimacs.shape[0] - (buf - <const char *> &dimacs[0])
        values = np.fromstring(buf[:remaining_len], dtype=np.int32, sep=' ')

        res._add_clauses(values)
        assert nvars >= res.nvars
        res.nvars = nvars
        return res

    @staticmethod
    def from_dimacs(dimacs: str) -> CNF:
        return CNF._from_dimacs(dimacs.encode())

    @staticmethod
    def from_espresso(espresso: str) -> CNF:
        cdef vector[int] clauses
        cdef vector[size_t] start_indices
        cdef const unsigned char[:] line
        cdef char val
        cdef uint64_t mask, sign
        cdef unsigned int numbits = 0
        cdef size_t i

        f = io.BytesIO(espresso.encode())

        for line_py in f:
            line = line_py.strip()
            if startswith(line, b'.i '):
                _, bits = line_py.split()
                numbits = int(bits)
            if startswith(line, b'.p '):
                ...
            if startswith(line, b'#') or startswith(line, b'.'):
                continue

            val = line[line.shape[0] - 1]
            if line.shape[0] != numbits + 2 or line[line.shape[0] - 2] != b' ':
                raise ValueError('file format error')

            #espresso_mask, val = line.split()

            if val != b'1':
                raise ValueError(f'got unexpected value for product term: {val!r} expected \'1\'.')

            for i in range(numbits):
                val = line[numbits - 1 - i]
                if val == b'-':
                    continue
                # 0/1 swapped according to De Morgan's law
                if val == b'0':
                    clauses.push_back((i + 1))
                    continue
                if val == b'1':
                    clauses.push_back(-(i + 1))
                    continue
                raise ValueError(f'file format error in line {bytes(line)}')
            clauses.push_back(0)

        cdef CNF res = CNF.__new__(CNF)
        if clauses.size() > 0:
            res._add_clauses(<int[:clauses.size()]> clauses.data())
        assert numbits >= <unsigned int> res.nvars 
        res.nvars = numbits
        return res


    cdef void _add_clauses(self, int[:] clauses):
        cdef size_t l, old_len, i

        if self.view_count > 0:
            raise ValueError('cannot alter while referenced by buffer')

        l = clauses.shape[0]
        if l > 0 and clauses[l - 1] != 0:
            raise ValueError('last clause not terminated with 0')

        old_len = self.clauses.size()
        self.clauses.resize(self.clauses.size() + l)

        if l > 0:
            self.start_indices.push_back(old_len)

        for i in range(l):
            self.clauses[old_len + i] = clauses[i]
            if abs(clauses[i]) > self.nvars:
                self.nvars = abs(clauses[i])

            if clauses[i] == 0 and i + 1 < l:
                self.start_indices.push_back(old_len + i + 1)

    def add_clauses(self, clauses) -> None:
        np_clauses = np.array(clauses, dtype=np.int32)
        self._add_clauses(np_clauses)

    def add_clause(self, clause) -> None:
        "add a single clause to CNF formula"
        cdef ssize_t clause_len = len(clause)
        np_clause = np.zeros(clause_len + 1, dtype=np.int32)
        np_clause[:clause_len - 1] = clause
        if np.count_nonzero(np_clause) != clause_len:
            raise ValueError('cannot use 0 in clause')
        self._add_clauses(np_clause)

    append = add_clause

    def logical_or(self, int var) -> CNF:
        """
        return a new CNF corresponding to (var or self). I.e., the new CNF is
        build by appending var to each clause
        """
        if var == 0:
            raise ValueError("var must not be zero")

        cdef vector[int] new_clauses
        cdef ssize_t src = 0, dst = 0
        new_clauses.resize(self.clauses.size() + self.start_indices.size())

        for src in range(<ssize_t> self.clauses.size()):
            if self.clauses[src] == 0:
                new_clauses[dst] = var
                dst += 1
            new_clauses[dst] = self.clauses[src]
            dst += 1

        cdef CNF res = CNF.__new__(CNF)
        res._add_clauses(<int[:new_clauses.size()]> new_clauses.data())
        return res


    def implied_by(self, int var) -> CNF:
        """
        return a new CNF corresponding to (var -> self). I.e., the new CNF is
        build by appending ~var to each clause
        """
        return self.logical_or(-var)


    def to_dimacs(self):
        cdef size_t max_len = snprintf(NULL, 0, "%d", -self.nvars)
        cdef size_t nclauses = self.start_indices.size()
        cdef ssize_t buf_size = (self.clauses.size() - nclauses) * (max_len + 1) + nclauses * (2)
        cdef char *buf = <char *> malloc(buf_size + 1)
        cdef ssize_t buf_idx = 0, written
        cdef size_t i

        for i in range(self.clauses.size()):
            if self.clauses[i] == 0:
                written = snprintf(&buf[buf_idx], buf_size, "0\n")
                if written < 0:
                    assert 0
                buf_idx += written
                buf_size -= written
            else:
                written = snprintf(&buf[buf_idx], buf_size, "%d ", self.clauses[i])
                if written < 0:
                    assert 0
                buf_idx += written
                buf_size -= written

        assert buf_size >= 0
        py_str = buf[:buf_idx]
        free(buf)

        return 'p cnf ' + str(self.nvars) + ' ' + str(nclauses) + '\n' + py_str.decode()

    def to_espresso(self, print_numvars: bool = True):
        cdef size_t i, j
        cdef int lit
        cdef char target_char
        cdef char *line_buf
        cdef fmt_buf buf = make_buf()

        if print_numvars:
            buf_printf(&buf, ".i %d\n", self.nvars)
            buf_printf(&buf, ".o 1\n", self.nvars)
        buf_printf(&buf, ".p %zd\n", self.start_indices.size())

        line_buf = <char *> malloc(self.nvars + 4)
        strcpy(line_buf + self.nvars, " 1\n");

        for i in range(self.start_indices.size()):
            memset(line_buf, b'-', self.nvars);

            j = 0
            while self.clauses[self.start_indices[i] + j] != 0:
                lit = self.clauses[self.start_indices[i] + j]

                target_char = b'0'
                if lit < 0:
                    target_char = b'1'
                    lit = -lit

                line_buf[self.nvars - lit] = target_char

                j += 1

            buf_printf(&buf, "%s", line_buf)

        buf_printf(&buf, ".e\n")
        py_bytes = buf.buf[:buf.len]

        free_buf(&buf)
        return py_bytes.decode()

    def minimize_espresso(self, espresso_args: List[str] = []) -> CNF:
        """
        Uses espresso to minimize the given CNF.

        :param espresso_args: extra parameters given when calling espresso, defaults to []

        :return: a new CNF object as minimized by espresso
        :rtype: CNF
        """
        cdef int ret_code

        with sp.Popen(['espresso'] + espresso_args, stdin=sp.PIPE, stdout=sp.PIPE, text=True) as espresso:
            espresso.stdin.write(self.to_espresso())
            espresso.stdin.close()

            cnf = CNF.from_espresso(espresso.stdout.read())

            ret_code = espresso.wait()
            if ret_code != 0:
                raise sp.CalledProcessError(ret_code, ' '.join(espresso.args))

            return cnf

    def _minimize_dimacs(self, args: List[str], outfile: str):
        """
        calls args with self.to_dimacs() as stdin, waits for the command to
        finish with exit code 10 or 20 and parses `outfile` as DIAMCS`.

        :return: a new CNF object read from `outfile`
        :rtype: CNF
        """
        cdef int ret_code = 0
        with sp.Popen(args, stdin=sp.PIPE, text=True) as minimizer:
            minimizer.stdin.write(self.to_dimacs())
            minimizer.stdin.close()

            ret_code = minimizer.wait()
            if ret_code not in [10, 20]:
                # for SAT solvers ret_code == 10 corresponds to SATISFIABLE and
                # ret == 20 to UNSATISFIABLE (see for example
                # http://www.satcompetition.org/2004/format-solvers2004.html)
                raise sp.CalledProcessError(ret_code, ' '.join(minimizer.args))

        with open(outfile, 'r') as f:
            return CNF.from_dimacs(f.read())

    def minimize_lingeling(self, optlevel=None, timeout=0, extra_args: List[str] = []) -> CNF:
        """
        Uses Lingeling to minimize the given CNF.

        :param optlevel: optimization level given to Lingeling via -O<optlevel>
        :param timeout: timeout given to Lingeling via -T <timeout>
        :param extra_args: extra parameters given when calling Lingeling, defaults to []

        :return: a new CNF object minimized by Lingeling
        :rtype: CNF
        """
        cdef int ret_code = 0

        args = ['lingeling', '-s']
        if optlevel is not None:
            args += [f'-O{optlevel}']
        if timeout is not None:
            args += ['-T', f'{timeout}']

        with NamedTemporaryFile(prefix='lingeling_', suffix='.dimacs') as f:
            args += ['-o', f.name]
            args += extra_args
            return self._minimize_dimacs(args, f.name)


    cdef Clause get_clause(self, ssize_t idx):
        cdef size_t begin, end, i
        cdef size_t numclauses = self.start_indices.size()
        cdef Clause result

        if idx < 0:
            idx += numclauses
        if idx < 0 or <size_t> idx >= numclauses:
            raise IndexError('index out of range')

        begin = self.start_indices[idx]
        end = self.start_indices[idx + 1] if <size_t> idx + 1 < numclauses else self.clauses.size()
        result = Clause.from_memview((<int[:self.clauses.size()]> self.clauses.data())[begin:end - 1])

        return result

    def __getitem__(self, ssize_t idx):
        return self.get_clause(idx)

    def __len__(self):
        return self.start_indices.size()

    def __iter__(self):
        cdef size_t i = 0
        while i < self.start_indices.size():
            yield self.get_clause(i)
            i += 1

    def __eq__(self, other):
        if not isinstance(other, CNF):
            return False

        cdef CNF c_other = <CNF> other

        if self.nvars != c_other.nvars:
            return False
        if self.start_indices != c_other.start_indices:
            return False
        if self.clauses != c_other.clauses:
            return False
        return True

    def __repr__(self):
        return f'CNF over {self.nvars} variables with {self.start_indices.size()} clauses'

    def __str__(self):
        return self.to_dimacs()

    # pickle support
    def __reduce__(self):
        return CNF, (np.array(self), self.nvars)

    def equiv(self, CNF other):
        """
        Check for logical eqivalence between self and other.
        Calls `espresso -Dverify` to perform the comparison.
        """
        if self.nvars != other.nvars:
            return False

        with sp.Popen(['espresso', '-Dverify'], stdin=sp.PIPE, stdout=sp.PIPE, text=True) as espresso:
            espresso.stdin.write(self.to_espresso())
            espresso.stdin.write(other.to_espresso(print_numvars = False))
            espresso.stdin.close()

            ret_code = espresso.wait()
            if ret_code not in [0, 1]:
                raise sp.CalledProcessError(ret_code, ' '.join(espresso.args))

            return ret_code == 0

    def translate(self, new_vars):
        cdef np_vars = np.array(new_vars, np.int32)
        cdef int [::1] var_view = np_vars
        cdef size_t i

        if var_view.shape[0] != self.nvars + 1:
            raise ValueError('need to provide translation for all 1+{self.nvars} variables')
        if var_view[0] != 0:
            raise ValueError('variable 0 must be mapped to 0')
        for i in range(1, <size_t> var_view.shape[0]):
            if var_view[i] == 0:
                raise ValueError('variable must not be mapped to 0')

        cdef vector[int] new_clauses
        new_clauses.resize(self.clauses.size())

        cdef int var
        for i in range(self.clauses.size()):
            var = self.clauses[i]
            new_clauses[i] = var_view[abs(var)] * (1 if var > 0 else -1)

        cdef CNF res = CNF.__new__(CNF)
        res._add_clauses(<int[:new_clauses.size()]> new_clauses.data())
        return res

    # buffer support
    def __getbuffer__(self, cython.Py_buffer *buffer, int flags):
        self.shape[0] = self.clauses.size()

        buffer.buf = <char *>&(self.clauses[0])
        buffer.format = 'i'                     # int
        buffer.internal = NULL                  # see References
        buffer.itemsize = self.strides[0]
        buffer.len = self.shape[0] * self.strides[0]
        buffer.ndim = 1
        buffer.obj = self
        buffer.readonly = 1
        buffer.shape = &self.shape[0]
        buffer.strides = &self.strides[0]
        buffer.suboffsets = NULL                # for pointer arrays only
        self.view_count += 1

    def __releasebuffer__(self, Py_buffer *buffer):
        self.view_count -= 1

cdef class Truthtable:
    """
    A boolean function represented as a truth table.
    The truth table is stored using a table for the ON set and the DC set of the function.
    The ON set denotes where the value of the function is 1/true, while the DC set
    denotes where the value of the function is left unspecified.
    The DC set allows more efficient CNF representations when optimizing with espresso.
    The OFF set is the complement of the two sets.
    """
    cdef public on_set
    cdef public dc_set
    cdef public uint64_t numbits

    INIT_INDEX_SET = object()

    def __init__(self, init_key, numbits, on_set, dc_set):
        if init_key is not self.INIT_INDEX_SET:
            raise ValueError('use .from_lut or .from_indices')

        if len(on_set.shape) != 1 or (dc_set is not None and len(dc_set.shape) != 1):
            raise ValueError('parameters must be one dimensional')

        self.numbits = numbits
        self.on_set = np.sort(on_set)
        self.dc_set = np.sort(dc_set)


    @classmethod
    def from_lut(cls, on_lut: np.ndarray, dc_lut: Optional[np.ndarray] = None):
        """
        Creates a Truthtable from a lookup table (LUT).

        :param on_lut: specifies where the Truthtable should be on, i.e., 1
        :param dc_lut: specifies where the value of the Truthtable can be ignored, this allows for better optimization, defaults to None

        :return: Truthtable with on_set and dc_set initialized according to parameters
        :rtype: Truthtable
        """
        if len(on_lut.shape) != 1 or (dc_lut is not None and len(dc_lut.shape) != 1):
            raise ValueError('parameters must be one dimensional')

        if dc_lut is not None and on_lut.shape != dc_lut.shape:
            raise ValueError('parameters must have the same shape')

        numvals = on_lut.shape[0]
        if (numvals & (numvals - 1)) != 0 or numvals == 0:
            raise ValueError('length parameter must be a power of 2')

        numbits = numvals.bit_length() - 1

        if dc_lut is not None and np.any(on_lut & dc_lut):
            raise ValueError('on_lut and dc_lut must be distinct')

        on_set, = np.where(on_lut)
        dc_set, = np.where(dc_lut) if dc_lut is not None else (np.array([], int),)
        return cls(cls.INIT_INDEX_SET, numbits, on_set, dc_set)

    @classmethod
    def from_indices(cls, numbits: int, on_indices: np.array, dc_indices = np.array([], dtype=int)):
        """
        Creates a Truthtable from the set of indices with value 1 and optionally indices where the value can be ignored.

        :param numbits: number of input bits for the Truthtable
        :param on_indices: set of indices where the Truthtable should be on, i.e., 1
        :param dc_indices: set of indices where the Truthtable value can be ignored, this allows for better optimization, defaults to []

        :return: Truthtable with on_set and dc_set initialized according to parameters
        :rtype: Truthtable
        """
        return cls(cls.INIT_INDEX_SET, numbits, on_indices, dc_indices)


    def _write(self, io: io.TextIOBase, espresso: bool = False, invert: bool = False):
        i_list = range(1 << self.numbits)

        if espresso:
            i_list = np.concatenate((self.on_set, self.dc_set), axis=0)
            i_list.sort()
            io.write(f'.i {self.numbits}\n')
            io.write(f'.o 1\n')
            io.write(f'.p {len(i_list)}\n')

            # this parameter is important so espresso minimizes the inverted function
            io.write(f'.phase {not invert:b}\n')

        def sorted_contains(a, v):
            idx = np.searchsorted(a, v)
            return idx < len(a) and a[idx] == v

        for i in i_list:
            on, dc = sorted_contains(self.on_set, i), sorted_contains(self.dc_set, i)
            desc = '-' if dc else f'{on:b}'
            io.write(f'{i:0{self.numbits}b} {desc}\n')

        # ensure that we write some PLA description
        if len(i_list) == 0:
            io.write('-' * self.numbits + ' 0\n')

        if espresso:
            io.write(f'.end\n')

    def to_espresso(self, phase='cnf'):
        """
        return the truthtable in espresso format

        :param phase: wether to minimize the off_set ('cnf'/0) or on_set ('dnf'/1)

        :return: Truthtable with on_set and dc_set initialized according to parameters
        :rtype: Truthtable
        """
        if phase == 'cnf' or phase == '0' or phase == 0:
            invert = True
        elif phase == 'dnf' or phase == '1' or phase == 1:
            invert = False
        else:
            raise ValueError('invalid value for `phase`')

        res = io.StringIO()
        self._write(res, True, invert)
        return res.getvalue()

    def __repr__(self):
        result = io.StringIO()
        result.write("Truthtable\n")
        self._write(result)
        return result.getvalue()

    def __eq__(self, other):
        if self.numbits != other.numbits:
            return False
        if not np.all(self.on_set == other.on_set):
            return False
        if self.dc_set is None and other.dc_set is not None:
            return False
        if other.dc_set is None and self.dc_set is not None:
            return False
        if not np.all(self.dc_set == other.dc_set):
            return False
        return True

    def to_cnf(self, espresso_args: List[str] = []) -> CNF:
        """
        Uses espresso to convert the Truthtable to a minimized CNF.

        The resulting CNF will be indexed by [1, self.numbits], where index 1
        corresponds to the least significant bit in the truthtable index.

        :param espresso_args: extra parameters given when calling espresso, defaults to []

        :return: CNF minimized by espresso
        :rtype: CNF
        """
        with sp.Popen(['espresso'] + espresso_args, stdin=sp.PIPE, stdout=sp.PIPE, text=True) as espresso:
            self._write(espresso.stdin, True, True)
            espresso.stdin.close()

            cnf = CNF.from_espresso(espresso.stdout.read())

            ret_code = espresso.wait()
            if ret_code != 0:
                raise sp.CalledProcessError(ret_code, ' '.join(espresso.args))

            return cnf
