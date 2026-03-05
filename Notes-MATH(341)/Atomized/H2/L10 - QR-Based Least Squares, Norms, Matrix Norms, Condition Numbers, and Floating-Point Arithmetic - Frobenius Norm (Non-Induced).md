# Frobenius Norm (Non-Induced)

*Original Note: [[L10 - QR-Based Least Squares, Norms, Matrix Norms, Condition Numbers, and Floating-Point Arithmetic]]*

> [!def] Frobenius norm
> For $A=[a_{ij}] \in \mathbb{R}^{m\times n}$,
> $$
> \|A\|_F = \Big(\sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^2\Big)^{1/2}
> \quad\text{and}\quad
> \|A\|_F = \sqrt{\operatorname{tr}(A^\top A)} = \sqrt{\operatorname{tr}(A A^\top)}.
> $$

Notes:
- The trace is $\operatorname{tr}(A)=\sum_i a_{ii}$ (no absolute values).
- $\|\cdot\|_F$ is unitarily (orthogonally) invariant but not induced by a vector norm.
- Relation to singular values: $\|A\|_F^2 = \sum_{k} \sigma_k(A)^2$.
