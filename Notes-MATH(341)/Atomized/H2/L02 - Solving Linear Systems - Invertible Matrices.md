# Invertible Matrices

*Original Note: [[L02 - Solving Linear Systems]]*

> [!thm] Invertible Matrix Theorem (selected equivalences)
> For $A\in\mathbb{R}^{n\times n}$, the following are equivalent:
> - $A$ is invertible (nonsingular).
> - $\det(A)\neq 0$ and $0$ is not an eigenvalue of $A$.
> - $\operatorname{rank}(A)=n$ (full rank).
> - The nullspace is trivial: $\mathcal{N}(A)=\{0\}$.
> - The columns of $A$ are linearly independent and span $\mathbb{R}^n$.
> - For every $b\in\mathbb{R}^n$, the system $Ax=b$ has a unique solution.

> [!def] Solving via the inverse (formal)
> If $A$ is invertible and $Ax=b$, then
> $$
> A^{-1}Ax = A^{-1}b \;\Rightarrow\; x = A^{-1}b.
> $$
> This identity defines the inverse and shows uniqueness of the solution when $A^{-1}$ exists.

> [!imp] Important computational note
> Avoid forming $A^{-1}$ explicitly in numerical computations. Instead, solve $Ax=b$ via a factorization (e.g., LU or QR). This is typically faster and more numerically stable.
