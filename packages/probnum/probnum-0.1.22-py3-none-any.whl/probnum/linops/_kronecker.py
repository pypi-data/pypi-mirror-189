"""Operators of Kronecker-type or related."""
from __future__ import annotations

from typing import Optional, Union

import numpy as np

from probnum.typing import DTypeLike, LinearOperatorLike, NotImplementedType

from . import _linear_operator, _utils


class Symmetrize(_linear_operator.LambdaLinearOperator):
    r"""Symmetrizes a vector in its matrix representation.

    Given a vector :math:`x=\operatorname{vec}(X)`
    representing a square matrix :math:`X`,
    this linear operator computes :math:
    `y=\operatorname{vec}(\frac{1}{2}(X + X^\top))`.

    Parameters
    ----------
    n :
        Dimension of matrix X.
    dtype :
        Data type.
    """

    def __init__(self, n: int, dtype: DTypeLike = np.double):
        self._n = n

        super().__init__(
            shape=2 * (self._n**2,),
            dtype=dtype,
            matmul=self._matmul,
        )

    def _astype(
        self, dtype: np.dtype, order: str, casting: str, copy: bool
    ) -> "Symmetrize":
        if self.dtype == dtype:
            return self
        else:
            return Symmetrize(self._n, dtype=dtype)

    def _matmul(self, x: np.ndarray) -> np.ndarray:
        # vec(X) -> X, i.e. reshape into stack of matrices
        y = np.swapaxes(x, -2, -1)

        if not y.flags.c_contiguous:
            y = y.copy(order="C")

        y = y.reshape(y.shape[:-1] + (self._n, self._n))

        # Symmetrize Matrices
        y_transpose = np.swapaxes(y, -2, -1)
        y = 0.5 * (y + y_transpose)

        # Y -> vec(y), i.e. revert to stack of vectorized matrices
        y = y.reshape(y.shape[:-2] + (-1,))
        y = np.swapaxes(y, -1, -2)

        return y.astype(
            np.result_type(self.dtype, x.dtype), order="K", casting="safe", copy=False
        )


