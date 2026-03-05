# Solution Counts by Shape (Typical Behavior)

*Original Note: [[L04 - Rectangular Systems and Echelon Form]]*

- Tall-skinny (overdetermined), $m > n$:
  - Typically no exact solution for arbitrary $b$ (inconsistency when $b \notin \mathrm{Col}(A)$).
  - Least-squares solutions minimize $\|A x - b\|_2$.
  - Uniqueness of the least-squares solution holds if $A$ has full column rank ($\mathrm{rank}(A)=n$).
- Square, $m = n$:
  - Unique solution iff $A$ is nonsingular (e.g., via LU, Cholesky for SPD, or iterative solvers).
  - If singular, either no solution or infinitely many, depending on $b$.
- Fat-short (underdetermined), $m < n$:
  - If consistent, infinitely many solutions (free variables).
  - The minimum-norm solution is given by the pseudoinverse when needed.

> [!imp] Takeaway
> - Exact solvability depends on whether $b \in \mathrm{Col}(A)$.
> - Uniqueness depends on rank conditions (full column rank for overdetermined unique LS; nonsingularity for square; underdetermined systems are non-unique unless regularized).
