# Cholesky Factorization

*Original Note: [L04](../s01/L04.md)*

## Overview and Definitions

> [!def] Cholesky Factorization
> For a symmetric positive definite (SPD) matrix $A \in \mathbb{R}^{n \times n}$, the Cholesky factorization is a decomposition
> $$
> A = R^T R,
> $$
> where $R$ is upper triangular with strictly positive diagonal entries. The matrix $R$ is called the Cholesky factor of $A$.

> [!def] Symmetric Matrix
> A matrix $A$ is symmetric if
> $$
> A = A^T.
> $$

> [!def] Positive Definite Matrix
> A symmetric matrix $A$ is positive definite if
> $$
> v^T A v > 0 \quad \text{for all } v \in \mathbb{R}^n \setminus \{0\}.
> $$

> [!thm] Cholesky Existence and Uniqueness
> If $A \in \mathbb{R}^{n \times n}$ is SPD, then there exists a unique upper triangular matrix $R$ with $r_{ii} > 0$ such that
> $$
> A = R^T R.
> $$

> [!def] Terminology
> - The factor $R$ in $A = R^T R$ is called the (upper-triangular) Cholesky factor.
> - Equivalently, one may write $A = L L^T$ with $L$ lower triangular and positive diagonal.


## Block Matrices

> [!def] Block Matrices and Conforming Partitions
> Given conformable block partitions, the product
> $$
> \begin{bmatrix}
> A_{11} & A_{12} \\
> A_{21} & A_{22}
> \end{bmatrix}
> \begin{bmatrix}
> X_{11} & X_{12} \\
> X_{21} & X_{22}
> \end{bmatrix}
> =
> \begin{bmatrix}
> B_{11} & B_{12} \\
> B_{21} & B_{22}
> \end{bmatrix}
> $$
> is defined when the inner block dimensions match. The subblocks are called submatrices (or blocks), and the partition must be conforming for block multiplication to be valid.

### Special Inverses

> [!case] Case A — Block Diagonal Inverse
> If $A$ and $B$ are invertible, then
> $$
> \begin{bmatrix}
> A & 0 \\
> 0 & B
> \end{bmatrix}^{-1}
> =
> \begin{bmatrix}
> A^{-1} & 0 \\
> 0 & B^{-1}
> \end{bmatrix}.
> $$

> [!case] Case B — Block Upper Triangular Inverse
> If $A$ and $B$ are invertible, then
> $$
> \begin{bmatrix}
> A & C \\
> 0 & B
> \end{bmatrix}^{-1}
> =
> \begin{bmatrix}
> A^{-1} & -A^{-1} C B^{-1} \\
> 0      & B^{-1}
> \end{bmatrix}.
> $$

> [!pf] Verification (Case B)
> Multiply:
> $$
> \begin{aligned}
> \begin{bmatrix}
> A & C \\
> 0 & B
> \end{bmatrix}
> \begin{bmatrix}
> A^{-1} & -A^{-1} C B^{-1} \\
> 0      & B^{-1}
> \end{bmatrix}
> &=
> \begin{bmatrix}
> A A^{-1} + C \cdot 0 & A(-A^{-1} C B^{-1}) + C B^{-1} \\
> 0 \cdot A^{-1} + B \cdot 0 & 0(-A^{-1} C B^{-1}) + B B^{-1}
> \end{bmatrix} \\
> &=
> \begin{bmatrix}
> I & -C B^{-1} + C B^{-1} \\
> 0 & I
> \end{bmatrix}
> =
> \begin{bmatrix}
> I & 0 \\
> 0 & I
> \end{bmatrix}.
> \end{aligned}
> $$

### General 2×2 Block Inversion via Schur Complements

Let
$$
D =
\begin{bmatrix}
A & C \\
R & B
\end{bmatrix}.
$$

> [!def] Schur Complements
> When the relevant inverses exist, define
> $$
> S := B - R A^{-1} C, \qquad
> T := A - C B^{-1} R.
> $$

> [!thm] Block Matrix Inversion via Schur Complements
> Suppose the indicated inverses exist.
> $$
> D^{-1}
> =
> \begin{cases}
> \begin{bmatrix}
> A^{-1} + A^{-1} C S^{-1} R A^{-1} & -A^{-1} C S^{-1} \\
> -S^{-1} R A^{-1}                   & \ \ \ \, S^{-1}
> \end{bmatrix},
> &
> \text{if } A \text{ and } S = B - R A^{-1} C \text{ are invertible}, \\[1.25em]
> \begin{bmatrix}
> T^{-1}                              & -T^{-1} C B^{-1} \\
> -B^{-1} R T^{-1}                    & B^{-1} + B^{-1} R T^{-1} C B^{-1}
> \end{bmatrix},
> &
> \text{if } B \text{ and } T = A - C B^{-1} R \text{ are invertible}.
> \end{cases}
> $$

> [!imp] Note on Invertibility
> Invertibility of $A$ (or $B$) alone does not guarantee $D$ is invertible; the corresponding Schur complement $S$ (or $T$) must also be invertible.