class Kronecker(_linear_operator.LambdaLinearOperator):
    """Kronecker product of two linear operators.

    The Kronecker product [1]_ :math:`A \\otimes B` of two linear operators :math:`A`
    and :math:`B` is given by

    .. math::
        A \\otimes B = \\begin{bmatrix}
            A_{11} B   &  \\dots   & A_{1 m_1} B  \\\\
            \\vdots     &  \\ddots  & \\vdots \\\\
            A_{n_11} B &  \\dots   & A_{n_1 m_1} B
        \\end{bmatrix}

    where :math:`A_{ij}v=A(v_j e_i)`, where :math:`e_i` is the :math:`i^{\\text{th}}`
    unit vector. The result is a new linear operator mapping from
    :math:`\\mathbb{R}^{n_1n_2}` to :math:`\\mathbb{R}^{m_1m_2}`. By recognizing that
    :math:`(A \\otimes B)\\operatorname{vec}(X) = AXB^{\\top}`, the Kronecker product
    can be understood as "translation" between matrix multiplication and (row-wise)
    vectorization.

    Parameters
    ----------
    A : np.ndarray or LinearOperator
        The first operator.
    B : np.ndarray or LinearOperator
        The second operator.
    dtype : dtype
        Data type of the operator.

    References
    ----------
    .. [1] Van Loan, C. F., The ubiquitous Kronecker product, *Journal of Computational
        and Applied Mathematics*, 2000, 123, 85-100

    See Also
    --------
    SymmetricKronecker : The symmetric Kronecker product of two linear operators.
    """

    # todo: extend this to list of operators
    def __init__(self, A: LinearOperatorLike, B: LinearOperatorLike):
        self.A = _utils.aslinop(A)
        self.B = _utils.aslinop(B)

        if self.A.is_square and self.B.is_square:
            # (A (x) B)^-1 = A^-1 (x) B^-1
            inverse = lambda: Kronecker(A=self.A.inv(), B=self.B.inv())
            cond = self._cond_square_factors
            # det(A (x) B) = det(A)^n * det(B)^m
            det = lambda: (
                self.A.det() ** self.B.shape[0] * self.B.det() ** self.A.shape[0]
            )
            logabsdet = lambda: (
                self.B.shape[0] * self.A.logabsdet()
                + self.A.shape[0] * self.B.logabsdet()
            )
            trace = lambda: self.A.trace() * self.B.trace()
        else:
            inverse = None
            cond = None
            det = None
            logabsdet = None
            trace = None

        super().__init__(
            dtype=np.result_type(self.A.dtype, self.B.dtype),
            shape=(
                self.A.shape[0] * self.B.shape[0],
                self.A.shape[1] * self.B.shape[1],
            ),
            matmul=lambda x: _kronecker_matmul(self.A, self.B, x),
            todense=lambda: np.kron(
                self.A.todense(cache=False), self.B.todense(cache=False)
            ),
            # (A (x) B)^T = A^T (x) B^T
            transpose=lambda: Kronecker(A=self.A.T, B=self.B.T),
            inverse=inverse,
            rank=lambda: self.A.rank() * self.B.rank(),
            cond=cond,
            det=det,
            logabsdet=logabsdet,
            trace=trace,
        )

        if self.A.is_symmetric and self.B.is_symmetric:
            self.is_symmetric = True

    def _astype(
        self, dtype: DTypeLike, order: str, casting: str, copy: bool
    ) -> "Kronecker":
        A_astype = self.A.astype(dtype, order=order, casting=casting, copy=copy)
        B_astype = self.B.astype(dtype, order=order, casting=casting, copy=copy)

        if A_astype is self.A and B_astype is self.B:
            return self

        return Kronecker(A_astype, B_astype)

    def _cond_square_factors(self, p) -> np.inexact:
        if p is None or p in (2, 1, np.inf, "fro", -2, -1, -np.inf):
            return self.A.cond(p=p) * self.B.cond(p=p)

        return np.linalg.cond(self.todense(cache=False), p=p)

    def _matmul_kronecker(self, other: "Kronecker") -> "Kronecker":
        if self.shape[1] != other.shape[0]:
            raise ValueError(
                f"matmul received invalid shapes {self.shape} @ {other.shape}"
            )

        _A, _B = self.A, self.B
        _C, _D = other.A, other.B
        if not (_A.shape[1] == _C.shape[0] and _B.shape[1] == _D.shape[0]):
            return NotImplemented

        # Using (A (x) B) @ (C (x) D) = (A @ C) (x) (B @ D)
        return Kronecker(A=_A @ _C, B=_B @ _D)

    def _add_kronecker(
        self, other: "Kronecker"
    ) -> Union[NotImplementedType, "Kronecker"]:

        if self.A is other.A or self.A == other.A:
            return Kronecker(A=self.A, B=self.B + other.B)

        if self.B is other.B or self.B == other.B:
            return Kronecker(A=self.A + other.A, B=other.B)

        return NotImplemented

    def _sub_kronecker(
        self, other: "Kronecker"
    ) -> Union[NotImplementedType, "Kronecker"]:

        if self.A is other.A or self.A == other.A:
            return Kronecker(A=self.A, B=self.B - other.B)

        if self.B is other.B or self.B == other.B:
            return Kronecker(A=self.A - other.A, B=other.B)

        return NotImplemented

    def _cholesky(self, lower: bool = True) -> Kronecker:
        # A Kronecker product is symmetric iff its factors are symmetric, since
        # (A (x) B)^T = A^T (x) B^T
        assert self.A.is_symmetric and self.B.is_symmetric

        return Kronecker(
            A=self.A.cholesky(lower),
            B=self.B.cholesky(lower),
        )

    def _symmetrize(self) -> _linear_operator.LinearOperator:
        # This is only an approximation to the closest symmetric matrix in the
        # Frobenius norm, which is however much more efficient than the exact
        # solution to the optimization problem
        if self.A.is_square and self.B.is_square:
            return Kronecker(
                A=self.A.symmetrize(),
                B=self.B.symmetrize(),
            )

        return super()._symmetrize()


