# Cholesky Factorization

*Original Note: [[L04]]*

Cholesky factorization is a specialized factorization for real symmetric positive definite (SPD) matrices.

## Symmetric Positive Definite (SPD)

> [!def] Symmetric Matrix
> A matrix $A \in \mathbb{R}^{n \times n}$ is symmetric if
> $$A = A^T.$$

> [!def] Positive Definite Matrix
> A symmetric matrix $A \in \mathbb{R}^{n \times n}$ is positive definite if
> $$v^T A v > 0 \quad \text{for all } v \in \mathbb{R}^n \setminus \{\vec{0}\}.$$

> [!imp] Notes
> - Every SPD matrix is nonsingular (invertible).
> - All eigenvalues of an SPD matrix are positive.

> [!thm] Cholesky Factorization — Existence and Uniqueness
> If $A \in \mathbb{R}^{n \times n}$ is SPD, then there exists a unique upper-triangular matrix $R$ with strictly positive diagonal entries such that
> $$A = R^T R.$$
> Equivalently, there exists a unique lower-triangular $L$ with positive diagonal such that $A = L L^T$.

> [!pf] Proof sketch
> Proceed by induction on $n$. For $n=1$, the claim is trivial. Assume the claim for $(n-1)\times(n-1)$ SPD matrices. Partition
> $$A = \begin{bmatrix} \alpha & a^T \\ a & B \end{bmatrix}, \quad \alpha \in \mathbb{R}, \; a \in \mathbb{R}^{n-1}, \; B \in \mathbb{R}^{(n-1)\times(n-1)}.$$
> Since $A$ is SPD, $\alpha>0$. Define $r_{11}=\sqrt{\alpha}$ and $r_{1,2:n} = r_{11}^{-1} a^T$. The Schur complement $S = B - r_{11}^{-2} a a^T$ is also SPD. By the induction hypothesis, $S = \tilde{R}^T \tilde{R}$ for some upper-triangular $\tilde{R}$ with positive diagonal. Then
> $$R = \begin{bmatrix} r_{11} & r_{1,2:n} \\ 0 & \tilde{R} \end{bmatrix}$$
> satisfies $A=R^T R$. Uniqueness follows from positivity of the diagonal and triangular structure.

> [!imp] Computational formulas (upper-triangular form)
> For $A=[a_{ij}]$ and $R=[r_{ij}]$ with $R$ upper-triangular,
> - Diagonal: $$r_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} r_{k i}^2} \quad (i=1,\dots,n).$$
> - Off-diagonal: $$r_{ij} = \frac{a_{ij} - \sum_{k=1}^{i-1} r_{k i} r_{k j}}{r_{ii}} \quad (1 \le i < j \le n).$$


## Block Matrices

> [!def] Block Matrices and Conforming Partitions
> Partitioned (block) matrices group entries into submatrices. For example,
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
> \end{bmatrix}.
> $$
> The partition is conforming if the inner block dimensions match so that block multiplication is well-defined.

### Block Matrix Inversion Identities

> [!case] Case A — Block Diagonal Inverse
> If $A$ and $B$ are invertible,
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

> [!case] Case B — Block Upper-Triangular Inverse
> If $A$ and $B$ are invertible,
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

> [!pf] Verification for Case B
> Multiply to check:
> $$
> \begin{aligned}
> &\begin{bmatrix} A & C \\ 0 & B \end{bmatrix}
> \begin{bmatrix} A^{-1} & -A^{-1} C B^{-1} \\ 0 & B^{-1} \end{bmatrix} \\
> &= \begin{bmatrix}
> AA^{-1} + C\cdot 0 & A(-A^{-1} C B^{-1}) + C B^{-1} \\
> 0\cdot A^{-1} + B\cdot 0 & 0\cdot(-A^{-1} C B^{-1}) + B B^{-1}
> \end{bmatrix}
> =
> \begin{bmatrix}
> I & 0 \\ 0 & I
> \end{bmatrix}.
> \end{aligned}
> $$

> [!def] Schur Complements
> For the block matrix
> $$
> D =
> \begin{bmatrix}
> A & C \\
> R & B
> \end{bmatrix},
> $$
> the Schur complements of $A$ in $D$ and of $B$ in $D$ are
> $$
> S := B - R A^{-1} C, \qquad T := A - C B^{-1} R,
> $$
> when $A^{-1}$ or $B^{-1}$ exists, respectively.

> [!thm] Block 2×2 Inversion via Schur Complements
> Let
> $$D = \begin{bmatrix} A & C \\ R & B \end{bmatrix}.$$
> - If $A$ and $S = B - R A^{-1} C$ are invertible, then
> $$
> D^{-1} =
> \begin{bmatrix}
> A^{-1} + A^{-1} C S^{-1} R A^{-1} & -A^{-1} C S^{-1} \\
> -S^{-1} R A^{-1} & S^{-1}
> \end{bmatrix}.
> $$
> - If $B$ and $T = A - C B^{-1} R$ are invertible, then
> $$
> D^{-1} =
> \begin{bmatrix}
> T^{-1} & -T^{-1} C B^{-1} \\
> -B^{-1} R T^{-1} & B^{-1} + B^{-1} R T^{-1} C B^{-1}
> \end{bmatrix}.
> $$

> [!pf] Proof idea
> Use block Gaussian elimination (block LU factorization). For example, if $A$ is invertible,
> $$
> \begin{aligned}
> D
> &= \begin{bmatrix} I & 0 \\ RA^{-1} & I \end{bmatrix}
> \begin{bmatrix} A & C \\ 0 & S \end{bmatrix}
> \begin{bmatrix} I & A^{-1} C \\ 0 & I \end{bmatrix}, \\
> D^{-1}
> &= \begin{bmatrix} I & -A^{-1} C \\ 0 & I \end{bmatrix}
> \begin{bmatrix} A^{-1} & 0 \\ 0 & S^{-1} \end{bmatrix}
> \begin{bmatrix} I & 0 \\ -R A^{-1} & I \end{bmatrix}.
> \end{aligned}
> $$
> Multiplying the factors yields the stated formula. The second case is analogous with roles of $A$ and $B$ swapped.
# Extractions -------------
# Cholesky Factorization

*Original Note: [[L04]]*

Cholesky factorization is a specialized factorization for real symmetric positive definite (SPD) matrices.

## Symmetric Positive Definite (SPD)

*Extracted to: [[L04 - Cholesky Factorization - Symmetric Positive Definite (SPD)]]*

## Block Matrices

*Extracted to: [[L04 - Cholesky Factorization - Block Matrices]]*

