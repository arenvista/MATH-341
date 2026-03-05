# Condition Number of a Matrix

*Original Note: [[L10 - QR-Based Least Squares, Norms, Matrix Norms, Condition Numbers, and Floating-Point Arithmetic]]*

> [!def] Condition number (with respect to an induced norm)
> For a nonsingular $A\in\mathbb{R}^{n\times n}$,
> $$
> \kappa(A) := \|A\|\,\|A^{-1}\|.
> $$

Basic observations:
- $\kappa(I)=1$.
- For any nonsingular $A$, $\kappa(A)\ge 1$ (and equality holds, e.g., for orthogonal $A$ in the 2-norm).
- Scale invariance: $\kappa(\alpha A)=\kappa(A)$ for all $\alpha\ne 0$.
- In the 2-norm: $\kappa_2(A)=\dfrac{\sigma_{\max}(A)}{\sigma_{\min}(A)}$.

> [!imp] Interpretation and numerical implications
> - $\kappa(A)$ measures the sensitivity of the solution $x$ of $Ax=b$ to small perturbations in $A$ or $b$.
> - Large $\kappa(A)$ indicates ill-conditioning: the matrix is close to singular (its rows/columns are nearly linearly dependent), and small data or rounding errors can cause large solution errors.
> - For induced norms, by submultiplicativity,
>   $$
>   \|I\| = \|A A^{-1}\| \le \|A\|\,\|A^{-1}\| = \kappa(A),
>   $$
>   confirming $\kappa(A)\ge 1$.
