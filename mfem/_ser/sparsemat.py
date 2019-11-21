# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _sparsemat
else:
    import _sparsemat

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import weakref

import mfem._ser.mem_manager
import mfem._ser.array
import mfem._ser.vector
import mfem._ser.operators
import mfem._ser.matrix
import mfem._ser.densemat

def RAP_P(A, R, ORAP):
    r"""RAP_P(SparseMatrix A, SparseMatrix R, SparseMatrix ORAP) -> SparseMatrix"""
    return _sparsemat.RAP_P(A, R, ORAP)

def RAP_R(Rt, A, P):
    r"""RAP_R(SparseMatrix Rt, SparseMatrix A, SparseMatrix P) -> SparseMatrix"""
    return _sparsemat.RAP_R(Rt, A, P)

def OperatorPtr2SparseMatrix(op):
    r"""OperatorPtr2SparseMatrix(mfem::OperatorPtr op) -> SparseMatrix"""
    return _sparsemat.OperatorPtr2SparseMatrix(op)

def OperatorHandle2SparseMatrix(op):
    r"""OperatorHandle2SparseMatrix(mfem::OperatorHandle op) -> SparseMatrix"""
    return _sparsemat.OperatorHandle2SparseMatrix(op)
class RowNode(object):
    r"""Proxy of C++ mfem::RowNode class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    Value = property(_sparsemat.RowNode_Value_get, _sparsemat.RowNode_Value_set, doc=r"""Value : double""")
    Prev = property(_sparsemat.RowNode_Prev_get, _sparsemat.RowNode_Prev_set, doc=r"""Prev : p.mfem::RowNode""")
    Column = property(_sparsemat.RowNode_Column_get, _sparsemat.RowNode_Column_set, doc=r"""Column : int""")

    def __init__(self):
        r"""__init__(RowNode self) -> RowNode"""
        _sparsemat.RowNode_swiginit(self, _sparsemat.new_RowNode())
    __swig_destroy__ = _sparsemat.delete_RowNode

# Register RowNode in _sparsemat:
_sparsemat.RowNode_swigregister(RowNode)

class SparseMatrix(mfem._ser.matrix.AbstractSparseMatrix):
    r"""Proxy of C++ mfem::SparseMatrix class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(SparseMatrix self) -> SparseMatrix
        __init__(SparseMatrix self, int nrows, int ncols=-1) -> SparseMatrix
        __init__(SparseMatrix self, int * i) -> SparseMatrix
        __init__(SparseMatrix self, int * i, bool ownij, bool owna, bool issorted) -> SparseMatrix
        __init__(SparseMatrix self, int nrows, int ncols, int rowsize) -> SparseMatrix
        __init__(SparseMatrix self, SparseMatrix mat, bool copy_graph=True) -> SparseMatrix
        __init__(SparseMatrix self, Vector v) -> SparseMatrix
        """

        import numpy as np  
        from scipy.sparse import csr_matrix
        if len(args) == 1 and isinstance(args[0], csr_matrix):
           csr = args[0]
           if np.real(csr).dtype != 'float64':
               csr = csr.astype('float64')
           i = np.ascontiguousarray(csr.indptr)
           j = np.ascontiguousarray(csr.indices)
           data = np.ascontiguousarray(csr.data)
           m, n = csr.shape
           this = _sparsemat.new_SparseMatrix([i, j, data, m, n])
           try:
               self.this.append(this)
           except __builtin__.Exception:
               self.this = this
           _sparsemat.SparseMatrix_SetGraphOwner(self, False)
           _sparsemat.SparseMatrix_SetDataOwner(self, False)
           self._i_data = i
           self._j_data = j
           self._d_data = data

           return


        _sparsemat.SparseMatrix_swiginit(self, _sparsemat.new_SparseMatrix(*args))

    def MakeRef(self, master):
        r"""MakeRef(SparseMatrix self, SparseMatrix master)"""
        return _sparsemat.SparseMatrix_MakeRef(self, master)

    def Size(self):
        r"""Size(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_Size(self)

    def Clear(self):
        r"""Clear(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_Clear(self)

    def Empty(self):
        r"""Empty(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_Empty(self)

    def GetI(self, *args):
        r"""
        GetI(SparseMatrix self) -> int
        GetI(SparseMatrix self) -> int const *
        """
        return _sparsemat.SparseMatrix_GetI(self, *args)

    def GetJ(self, *args):
        r"""
        GetJ(SparseMatrix self) -> int
        GetJ(SparseMatrix self) -> int const *
        """
        return _sparsemat.SparseMatrix_GetJ(self, *args)

    def GetData(self, *args):
        r"""
        GetData(SparseMatrix self) -> double
        GetData(SparseMatrix self) -> double const *
        """
        return _sparsemat.SparseMatrix_GetData(self, *args)

    def RowSize(self, i):
        r"""RowSize(SparseMatrix self, int const i) -> int"""
        return _sparsemat.SparseMatrix_RowSize(self, i)

    def MaxRowSize(self):
        r"""MaxRowSize(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_MaxRowSize(self)

    def GetRowColumns(self, *args):
        r"""
        GetRowColumns(SparseMatrix self, int const row) -> int
        GetRowColumns(SparseMatrix self, int const row) -> int const *
        """
        return _sparsemat.SparseMatrix_GetRowColumns(self, *args)

    def GetRowEntries(self, *args):
        r"""
        GetRowEntries(SparseMatrix self, int const row) -> double
        GetRowEntries(SparseMatrix self, int const row) -> double const *
        """
        return _sparsemat.SparseMatrix_GetRowEntries(self, *args)

    def SetWidth(self, width_=-1):
        r"""SetWidth(SparseMatrix self, int width_=-1)"""
        return _sparsemat.SparseMatrix_SetWidth(self, width_)

    def ActualWidth(self):
        r"""ActualWidth(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_ActualWidth(self)

    def SortColumnIndices(self):
        r"""SortColumnIndices(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_SortColumnIndices(self)

    def MoveDiagonalFirst(self):
        r"""MoveDiagonalFirst(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_MoveDiagonalFirst(self)

    def Elem(self, *args):
        r"""
        Elem(SparseMatrix self, int i, int j) -> double
        Elem(SparseMatrix self, int i, int j) -> double const &
        """
        return _sparsemat.SparseMatrix_Elem(self, *args)

    def __call__(self, *args):
        r"""
        __call__(SparseMatrix self, int i, int j) -> double
        __call__(SparseMatrix self, int i, int j) -> double const &
        """
        return _sparsemat.SparseMatrix___call__(self, *args)

    def GetDiag(self, d):
        r"""GetDiag(SparseMatrix self, Vector d)"""
        return _sparsemat.SparseMatrix_GetDiag(self, d)

    def ToDenseMatrix(self, *args):
        r"""
        ToDenseMatrix(SparseMatrix self) -> DenseMatrix
        ToDenseMatrix(SparseMatrix self, DenseMatrix B)
        """
        return _sparsemat.SparseMatrix_ToDenseMatrix(self, *args)

    def GetMemoryClass(self):
        r"""GetMemoryClass(SparseMatrix self) -> mfem::MemoryClass"""
        return _sparsemat.SparseMatrix_GetMemoryClass(self)

    def Mult(self, x, y):
        r"""Mult(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_Mult(self, x, y)

    def AddMult(self, x, y, a=1.0):
        r"""AddMult(SparseMatrix self, Vector x, Vector y, double const a=1.0)"""
        return _sparsemat.SparseMatrix_AddMult(self, x, y, a)

    def MultTranspose(self, x, y):
        r"""MultTranspose(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_MultTranspose(self, x, y)

    def AddMultTranspose(self, x, y, a=1.0):
        r"""AddMultTranspose(SparseMatrix self, Vector x, Vector y, double const a=1.0)"""
        return _sparsemat.SparseMatrix_AddMultTranspose(self, x, y, a)

    def BuildTranspose(self):
        r"""BuildTranspose(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_BuildTranspose(self)

    def ResetTranspose(self):
        r"""ResetTranspose(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_ResetTranspose(self)

    def PartMult(self, rows, x, y):
        r"""PartMult(SparseMatrix self, intArray rows, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_PartMult(self, rows, x, y)

    def PartAddMult(self, rows, x, y, a=1.0):
        r"""PartAddMult(SparseMatrix self, intArray rows, Vector x, Vector y, double const a=1.0)"""
        return _sparsemat.SparseMatrix_PartAddMult(self, rows, x, y, a)

    def BooleanMult(self, x, y):
        r"""BooleanMult(SparseMatrix self, intArray x, intArray y)"""
        return _sparsemat.SparseMatrix_BooleanMult(self, x, y)

    def BooleanMultTranspose(self, x, y):
        r"""BooleanMultTranspose(SparseMatrix self, intArray x, intArray y)"""
        return _sparsemat.SparseMatrix_BooleanMultTranspose(self, x, y)

    def InnerProduct(self, x, y):
        r"""InnerProduct(SparseMatrix self, Vector x, Vector y) -> double"""
        return _sparsemat.SparseMatrix_InnerProduct(self, x, y)

    def GetRowSums(self, x):
        r"""GetRowSums(SparseMatrix self, Vector x)"""
        return _sparsemat.SparseMatrix_GetRowSums(self, x)

    def GetRowNorml1(self, irow):
        r"""GetRowNorml1(SparseMatrix self, int irow) -> double"""
        return _sparsemat.SparseMatrix_GetRowNorml1(self, irow)

    def Inverse(self):
        r"""Inverse(SparseMatrix self) -> MatrixInverse"""
        return _sparsemat.SparseMatrix_Inverse(self)

    def EliminateRow(self, *args):
        r"""
        EliminateRow(SparseMatrix self, int row, double const sol, Vector rhs)
        EliminateRow(SparseMatrix self, int row, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ZERO)
        """
        return _sparsemat.SparseMatrix_EliminateRow(self, *args)

    def EliminateCol(self, *args):
        r"""EliminateCol(SparseMatrix self, int col, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ZERO)"""
        return _sparsemat.SparseMatrix_EliminateCol(self, *args)

    def EliminateCols(self, cols, x=None, b=None):
        r"""EliminateCols(SparseMatrix self, intArray cols, Vector x=None, Vector b=None)"""
        return _sparsemat.SparseMatrix_EliminateCols(self, cols, x, b)

    def EliminateRowColMultipleRHS(self, *args):
        r"""EliminateRowColMultipleRHS(SparseMatrix self, int rc, Vector sol, DenseMatrix rhs, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ONE)"""
        return _sparsemat.SparseMatrix_EliminateRowColMultipleRHS(self, *args)

    def EliminateRowColDiag(self, rc, value):
        r"""EliminateRowColDiag(SparseMatrix self, int rc, double value)"""
        return _sparsemat.SparseMatrix_EliminateRowColDiag(self, rc, value)

    def EliminateRowCol(self, *args):
        r"""
        EliminateRowCol(SparseMatrix self, int rc, double const sol, Vector rhs, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ONE)
        EliminateRowCol(SparseMatrix self, int rc, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ONE)
        EliminateRowCol(SparseMatrix self, int rc, SparseMatrix Ae, mfem::Matrix::DiagonalPolicy dpolicy=DIAG_ONE)
        """
        return _sparsemat.SparseMatrix_EliminateRowCol(self, *args)

    def SetDiagIdentity(self):
        r"""SetDiagIdentity(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_SetDiagIdentity(self)

    def EliminateZeroRows(self, threshold=1e-12):
        r"""EliminateZeroRows(SparseMatrix self, double const threshold=1e-12)"""
        return _sparsemat.SparseMatrix_EliminateZeroRows(self, threshold)

    def Gauss_Seidel_forw(self, x, y):
        r"""Gauss_Seidel_forw(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_Gauss_Seidel_forw(self, x, y)

    def Gauss_Seidel_back(self, x, y):
        r"""Gauss_Seidel_back(SparseMatrix self, Vector x, Vector y)"""
        return _sparsemat.SparseMatrix_Gauss_Seidel_back(self, x, y)

    def GetJacobiScaling(self):
        r"""GetJacobiScaling(SparseMatrix self) -> double"""
        return _sparsemat.SparseMatrix_GetJacobiScaling(self)

    def Jacobi(self, b, x0, x1, sc):
        r"""Jacobi(SparseMatrix self, Vector b, Vector x0, Vector x1, double sc)"""
        return _sparsemat.SparseMatrix_Jacobi(self, b, x0, x1, sc)

    def DiagScale(self, b, x, sc=1.0):
        r"""DiagScale(SparseMatrix self, Vector b, Vector x, double sc=1.0)"""
        return _sparsemat.SparseMatrix_DiagScale(self, b, x, sc)

    def Jacobi2(self, b, x0, x1, sc=1.0):
        r"""Jacobi2(SparseMatrix self, Vector b, Vector x0, Vector x1, double sc=1.0)"""
        return _sparsemat.SparseMatrix_Jacobi2(self, b, x0, x1, sc)

    def Jacobi3(self, b, x0, x1, sc=1.0):
        r"""Jacobi3(SparseMatrix self, Vector b, Vector x0, Vector x1, double sc=1.0)"""
        return _sparsemat.SparseMatrix_Jacobi3(self, b, x0, x1, sc)

    def Finalize(self, *args):
        r"""
        Finalize(SparseMatrix self, int skip_zeros=1)
        Finalize(SparseMatrix self, int skip_zeros, bool fix_empty_rows)
        """
        return _sparsemat.SparseMatrix_Finalize(self, *args)

    def Finalized(self):
        r"""Finalized(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_Finalized(self)

    def areColumnsSorted(self):
        r"""areColumnsSorted(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_areColumnsSorted(self)

    def Threshold(self, tol, fix_empty_rows=False):
        r"""Threshold(SparseMatrix self, double tol, bool fix_empty_rows=False)"""
        return _sparsemat.SparseMatrix_Threshold(self, tol, fix_empty_rows)

    def GetBlocks(self, blocks):
        r"""GetBlocks(SparseMatrix self, mfem::Array2D< mfem::SparseMatrix * > & blocks)"""
        return _sparsemat.SparseMatrix_GetBlocks(self, blocks)

    def GetSubMatrix(self, rows, cols, subm):
        r"""GetSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm)"""
        return _sparsemat.SparseMatrix_GetSubMatrix(self, rows, cols, subm)

    def SetColPtr(self, row):
        r"""SetColPtr(SparseMatrix self, int const row)"""
        return _sparsemat.SparseMatrix_SetColPtr(self, row)

    def ClearColPtr(self):
        r"""ClearColPtr(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_ClearColPtr(self)

    def _Get_(self, col):
        r"""_Get_(SparseMatrix self, int const col) -> double"""
        return _sparsemat.SparseMatrix__Get_(self, col)

    def SearchRow(self, *args):
        r"""
        SearchRow(SparseMatrix self, int const col) -> double
        SearchRow(SparseMatrix self, int const row, int const col) -> double &
        """
        return _sparsemat.SparseMatrix_SearchRow(self, *args)

    def _Add_(self, *args):
        r"""
        _Add_(SparseMatrix self, int const col, double const a)
        _Add_(SparseMatrix self, int const row, int const col, double const a)
        """
        return _sparsemat.SparseMatrix__Add_(self, *args)

    def _Set_(self, *args):
        r"""
        _Set_(SparseMatrix self, int const col, double const a)
        _Set_(SparseMatrix self, int const row, int const col, double const a)
        """
        return _sparsemat.SparseMatrix__Set_(self, *args)

    def Set(self, i, j, a):
        r"""Set(SparseMatrix self, int const i, int const j, double const a)"""
        return _sparsemat.SparseMatrix_Set(self, i, j, a)

    def SetSubMatrix(self, rows, cols, subm, skip_zeros=1):
        r"""SetSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm, int skip_zeros=1)"""
        return _sparsemat.SparseMatrix_SetSubMatrix(self, rows, cols, subm, skip_zeros)

    def SetSubMatrixTranspose(self, rows, cols, subm, skip_zeros=1):
        r"""SetSubMatrixTranspose(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm, int skip_zeros=1)"""
        return _sparsemat.SparseMatrix_SetSubMatrixTranspose(self, rows, cols, subm, skip_zeros)

    def AddSubMatrix(self, rows, cols, subm, skip_zeros=1):
        r"""AddSubMatrix(SparseMatrix self, intArray rows, intArray cols, DenseMatrix subm, int skip_zeros=1)"""
        return _sparsemat.SparseMatrix_AddSubMatrix(self, rows, cols, subm, skip_zeros)

    def RowIsEmpty(self, row):
        r"""RowIsEmpty(SparseMatrix self, int const row) -> bool"""
        return _sparsemat.SparseMatrix_RowIsEmpty(self, row)

    def GetRow(self, row, cols, srow):
        r"""GetRow(SparseMatrix self, int const row, intArray cols, Vector srow) -> int"""
        return _sparsemat.SparseMatrix_GetRow(self, row, cols, srow)

    def SetRow(self, row, cols, srow):
        r"""SetRow(SparseMatrix self, int const row, intArray cols, Vector srow)"""
        return _sparsemat.SparseMatrix_SetRow(self, row, cols, srow)

    def AddRow(self, row, cols, srow):
        r"""AddRow(SparseMatrix self, int const row, intArray cols, Vector srow)"""
        return _sparsemat.SparseMatrix_AddRow(self, row, cols, srow)

    def ScaleRow(self, row, scale):
        r"""ScaleRow(SparseMatrix self, int const row, double const scale)"""
        return _sparsemat.SparseMatrix_ScaleRow(self, row, scale)

    def ScaleRows(self, sl):
        r"""ScaleRows(SparseMatrix self, Vector sl)"""
        return _sparsemat.SparseMatrix_ScaleRows(self, sl)

    def ScaleColumns(self, sr):
        r"""ScaleColumns(SparseMatrix self, Vector sr)"""
        return _sparsemat.SparseMatrix_ScaleColumns(self, sr)

    def __iadd__(self, B):
        r"""__iadd__(SparseMatrix self, SparseMatrix B) -> SparseMatrix"""
        val = _sparsemat.SparseMatrix___iadd__(self, B)

        val.thisown = 0
        return self


        return val


    def Add(self, *args):
        r"""
        Add(SparseMatrix self, int const i, int const j, double const a)
        Add(SparseMatrix self, double const a, SparseMatrix B)
        """
        return _sparsemat.SparseMatrix_Add(self, *args)

    def __imul__(self, a):
        r"""__imul__(SparseMatrix self, double a) -> SparseMatrix"""
        val = _sparsemat.SparseMatrix___imul__(self, a)

        val.thisown = 0
        return self


        return val


    def IsSymmetric(self):
        r"""IsSymmetric(SparseMatrix self) -> double"""
        return _sparsemat.SparseMatrix_IsSymmetric(self)

    def Symmetrize(self):
        r"""Symmetrize(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_Symmetrize(self)

    def NumNonZeroElems(self):
        r"""NumNonZeroElems(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_NumNonZeroElems(self)

    def MaxNorm(self):
        r"""MaxNorm(SparseMatrix self) -> double"""
        return _sparsemat.SparseMatrix_MaxNorm(self)

    def CountSmallElems(self, tol):
        r"""CountSmallElems(SparseMatrix self, double tol) -> int"""
        return _sparsemat.SparseMatrix_CountSmallElems(self, tol)

    def CheckFinite(self):
        r"""CheckFinite(SparseMatrix self) -> int"""
        return _sparsemat.SparseMatrix_CheckFinite(self)

    def SetGraphOwner(self, ownij):
        r"""SetGraphOwner(SparseMatrix self, bool ownij)"""
        return _sparsemat.SparseMatrix_SetGraphOwner(self, ownij)

    def SetDataOwner(self, owna):
        r"""SetDataOwner(SparseMatrix self, bool owna)"""
        return _sparsemat.SparseMatrix_SetDataOwner(self, owna)

    def OwnsGraph(self):
        r"""OwnsGraph(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_OwnsGraph(self)

    def OwnsData(self):
        r"""OwnsData(SparseMatrix self) -> bool"""
        return _sparsemat.SparseMatrix_OwnsData(self)

    def LoseData(self):
        r"""LoseData(SparseMatrix self)"""
        return _sparsemat.SparseMatrix_LoseData(self)

    def Swap(self, other):
        r"""Swap(SparseMatrix self, SparseMatrix other)"""
        return _sparsemat.SparseMatrix_Swap(self, other)
    __swig_destroy__ = _sparsemat.delete_SparseMatrix

    def GetType(self):
        r"""GetType(SparseMatrix self) -> mfem::Operator::Type"""
        return _sparsemat.SparseMatrix_GetType(self)

    def GetIArray(self):
        r"""GetIArray(SparseMatrix self) -> PyObject *"""
        return _sparsemat.SparseMatrix_GetIArray(self)

    def GetJArray(self):
        r"""GetJArray(SparseMatrix self) -> PyObject *"""
        return _sparsemat.SparseMatrix_GetJArray(self)

    def GetDataArray(self):
        r"""GetDataArray(SparseMatrix self) -> PyObject *"""
        return _sparsemat.SparseMatrix_GetDataArray(self)

    def Print(self, *args):
        r"""
        Print(SparseMatrix self, std::ostream & out=mfem::out, int width_=4)
        Print(SparseMatrix self, char const * file, int precision=8)
        """
        return _sparsemat.SparseMatrix_Print(self, *args)

    def PrintMatlab(self, *args):
        r"""
        PrintMatlab(SparseMatrix self, std::ostream & out=mfem::out)
        PrintMatlab(SparseMatrix self, char const * file, int precision=8)
        """
        return _sparsemat.SparseMatrix_PrintMatlab(self, *args)

    def PrintMM(self, *args):
        r"""
        PrintMM(SparseMatrix self, std::ostream & out=mfem::out)
        PrintMM(SparseMatrix self, char const * file, int precision=8)
        """
        return _sparsemat.SparseMatrix_PrintMM(self, *args)

    def PrintCSR(self, *args):
        r"""
        PrintCSR(SparseMatrix self, std::ostream & out)
        PrintCSR(SparseMatrix self, char const * file, int precision=8)
        PrintCSR(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_PrintCSR(self, *args)

    def PrintCSR2(self, *args):
        r"""
        PrintCSR2(SparseMatrix self, std::ostream & out)
        PrintCSR2(SparseMatrix self, char const * file, int precision=8)
        PrintCSR2(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_PrintCSR2(self, *args)

    def PrintInfo(self, *args):
        r"""
        PrintInfo(SparseMatrix self, std::ostream & out)
        PrintInfo(SparseMatrix self, char const * file, int precision=8)
        PrintInfo(SparseMatrix self)
        """
        return _sparsemat.SparseMatrix_PrintInfo(self, *args)

# Register SparseMatrix in _sparsemat:
_sparsemat.SparseMatrix_swigregister(SparseMatrix)


def SparseMatrixFunction(S, f):
    r"""SparseMatrixFunction(SparseMatrix S, double (*)(double) f)"""
    return _sparsemat.SparseMatrixFunction(S, f)

def TransposeAbstractSparseMatrix(A, useActualWidth):
    r"""TransposeAbstractSparseMatrix(AbstractSparseMatrix A, int useActualWidth) -> SparseMatrix"""
    return _sparsemat.TransposeAbstractSparseMatrix(A, useActualWidth)

def TransposeMult(A, B):
    r"""TransposeMult(SparseMatrix A, SparseMatrix B) -> SparseMatrix"""
    return _sparsemat.TransposeMult(A, B)

def MultAbstractSparseMatrix(A, B):
    r"""MultAbstractSparseMatrix(AbstractSparseMatrix A, AbstractSparseMatrix B) -> SparseMatrix"""
    return _sparsemat.MultAbstractSparseMatrix(A, B)

def Mult_AtDA(A, D, OAtDA=None):
    r"""Mult_AtDA(SparseMatrix A, Vector D, SparseMatrix OAtDA=None) -> SparseMatrix"""
    return _sparsemat.Mult_AtDA(A, D, OAtDA)

def OuterProduct(*args):
    r"""
    OuterProduct(DenseMatrix A, DenseMatrix B) -> DenseMatrix
    OuterProduct(DenseMatrix A, SparseMatrix B) -> SparseMatrix
    OuterProduct(SparseMatrix A, DenseMatrix B) -> SparseMatrix
    OuterProduct(SparseMatrix A, SparseMatrix B) -> SparseMatrix
    """
    return _sparsemat.OuterProduct(*args)

