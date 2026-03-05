# Block Matrices

*Original Note: [[L04 - Cholesky Factorization]]*

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
