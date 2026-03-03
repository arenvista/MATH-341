# L08 — Orthogonal Matrices: Reflectors and Rotators

*Original Note: [L08](../s01/L08.md)*

## Recall: Types of Orthogonal Matrices
- Permutation matrices
- Reflectors (Householder)
- Rotators (Givens/plane rotations)
- ...

---

## Elementary Orthogonal Projector

> [!def] Elementary orthogonal projector onto u⊥
> 
> Let $u \in \mathbb{R}^n$ with $\|u\| = 1$. Define
> $$
> Q \;=\; I - u u^\top.
> $$
> Then $Q$ is the orthogonal projector onto $u_\perp$ and $P_u := I - Q = u u^\top$ is the projector onto $\mathrm{span}\{u\}$.
> 
> If $u$ is not normalized,
> $$
> Q \;=\; I - \frac{u u^\top}{u^\top u}, 
> \qquad
> P_u \;=\; \frac{u u^\top}{u^\top u}.
> $$

Basic properties (for any $x \in \mathbb{R}^n$):
- Decomposition and orthogonality:
  $$
  x = (I-Q)x + Qx, 
  \qquad (I-Q)x \perp Qx.
  $$
- Explicit projection onto the $u$-line:
  $$
  P_u x = (u^\top x)\,u, 
  \qquad \|P_u x\| = |u^\top x|.
  $$

> [!def] Standard basis vectors and elementary operations
> 
> Let $e_i \in \mathbb{R}^n$ denote the $i$-th standard basis vector (used in elementary row/column operations).
> A typical elementary “row-add” matrix has the form
> $$
> L \;=\; I - \alpha\, e_i e_j^\top \quad (\text{for some scalar } \alpha),
> $$
> which adds $-\alpha$ times row $j$ to row $i$ when left-multiplying a matrix.

---

## Elementary Reflectors (Householder)

> [!def] Householder reflector
> 
> Let $u \in \mathbb{R}^n$ with $\|u\|=1$. Define
> $$
> R \;=\; I - 2 u u^\top,
> $$
> which is the reflection across the hyperplane $u_\perp$.
> 
> If $u$ is not normalized,
> $$
> R \;=\; I - \frac{2 u u^\top}{u^\top u}.
> $$

> [!thm] Properties of Householder reflectors
> 
> $$
> R^\top = R \quad (\text{symmetric}), 
> \qquad R^\top R = I \quad (\text{orthogonal}),
> \qquad R^2 = I \quad (\text{involutory}).
> $$

> [!thm] Sparsifying a vector with a reflector
> 
> Let $x \in \mathbb{R}^n$, $x \neq 0$, and let $e_1$ be the first standard basis vector. Set
> $$
> v \;=\; x \pm \|x\|\, e_1, 
> \qquad R \;=\; I - \frac{2 v v^\top}{v^\top v}.
> $$
> Then
> $$
> R x \;=\; \pm \|x\|\, e_1 \;=\; \pm \begin{bmatrix} \|x\| \\ 0 \\ \vdots \\ 0 \end{bmatrix}.
> $$

---

## Rotators (Givens/Plane Rotations)

> [!def] Planar rotator in R²
> 
> $$
> P(\theta) \;=\; 
> \begin{bmatrix}
> \cos\theta & -\sin\theta \\
> \sin\theta & \cos\theta
> \end{bmatrix},
> \qquad
> P(\theta)^\top = P(-\theta),
> \qquad
> P(\theta)^\top P(\theta) = I.
> $$

> [!def] Plane rotator $P_{i,j}$ in $\mathbb{R}^n$
> 
> For indices $1 \le i < j \le n$, define $P_{i,j}$ to be the identity matrix except on rows/columns $i$ and $j$, where it contains the $2\times 2$ block
> $$
> \begin{bmatrix}
> c & -s \\
> s & \phantom{-}c
> \end{bmatrix},
> \qquad c^2 + s^2 = 1.
> $$
> Then $P_{i,j}$ rotates in the $(i,j)$-plane and satisfies $P_{i,j}^\top P_{i,j} = I$.

