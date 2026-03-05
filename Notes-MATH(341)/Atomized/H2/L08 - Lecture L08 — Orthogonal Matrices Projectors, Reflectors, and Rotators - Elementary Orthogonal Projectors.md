# Elementary Orthogonal Projectors

*Original Note: [[L08 - Lecture L08 — Orthogonal Matrices Projectors, Reflectors, and Rotators]]*

> [!def] Elementary Orthogonal Projector onto u⊥
> Let $u \in \mathbb{R}^{n}$ with $\|u\|=1$.  
> The orthogonal projector onto the hyperplane $u^\perp$ is
> $$
> Q = I - uu^T.
> $$
> The complementary projector onto $\text{span}\{u\}$ is
> $$
> P_u = I - Q = uu^T.
> $$

Basic decomposition and orthogonality:
$$
x = (I-Q)x + Qx = P_u x + Qx, 
\quad \text{with } P_u x \perp Qx.
$$

Length of the component along $u$:
$$
P_u x = (u^T x)\,u 
\quad\Rightarrow\quad
\|P_u x\| = |u^T x|.
$$

If $u$ is not normalized:
$$
Q = I - \frac{uu^T}{u^T u}, 
\qquad 
P_u = \frac{uu^T}{u^T u}.
$$

> [!pf] Why $P_u x \perp Qx$
> For unit $u$, $P_u=uu^T$ and $Q=I-uu^T$ are symmetric idempotents with $P_u Q=0$. Then
> $$
> \langle P_u x, Qx\rangle 
> = x^T P_u^T Q x
> = x^T P_u Q x
> = x^T 0\, x
> = 0.
> $$

> [!def] Elementary elimination matrix (row update)
> For standard basis vectors $e_i$ and a scalar $\alpha$, the matrix
> $$
> L = I - \alpha\, e_i e_j^T
> $$
> adds $-\alpha$ times row $j$ to row $i$ when left-multiplying a matrix.  
> This is not a projector in general, but it shares the “rank-1 update” form.

> [!?] What if we consider $R = I - 2uu^T$? What does $Rx$ do?
> $R$ is the reflection (Householder reflector) through the hyperplane $u^\perp$:
> $$
> Rx = x - 2(u^T x)\,u.
> $$
> Applying it twice returns the original vector: $R^2=I$.

---
