# Practical Notes and Workflow

*Original Note: [[L03 - LU Factorization]]*

- For multiple right-hand sides $b^{(1)},\dots,b^{(m)}$, compute $PA=LU$ once; reuse it to solve all systems efficiently.
- When all leading principal minors are nonzero, you may use $A=LU$ directly (no pivoting). Otherwise, use $PA=LU$.
- $L$ is unit lower triangular; $U$ is upper triangular; $P$ is a permutation matrix with $P^{-1}=P^{\mathsf T}$.
