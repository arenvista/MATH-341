# Orthonormal Bases and Fourier Expansion

*Original Note: [[L06]]*

> [!def] Orthonormal Basis
> A set $B = \{u_1,\dots,u_n\}$ in an inner product space is an orthonormal basis if
> $$\langle u_i, u_j\rangle = \delta_{ij}, \quad \|u_i\| = 1,$$
> and it spans the space.

- Kronecker delta:
  $$
  \langle u_i, u_j\rangle = u_i^T u_j = \delta_{ij}, \quad
  \delta_{ij} = \begin{cases}
  1, & i=j,\\
  0, & i\ne j.
  \end{cases}
  $$

> [!def] Fourier Expansion of a Vector
> If $B = \{u_1,\dots,u_n\}$ is an orthonormal basis of $\mathbb{R}^n$, then for any $x \in \mathbb{R}^n$,
> $$x = \sum_{i=1}^n \langle u_i, x\rangle\, u_i.$$

> [!def] Fourier Coefficients
> The scalars $\langle u_i, x\rangle$ are the Fourier coefficients of $x$ with respect to the orthonormal basis $B$. Each coefficient equals the orthogonal projection of $x$ onto the one-dimensional subspace $\operatorname{span}\{u_i\}$, scaled by $u_i$:
> $$\operatorname{proj}_{\operatorname{span}\{u_i\}}(x) = \langle u_i, x\rangle\, u_i.$$

> [!pf] Why the Expansion Holds
> Because the $u_i$ form a basis, $x = \sum_i \alpha_i u_i$ for unique $\alpha_i$. Taking inner products with $u_j$ and using orthonormality:
> $$\langle u_j, x\rangle = \left\langle u_j, \sum_i \alpha_i u_i \right\rangle = \sum_i \alpha_i \langle u_j, u_i\rangle = \alpha_j.$$
> Hence $\alpha_j = \langle u_j, x\rangle$ and the formula follows.
