# Orthonormal Bases and Fourier Expansion

*Original Note: [L06](../s01/L06.md)*

> [!def] Orthonormal Basis
> A set B = {u_1, …, u_n} ⊆ R^n is an orthonormal basis if
> $$u_i \perp u_j \ (i \ne j), \quad \|u_i\| = 1.$$

> [!def] Fourier Expansion of a Vector ^FourierExpansion
> If {u_1, …, u_n} is an orthonormal basis of R^n, then every x ∈ R^n has the expansion
> $$
> x = \sum_{i=1}^n \langle u_i, x \rangle\, u_i.
> $$

> [!def] Fourier Coefficients and Orthogonal Projections
> - The scalar ⟨u_i, x⟩ is the i-th Fourier coefficient of x.
> - The orthogonal projection of x onto Span(u_i) is the vector ⟨u_i, x⟩ u_i.

Orthogonality conditions for an orthonormal set:
$$
\langle u_i, u_j \rangle = u_i^T u_j = \delta_{ij}, \quad
\delta_{ij} = \begin{cases}
1, & i = j,\\
0, & i \ne j.
\end{cases}
$$
