# Matrix Factorization Methods

*Original Note: [[L02]]*

All factorization methods below are useful for solving linear systems $Ax=b$ (exactly when $A$ is square and nonsingular, or as least-squares solutions when $A$ is rectangular).

## Key Factorizations

$$
\begin{aligned}
& A = C R \quad &&\text{(Column–Row / skeleton factorization)}\\
& A = L U \quad &&\text{(LU factorization; with pivoting: }PA=LU\text{)}\\
& A = Q R \quad &&\text{(QR factorization; }Q\text{ orthonormal columns)}\\
& S = Q \Lambda Q^T \quad &&\text{(Spectral decomposition for symmetric }S)\\
& A = U \Sigma V^T \quad &&\text{(Singular Value Decomposition, SVD)}
\end{aligned}
$$

## CR (Column–Row) Factorization

> [!def] CR factorization (selecting independent columns)
> Let $A\in\mathbb{R}^{m\times n}$ have rank $r$. Choose $C\in\mathbb{R}^{m\times r}$ to be any matrix formed by $r$ linearly independent columns of $A$ (pivot columns). Then there exists $R\in\mathbb{R}^{r\times n}$ such that
> $$
> A = C R,
> $$
> where each column of $R$ gives the coefficients expressing the corresponding column of $A$ as a linear combination of the columns in $C$.
> 
> Notes:
> - Shapes: $A$ is $m\times n$, $C$ is $m\times r$, $R$ is $r\times n$.
> - If $C$ has full column rank, one convenient formula is $R = C^{\dagger} A = (C^T C)^{-1} C^T A$.
> - The choice of independent columns is not unique; different choices yield different $(C,R)$ with the same product.

> [!pf] Worked example (CR factorization)
> $$
> A=\begin{bmatrix}
> 1 & 2 & 4\\[2pt]
> 1 & 3 & 5
> \end{bmatrix}
> =
> \underbrace{\begin{bmatrix}
> 1 & 2\\[2pt]
> 1 & 3
> \end{bmatrix}}_{C=[\vec a_1\;\vec a_2]}
> \underbrace{\begin{bmatrix}
> 1 & 0 & 2\\[2pt]
> 0 & 1 & 1
> \end{bmatrix}}_{R}
> $$
> Check: $\vec a_3=\begin{bmatrix}4\\[2pt]5\end{bmatrix}=2\vec a_1+\vec a_2$, so the third column of $R$ is $\begin{bmatrix}2\\[2pt]1\end{bmatrix}$.

> [!pf] Worked example (rank-one as an outer product)
> $$
> A=\begin{bmatrix}2 & 4 & 6\\[2pt] 3 & 6 & 9\end{bmatrix}
> =
> \underbrace{\begin{bmatrix}2\\[2pt]3\end{bmatrix}}_{u}
> \underbrace{\begin{bmatrix}1 & 2 & 3\end{bmatrix}}_{v^T},
> $$
> so $\operatorname{rank}(A)=1$ and $A=uv^T$ is already a CR factorization with $C=u$ and $R=v^T$.

## LU Factorization

> [!def] LU factorization and solving $Ax=b$
> For a (typically square) matrix $A\in\mathbb{R}^{n\times n}$, an LU factorization writes
> $$
> A = LU,
> $$
> where $L$ is lower triangular (often with unit diagonal) and $U$ is upper triangular. In practice, partial pivoting is used:
> $$
> P A = L U,
> $$
> where $P$ is a permutation matrix.
> 
> To solve $Ax=b$:
> 1. Factor: $PA=LU$.
> 2. Apply the permutation: $\tilde b = Pb$.
> 3. Forward substitution: solve $Lc=\tilde b$ for $c$.
> 4. Back substitution: solve $Ux=c$ for $x$.

> [!cor] Computational cost and reuse
> - Computing $LU$ (without pivoting, dense case): $O(n^3)$ flops.
> - Each forward/back substitution (per right-hand side $b$): $O(n^2)$.
> - LU is especially efficient when solving $Ax=b$ for many different $b$’s with the same $A$ (factor once, reuse many times).

> [!imp] Practical note on pivoting
> Pivoting (PA=LU) improves numerical stability and ensures existence under mild conditions. Without pivoting, LU may fail or be unstable if leading principal minors vanish or are tiny.
# Extractions -------------
# Matrix Factorization Methods

*Original Note: [[L02]]*

All factorization methods below are useful for solving linear systems $Ax=b$ (exactly when $A$ is square and nonsingular, or as least-squares solutions when $A$ is rectangular).

## Key Factorizations

*Extracted to: [[L02 - Matrix Factorization Methods - Key Factorizations]]*

## CR (Column–Row) Factorization

*Extracted to: [[L02 - Matrix Factorization Methods - CR (Column–Row) Factorization]]*

## LU Factorization

*Extracted to: [[L02 - Matrix Factorization Methods - LU Factorization]]*

