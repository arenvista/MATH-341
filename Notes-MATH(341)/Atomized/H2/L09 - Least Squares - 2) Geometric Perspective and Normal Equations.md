# 2) Geometric Perspective and Normal Equations

*Original Note: [[L09 - Least Squares]]*

> [!thm] Normal Equations (Projection Condition)
> Let $A \in \mathbb{R}^{m\times n}$ and $b \in \mathbb{R}^m$. A vector $\bar{x}$ minimizes $\|Ax-b\|_2$ if and only if the residual $r:=b-A\bar{x}$ is orthogonal to the column space of $A$, i.e.,
> $$
> A^T(b-A\bar{x})=0
> \quad\Longleftrightarrow\quad
> A^TA\,\bar{x} = A^T b.
> $$
> If $A$ has full column rank, the solution is unique and
> $$
> \bar{x}=(A^T A)^{-1} A^T b.
> $$

> [!pf] Proof (sketch)
> The condition $r \perp \operatorname{Col}(A)$ is equivalent to $(Ax)^T r = 0$ for all $x$, i.e., $x^T A^T (b-A\bar{x})=0$ for all $x$. This holds iff $A^T(b-A\bar{x})=0$, which is the normal equation $A^T A\,\bar{x}=A^T b$.