Choosing $c,s$ to zero an entry:
- If $(x_i,x_j)\neq (0,0)$, set
  $$
  c \;=\; \frac{x_i}{\sqrt{x_i^2 + x_j^2}},
  \qquad
  s \;=\; \frac{x_j}{\sqrt{x_i^2 + x_j^2}}.
  $$

> [!thm] Zeroing a component with a plane rotation
> 
> With $c,s$ as above,
> $$
> x' \;=\; P_{i,j}\,x 
> \quad\Rightarrow\quad
> x'_i = \sqrt{x_i^2 + x_j^2}, \;\; x'_j = 0,
> $$
> and all other components are unchanged.

Sequential construction to concentrate the norm in the first entry:
$$
\begin{aligned}
P_{1,2}x &= \begin{bmatrix} \sqrt{x_1^2+x_2^2} \\ 0 \\ x_3 \\ \vdots \end{bmatrix}, \\
P_{1,3} P_{1,2}x &= \begin{bmatrix} \sqrt{x_1^2+x_2^2+x_3^2} \\ 0 \\ 0 \\ x_4 \\ \vdots \end{bmatrix}, \\
\cdots\quad
P_{1,n}\cdots P_{1,2}x &= \begin{bmatrix} \|x\| \\ 0 \\ \vdots \\ 0 \end{bmatrix}.
\end{aligned}
$$

> [!imp] Practical note
> 
> For dense matrices, reflectors (Householder) are typically preferred over rotators (Givens) for efficiency; rotators are often used when preserving sparsity or targeting a single entry is advantageous.

---

## Householder Reduction (QR Factorization)

Let
$$
A \in \mathbb{R}^{m\times n} = \begin{bmatrix} a_1 & a_2 & \cdots & a_n \end{bmatrix}.
$$

Goal: construct orthogonal $Q$ and upper-triangular (or upper-trapezoidal) $R$ such that $A = Q R$.

Algorithm (using Householder reflectors):
1) First column
- Set $x := a_1$ and form
  $$
  v_1 = x \pm \|x\|\, e_1, 
  \qquad
  R_1 = I - \frac{2 v_1 v_1^\top}{v_1^\top v_1}.
  $$
- Then
  $$
  A^{(1)} := R_1 A 
  = 
  \begin{bmatrix}
  r_{11} & r_{12} & \cdots & r_{1n} \\
  0      &        &        &        \\
  \vdots &        & A_2    &        \\
  0      &        &        &        
  \end{bmatrix}.
  $$

2) Trailing submatrix
- Apply the same idea to the $(m-1)\times (n-1)$ trailing submatrix $A_2$:
  construct $R_2 = \mathrm{diag}(1, \tilde R_2)$ so that
  $$
  A^{(2)} := R_2 A^{(1)} 
  =
  \begin{bmatrix}
  r_{11} & r_{12} & \cdots & r_{1n} \\
  0      & r_{22} & \cdots & r_{2n} \\
  \vdots & 0      & \ddots & \vdots \\
  0      & \vdots & \ddots & r_{kn}
  \end{bmatrix},
  $$
  with zeros introduced below the diagonal in the second column.

3) Iterate
- Continue for $k = \min(m,n)$ steps:
  $$
  A^{(k)} := R_k \cdots R_2 R_1 A =: T,
  $$
  where $T$ is upper-triangular (if $m \ge n$) or upper-trapezoidal.

4) Assemble $Q$ and $R$
- Let
  $$
  H := R_k \cdots R_2 R_1 \quad\Rightarrow\quad H \text{ is orthogonal},\; T = H A.
  $$
- Set
  $$
  Q := H^\top, 
  \qquad R := T,
  \qquad\text{so that}\qquad A = Q R.
  $$

Notes:
- Each $R_i$ is a Householder reflector: symmetric, orthogonal, and involutory.
- The product of reflectors is orthogonal, ensuring numerical stability and efficiency for dense QR.
