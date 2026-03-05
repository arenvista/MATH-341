# LU Factorization

*Original Note: [[L02 - Matrix Factorization Methods]]*

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
