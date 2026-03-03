# Orthogonal Projectors

*Original Note: [L06](../s01/L06.md)*

> [!def] Orthogonal Projector onto a Line
> Let u ∈ R^n be nonzero. The orthogonal projector onto Span(u) is
> $$
> P_u = \frac{u u^T}{u^T u}.
> $$
> If u is unit-norm, then P_u = u u^T.
> For any x ∈ R^n,
> $$
> P_u x = \frac{u u^T}{u^T u} x = \frac{\langle u, x \rangle}{\langle u, u \rangle}\, u,
> $$
> which is the orthogonal projection of x onto Span(u).