def _kronecker_matmul(
    A: _linear_operator.LinearOperator,
    B: _linear_operator.LinearOperator,
    x: np.ndarray,
):
    """Efficient multiplication via (A (x) B)vec(X) = vec(AXB^T) where vec is the
    row-wise vectorization operator.
    """
    # vec(X) -> X, i.e. reshape into stack of matrices
    y = np.swapaxes(x, -2, -1)

    if not y.flags.c_contiguous:
        y = y.copy(order="C")

    y = y.reshape(y.shape[:-1] + (A.shape[1], B.shape[1]))

    # (X @ B.T).T = B @ X.T
    y = B @ np.swapaxes(y, -1, -2)

    # A @ X @ B.T = A @ (B @ X.T).T
    y = A @ np.swapaxes(y, -1, -2)

    # vec(A @ X @ B.T), i.e. revert to stack of vectorized matrices
    y = y.reshape(y.shape[:-2] + (-1,))
    y = np.swapaxes(y, -1, -2)

    return y


class SymmetricKronecker(_linear_operator.LambdaLinearOperator):
    """Symmetric Kronecker product of two linear operators.

    The symmetric Kronecker product [1]_ :math:`A \\otimes_{s} B` of two square linear
    operators :math:`A` and :math:`B` maps a symmetric linear operator :math:`X` to
    :math:`\\mathbb{R}^{\\frac{1}{2}n (n+1)}`. It is given by

    .. math::
        (A \\otimes_{s} B)\\operatorname{svec}(X) = \\frac{1}{2} \\operatorname{svec}(AXB^{\\top} + BXA^{\\top})

    where :math:`\\operatorname{svec}(X) = (X_{11}, \\sqrt{2} X_{12}, \\dots, X_{1n},
    X_{22}, \\sqrt{2} X_{23}, \\dots, \\sqrt{2}X_{2n}, \\dots X_{nn})^{\\top}` is the
    (row-wise, normalized) symmetric stacking operator. The implementation is based on
    the relationship :math:`Q^\\top \\operatorname{svec}(X) = \\operatorname{vec}(X)`
    with an orthonormal matrix :math:`Q` [2]_.

    Note
    ----
    The symmetric Kronecker product has a symmetric matrix representation if both
    :math:`A` and :math:`B` are symmetric.

    References
    ----------
    .. [1] Van Loan, C. F., The ubiquitous Kronecker product, *Journal of Computational
       and Applied Mathematics*, 2000, 123, 85-100
    .. [2] De Klerk, E., Aspects of Semidefinite Programming, *Kluwer Academic
       Publishers*, 2002

    See Also
    --------
    Kronecker : The Kronecker product of two linear operators.
    """  # pylint: disable=line-too-long

    # TODO: update documentation to map from n2xn2 to matrices of rank 1/2n(n+1),
    # representation symmetric n2xn2

    def __init__(
        self,
        A: LinearOperatorLike,
        B: Optional[LinearOperatorLike] = None,
    ):
        self.A = _utils.aslinop(A)

        if not self.A.is_square:
            raise ValueError("`A` must be square")

        self._n = self.A.shape[0]

        if B is None:
            self._identical_factors = True

            self.B = self.A

            dtype = self.A.dtype
            matmul = lambda x: _kronecker_matmul(self.A, self.A, x)
            todense = self._todense_identical_factors
            # (A (x)_s A)^T = A^T (x)_s A^T
            transpose = lambda: SymmetricKronecker(A=self.A.T)
            # (A (x)_s A)^-1 = (A (x) A)^-1 = A^-1 (x) A^-1
            inverse = lambda: SymmetricKronecker(A=self.A.inv())
            rank = lambda: self.A.rank() ** 2
            cond = self._cond_identical_factors
            det = lambda: self.A.det() ** (2 * self._n)
            logabsdet = lambda: 2 * self._n * self.A.logabsdet()
        else:
            self._identical_factors = False

            self.B = _utils.aslinop(B)

            if self.A.shape != self.B.shape:
                raise ValueError("`A` and `B` must have the same shape")

            dtype = np.result_type(self.A.dtype, self.B.dtype, 0.5)
            matmul = self._matmul_different_factors
            todense = self._todense_different_factors
            # (A (x)_s B)^T = A^T (x)_s B^T
            transpose = lambda: SymmetricKronecker(A=self.A.T, B=self.B.T)
            inverse = None
            rank = None
            cond = None
            det = None
            logabsdet = None

        super().__init__(
            dtype=dtype,
            shape=2 * (self._n**2,),
            matmul=matmul,
            todense=todense,
            transpose=transpose,
            inverse=inverse,
            rank=rank,
            cond=cond,
            det=det,
            logabsdet=logabsdet,
            trace=lambda: (
                (self.A.trace() * self.B.trace()).astype(self.dtype, copy=False)
            ),
        )

        if self.A.is_symmetric and self.B.is_symmetric:
            self.is_symmetric = True

    @property
    def identical_factors(self) -> bool:
        return self._identical_factors

    def _astype(
        self, dtype: DTypeLike, order: str, casting: str, copy: bool
    ) -> Union["SymmetricKronecker", _linear_operator.LinearOperator]:
        if self._identical_factors:
            A_astype = self.A.astype(dtype, order=order, casting=casting, copy=copy)

            if A_astype is self.A:
                return self

            return SymmetricKronecker(A_astype)
        elif np.issubdtype(dtype, np.floating):
            A_astype = self.A.astype(dtype, order=order, casting=casting, copy=copy)
            B_astype = self.B.astype(dtype, order=order, casting=casting, copy=copy)

            if A_astype is self.A and B_astype is self.B:
                return self

            return SymmetricKronecker(A_astype, B_astype)
        else:
            return super()._astype(dtype, order, casting, copy)

    def _matmul_different_factors(self, x: np.ndarray) -> np.ndarray:
        """Efficient multiplication via (A (x)_s B)vec(X) = 1/2 vec(BXA^T + AXB^T) where
        vec is the column-wise normalized symmetric stacking operator.
        """
        # vec(X) -> X, i.e. reshape into stack of matrices
        y = np.swapaxes(x, -2, -1)

        if not y.flags.c_contiguous:
            y = y.copy(order="C")

        y = y.reshape(y.shape[:-1] + (self._n, self._n))

        # A @ X @ B.T = A @ (B @ X.T).T
        y1 = self.B @ np.swapaxes(y, -1, -2)
        y1 = self.A @ np.swapaxes(y1, -1, -2)

        # B @ X @ A.T = B @ (A @ X.T).T
        y2 = self.A @ np.swapaxes(y, -1, -2)
        y2 = self.B @ np.swapaxes(y2, -1, -2)

        # 1/2 (AXB^T + BXA^T)
        y = 0.5 * (y1 + y2)

        # Revert to stack of vectorized matrices
        y = y.reshape(y.shape[:-2] + (-1,))
        y = np.swapaxes(y, -1, -2)

        return y

    def _todense_identical_factors(self) -> np.ndarray:
        """Dense representation of the symmetric Kronecker product."""
        # 1/2 (A (x) B + B (x) A)
        A_dense = self.A.todense(cache=False)
        return np.kron(A_dense, A_dense)

    def _todense_different_factors(self) -> np.ndarray:
        # 1/2 (A (x) B + B (x) A)
        A_dense = self.A.todense(cache=False)
        B_dense = self.B.todense(cache=False)
        return 0.5 * (np.kron(A_dense, B_dense) + np.kron(B_dense, A_dense))

    def _cond_identical_factors(self, p) -> np.inexact:
        if p is None or p in (2, 1, np.inf, "fro", -2, -1, -np.inf):
            return self.A.cond(p=p) * self.B.cond(p=p)

        return np.linalg.cond(self.todense(cache=False), p=p)

    def _cholesky(self, lower: bool = True) -> _linear_operator.LinearOperator:
        if self._identical_factors:
            return SymmetricKronecker(A=self.A.cholesky(lower))

        return super()._cholesky(lower)

    def _symmetrize(self) -> SymmetricKronecker:
        # This is only an approximation to the closest symmetric matrix in the
        # Frobenius norm, which is however much more efficient than the exact
        # solution to the optimization problem
        if self._identical_factors:
            return SymmetricKronecker(A=self.A.symmetrize())

        return SymmetricKronecker(A=self.A.symmetrize(), B=self.B.symmetrize())


