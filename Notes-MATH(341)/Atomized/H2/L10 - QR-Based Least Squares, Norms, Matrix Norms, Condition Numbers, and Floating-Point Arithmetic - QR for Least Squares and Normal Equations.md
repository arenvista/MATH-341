# QR for Least Squares and Normal Equations

*Original Note: [[L10 - QR-Based Least Squares, Norms, Matrix Norms, Condition Numbers, and Floating-Point Arithmetic]]*

Let $A \in \mathbb{R}^{m \times n}$ with $m \ge n$. Suppose $A$ has full column rank $n$ and admits a (thin) QR factorization
$$
A = Q R, \quad Q \in \mathbb{R}^{m \times n}\ \text{with } Q^\top Q = I_n,\quad R \in \mathbb{R}^{n \times n}\ \text{upper triangular}.
$$

> [!lem] Orthogonal invariance of the 2-norm
> For any orthogonal (square) matrix $U$ and any $z$, we have $\|Uz\|_2 = \|z\|_2$.

> [!thm] Least-squares via QR
> Consider the least-squares problem $\min_x \|Ax - b\|_2$. Let $A=QR$ be a thin QR factorization with $Q^\top Q=I_n$.
> - Extend $Q$ to an $m\times m$ orthogonal matrix $\widehat{Q} = [Q\ Q_\perp]$.
> - Then
>   $$
>   \|Ax - b\|_2
>   = \|\widehat{Q}^\top(Ax - b)\|_2
>   = \left\|\begin{bmatrix} R \\ 0 \end{bmatrix}x - \begin{bmatrix} Q^\top b \\ Q_\perp^\top b \end{bmatrix}\right\|_2
>   = \sqrt{\|Rx - Q^\top b\|_2^2 + \|Q_\perp^\top b\|_2^2}.
>   $$
> - The minimizer $x^\star$ therefore satisfies the upper-triangular system
>   $$
>   R x^\star = Q^\top b,
>   $$
>   and the minimum residual norm is $\|Q_\perp^\top b\|_2$.

> [!pf]
> By orthogonal invariance, premultiplying by $\widehat{Q}^\top$ preserves the 2-norm. The expression separates into a sum of squares, where only the first block depends on $x$. Minimizing over $x$ amounts to solving $Rx=Q^\top b$ because $R$ is nonsingular when $A$ has full column rank (upper triangular with nonzero diagonal).

> [!cor] Normal equations via QR
> The normal equations $A^\top A x = A^\top b$ become
> $$
> (QR)^\top (QR) x = (QR)^\top b
> \ \Longrightarrow\ 
> R^\top Q^\top Q R x = R^\top Q^\top b
> \ \Longrightarrow\
> R^\top R x = R^\top Q^\top b.
> $$
> If $R$ is nonsingular, left-multiplying by $R^{-\top}$ yields $Rx=Q^\top b$.

Notes:
- $R$ is upper triangular with nonzero diagonal entries (full column rank), hence $R$ is nonsingular.
- The QR approach avoids explicitly forming $A^\top A$, which is numerically preferable and often more stable.
