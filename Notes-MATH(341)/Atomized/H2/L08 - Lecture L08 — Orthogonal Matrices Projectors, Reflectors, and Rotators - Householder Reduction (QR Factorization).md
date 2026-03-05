# Householder Reduction (QR Factorization)

*Original Note: [[L08 - Lecture L08 — Orthogonal Matrices Projectors, Reflectors, and Rotators]]*

Goal: Reduce $A\in\mathbb{R}^{m\times n}$ ($m\ge n$) to upper triangular form using Householder reflectors.

Let $A=[a_1\,a_2\,\cdots\,a_n]$.

> [!def] One-step Householder transform
> - Take $x$ as the first column (or trailing subcolumn) to be reduced.
> - Form $u = x - \alpha e_1$ with $\alpha=-\operatorname{sign}(x_1)\|x\|$, then $v=u/\|u\|$.
> - Define $R_1=I-2vv^T$ of appropriate size (identity on untouched rows/cols).

After the first step,
$$
R_1 A =
\begin{bmatrix}
t_{1,1} & \ast\\
0       & A_2
\end{bmatrix},
\qquad
t_{1,1}=\pm\|a_1\|.
$$

Proceed recursively on the trailing submatrix $A_2$:

- Step k ($k=1,\dots,\min(m,n)$): construct $R_k$ acting on rows $k:\!m$ to zero out entries below $t_{k,k}$ in column $k$.

After $p=\min(m,n)$ steps,
$$
R_p\cdots R_2 R_1 A = 
\begin{bmatrix}
t_{1,1} & t_{1,2} & \cdots & t_{1,n}\\
0       & t_{2,2} & \cdots & t_{2,n}\\
\vdots  & \vdots  & \ddots & \vdots \\
0       & 0       & \cdots & t_{p,n}\\
\vdots  & \vdots  &        & \vdots
\end{bmatrix}
= R \quad (\text{upper triangular in its leading } n\times n \text{ block}).
$$

Define
$$
P = R_p \cdots R_2 R_1 \quad\Rightarrow\quad R = P A.
$$
Since each $R_k$ is orthogonal, so is $P$. Set
$$
Q = P^T \quad\Rightarrow\quad A = Q R, \quad Q^T Q = I.
$$

> [!imp] Notes and conventions
> - Signs on the diagonal of $R$ can be standardized (e.g., positive) by flipping signs in the corresponding Householder vectors; this only changes $Q$ by a column sign.
> - If a Householder vector uses a non-unit $u$, then 
>   $$
>   R_k = I - 2\frac{uu^T}{u^T u}.
>   $$

---
