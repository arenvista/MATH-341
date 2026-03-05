# Givens Rotations (Rotators)

*Original Note: [[L08 - Lecture L08 — Orthogonal Matrices Projectors, Reflectors, and Rotators]]*

> [!def] 2D rotation and plane rotations
> - In 2D, a rotation with parameters $(c,s)$, where $c^2+s^2=1$, can be written as
>   $$
>   G(c,s) = \begin{bmatrix} c & s \\ -s & c \end{bmatrix}.
>   $$
>   This is orthogonal: $G^TG=I$. One may take $c=\cos\theta$, $s=\sin\theta$.
> - In $\mathbb{R}^n$, a plane rotation $P_{i,j}(c,s)$ acts like $G(c,s)$ on coordinates $(i,j)$ and as the identity elsewhere.

Explicitly, for $1\le i<j\le n$,
$$
P_{i,j}(c,s) =
\begin{bmatrix}
I_{i-1} &        &        &        &        \\
        & c      & \cdots & s      &        \\
        & \vdots & I      & \vdots &        \\
        & -s     & \cdots & c      &        \\
        &        &        &        & I
\end{bmatrix},
\quad \text{with the 2\times 2 block on rows/cols }(i,j).
$$

> [!thm] Zeroing a coordinate with a Givens rotation
> Given a vector $x\in\mathbb{R}^n$ and indices $i<j$, choose
> $$
> r=\sqrt{x_i^2+x_j^2},\qquad
> c=\begin{cases} x_i/r, & r\neq 0 \\ 1, & r=0\end{cases},\qquad
> s=\begin{cases} x_j/r, & r\neq 0 \\ 0, & r=0\end{cases}.
> $$
> Then
> $$
> P_{i,j}(c,s)\,x
> \text{ has entries }
> \begin{cases}
> \text{position }i:~ r,\\
> \text{position }j:~ 0,
> \end{cases}
> \text{ and all other entries unchanged.}
> $$

> [!pf] Direct calculation on the 2D subvector
> For the subvector $[x_i,\,x_j]^T$, 
> $$
> \begin{bmatrix} c & s \\ -s & c \end{bmatrix}
> \begin{bmatrix} x_i \\ x_j \end{bmatrix}
> =
> \begin{bmatrix} cx_i + sx_j \\ -sx_i + cx_j \end{bmatrix}
> =
> \begin{bmatrix} r \\ 0 \end{bmatrix},
> $$
> since $cx_i+sx_j=(x_i^2+x_j^2)/r=r$ and $-sx_i+cx_j=0$.

Constructing a full annihilation to the first axis:
$$
\begin{aligned}
P_{1,2}x &= \begin{bmatrix} \sqrt{x_1^2+x_2^2}\\ 0\\ x_3\\ \vdots \end{bmatrix},\\
P_{1,3}P_{1,2}x &= \begin{bmatrix} \sqrt{x_1^2+x_2^2+x_3^2}\\ 0\\ 0\\ \vdots \end{bmatrix},\\
&\ \ \vdots\\
P_{1,n}\cdots P_{1,2}x &= \begin{bmatrix} \|x\|\\ 0\\ \vdots\\ 0 \end{bmatrix}.
\end{aligned}
$$

> [!imp] Efficiency note
> - Householder reflectors transform whole columns at once; for dense $m\times n$ matrices they are typically more efficient (fewer flops and better vectorization/cache use).
> - Givens rotations update only two rows (or columns) at a time; they are preferred for sparse matrices and for introducing/maintaining sparsity.

---
