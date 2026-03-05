# Matrix Norms (Induced/Operator Norms)

*Original Note: [[L10 - QR-Based Least Squares, Norms, Matrix Norms, Condition Numbers, and Floating-Point Arithmetic]]*

> [!def] Induced (operator) matrix norm
> Let $\|\cdot\|$ be a vector norm on $\mathbb{R}^n$. The induced matrix norm of $A\in\mathbb{R}^{m\times n}$ is
> $$
> \|A\| := \sup_{x\ne 0} \frac{\|Ax\|}{\|x\|} = \sup_{\|x\|=1} \|Ax\|.
> $$
> Properties:
> - Consistency: $\|Ax\| \le \|A\|\,\|x\|$.
> - Submultiplicativity: $\|AB\| \le \|A\|\,\|B\|$.

Common induced norms:
- 1-norm (maximum column sum):
  $$
  \|A\|_1 = \max_{1\le j\le n} \sum_{i=1}^m |a_{ij}|.
  $$
- Infinity-norm (maximum row sum):
  $$
  \|A\|_\infty = \max_{1\le i\le m} \sum_{j=1}^n |a_{ij}|.
  $$
- 2-norm (spectral norm):
  $$
  \|A\|_2 = \sigma_{\max}(A) = \sqrt{\lambda_{\max}(A^\top A)}.
  $$

Additional facts:
- For orthogonal $Q$ (square, $Q^\top Q=I$): $\|Q\|_2 = 1$.
- For induced norms, $\|I\|=1$.