class IdentityKronecker(_linear_operator.LambdaLinearOperator):
    """Block-diagonal linear operator.

    Parameters
    ----------
    num_blocks :
        Number of blocks.
    B :
        Block.
    """

    def __init__(self, num_blocks: int, B: LinearOperatorLike):
        self._num_blocks = num_blocks
        self.A = _linear_operator.Identity(num_blocks)
        self.B = _utils.aslinop(B)

        if self.B.is_square:
            # det(A (x) B) = det(A)^n * det(B)^m
            det = lambda: (self.B.det() ** self.A.shape[0])
            logabsdet = lambda: (self.A.shape[0] * self.B.logabsdet())
            trace = lambda: self.A.trace() * self.B.trace()
        else:
            det = None
            logabsdet = None
            trace = None

        super().__init__(
            dtype=np.result_type(self.A.dtype, self.B.dtype),
            shape=(
                num_blocks * self.B.shape[0],
                num_blocks * self.B.shape[1],
            ),
            matmul=lambda x: _kronecker_matmul(
                self.A, self.B, x
            ),  # TODO: can be implemented more efficiently
            todense=lambda: np.kron(
                self.A.todense(cache=False), self.B.todense(cache=False)
            ),
            # (A (x) B)^T = A (x) B^T
            transpose=lambda: IdentityKronecker(self._num_blocks, B=self.B.T),
            # (A (x) B)^-1 = A^-1 (x) B^-1
            inverse=lambda: IdentityKronecker(num_blocks, B=self.B.inv()),
            rank=lambda: self.A.rank() * self.B.rank(),
            cond=self._cond,
            det=det,
            logabsdet=logabsdet,
            trace=trace,
        )

        if self.B.is_symmetric:
            self.is_symmetric = True

    @property
    def num_blocks(self):
        return self._num_blocks

    def _matmul_idkronecker(self, other: "IdentityKronecker") -> "IdentityKronecker":
        if self.shape[1] != other.shape[0]:
            raise ValueError(
                f"matmul received invalid shapes {self.shape} @ {other.shape}"
            )

        _A, _B = self.A, self.B
        _C, _D = other.A, other.B
        if not (_A.shape[1] == _C.shape[0] and _B.shape[1] == _D.shape[0]):
            return NotImplemented

        # Using (A (x) B) @ (C (x) D) = (A @ C) (x) (B @ D)
        return IdentityKronecker(num_blocks=self._num_blocks, B=_B @ _D)

    def _add_idkronecker(
        self, other: "IdentityKronecker"
    ) -> Union[NotImplementedType, "IdentityKronecker"]:

        if self.A.shape == other.A.shape:
            return IdentityKronecker(num_blocks=self._num_blocks, B=self.B + other.B)

        return NotImplemented

    def _sub_idkronecker(
        self, other: "IdentityKronecker"
    ) -> Union[NotImplementedType, "IdentityKronecker"]:

        if self.A.shape == other.A.shape:
            return IdentityKronecker(num_blocks=self._num_blocks, B=self.B - other.B)

        return NotImplemented

    def _cond(
        self, p: Optional[Union[None, int, str, np.floating]] = None
    ) -> np.number:
        if p is None or p in (2, 1, np.inf, "fro", -2, -1, -np.inf):
            return self.A.cond(p=p) * self.B.cond(p=p)

        return np.linalg.cond(self.todense(cache=False), p=p)

    def _cholesky(self, lower: bool = True) -> IdentityKronecker:
        return IdentityKronecker(
            num_blocks=self.num_blocks,
            B=self.B.cholesky(lower),
        )

    def _symmetrize(self) -> IdentityKronecker:
        # In contrast to the implementation for the generic Kronecker product, this is
        # not only an approximation of the closes symmetric matrix in the Frobenius norm
        return IdentityKronecker(
            num_blocks=self.num_blocks,
            B=self.B.symmetrize(),
        )
