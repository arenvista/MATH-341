# Rectangular Systems and Echelon Form

*Original Note: [L04](../s01/L04.md)*

## Shapes and Typical Solution Behavior

Let $A \in \mathbb{R}^{m \times n}$.

- Tall-skinny (overdetermined), $m > n$:
  - Typically inconsistent; when inconsistent, solve in the least-squares sense.
- Square, $m = n$:
  - Unique solution if $A$ is nonsingular (e.g., solvable by LU, Cholesky for SPD, or iterative solvers).
  - If singular, there may be no solution or infinitely many solutions depending on $b$.
- Fat-short (underdetermined), $m < n$:
  - Infinitely many solutions if the system is consistent.

> [!def] Echelon Forms (REF/RREF)
> - Row Echelon Form (REF): all-zero rows at bottom; each leading (pivot) entry is to the right of the pivot in the row above.
> - Reduced Row Echelon Form (RREF): REF with each pivot equal to 1 and the only nonzero entry in its column.
