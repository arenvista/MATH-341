# 8) Solving Least Squares Without Normal Equations

*Original Note: [[L09 - Least Squares]]*

> [! ?] What can we use instead of normal equations to solve least squares?
> QR factorization or SVD.

- QR factorization:
  $$
  A = Q R \quad (Q^T Q = I,\ R \text{ upper triangular}),
  $$
  $$
  \|Ax-b\|_2 = \|QRx-b\|_2 = \|Q^T(QRx-b)\|_2 = \|Rx - Q^T b\|_2.
  $$
  For $m\ge n$ (overdetermined), with economy QR $A=Q\begin{bmatrix}R\\0\end{bmatrix}$, write
  $$
  Q^T b = \begin{bmatrix} d \\ r \end{bmatrix},\quad R\in\mathbb{R}^{n\times n}.
  $$
  - Solve $R x = d$ by back-substitution.
  - The residual is the tail $r$; $\|r\|_2 = \min_x \|Ax-b\|_2$.

- SVD:
  $$
  A = U \Sigma V^T,\quad \hat{x} = A^+ b = V \Sigma^+ U^T b.
  $$
  - Numerically most robust; handles rank deficiency.
  - Provides the minimum-norm least-squares solution when solutions are not unique.
