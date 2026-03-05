# Partial Pivoting

*Original Note: [[L03 - LU Factorization]]*

> [!def] Partial Pivoting (Stability Heuristic)
> At step $k$, inspect column $k$ at/below the diagonal and swap the current pivot row $k$ with a row having the largest $|a_{ik}|$ (for $i\ge k$). This chooses a “large” pivot and reduces the effect of roundoff.
> 
> The factorization is written
> $$PA=LU,$$
> where $P$ accumulates the row swaps performed during elimination.
> 
> To solve $Ax=b$:
> - Compute $PA=LU$ by Gaussian elimination with partial pivoting.
> - Forward substitution: $Ly=Pb$.
> - Back substitution: $Ux=y$.
