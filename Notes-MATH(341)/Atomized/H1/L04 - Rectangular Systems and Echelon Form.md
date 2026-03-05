# Rectangular Systems and Echelon Form

*Original Note: [[L04]]*

We study solutions to $A x = b$ with $A \in \mathbb{R}^{m \times n}$ by shape.

## Solution Counts by Shape (Typical Behavior)

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


## Echelon Forms

> [!def] Row Echelon Form (REF)
> A matrix is in REF if:
> - All nonzero rows are above any all-zero rows.
> - Each leading (pivot) entry of a nonzero row is to the right of the leading entry of the row above it.
> - Entries below each pivot are zero.

> [!def] Reduced Row Echelon Form (RREF)
> A matrix is in RREF if it is in REF, and in addition:
> - Each pivot is 1.
> - Each pivot is the only nonzero entry in its column.
# Extractions -------------
# Rectangular Systems and Echelon Form

*Original Note: [[L04]]*

We study solutions to $A x = b$ with $A \in \mathbb{R}^{m \times n}$ by shape.

## Solution Counts by Shape (Typical Behavior)

*Extracted to: [[L04 - Rectangular Systems and Echelon Form - Solution Counts by Shape (Typical Behavior)]]*

## Echelon Forms

*Extracted to: [[L04 - Rectangular Systems and Echelon Form - Echelon Forms]]*

