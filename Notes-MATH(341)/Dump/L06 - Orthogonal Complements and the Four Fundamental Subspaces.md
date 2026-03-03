# Orthogonal Complements and the Four Fundamental Subspaces

*Original Note: [L06](../s01/L06.md)*

Let A ∈ R^{m×n}. We use the standard Euclidean inner product ⟨u, v⟩ = u^T v.

> [!thm] Orthogonality of Fundamental Subspaces
> For A ∈ R^{m×n} with rank r:
> - R(A)⊥ = N(A^T) and R(A^T)⊥ = N(A).
> - R^n = N(A) ⊕ R(A^T) and R^m = R(A) ⊕ N(A^T).
> - Dimensions:
>   - dim R(A) = r, dim R(A^T) = r
>   - dim N(A) = n − r, dim N(A^T) = m − r

> [!pf] Proof
> Take x ∈ R(A)⊥. Then for all y ∈ R^n,
> $$0 = \langle x, Ay \rangle = (Ay)^T x = y^T A^T x = \langle y, A^T x \rangle.$$
> Since this holds for all y, we get A^T x = 0, so x ∈ N(A^T). Thus R(A)⊥ = N(A^T).
> The relation R(A^T)⊥ = N(A) follows by applying the same argument to A^T.

Direct sum decompositions follow from V = W ⊕ W⊥ in inner-product spaces applied to the pairs (R(A), N(A^T)) in R^m and (R(A^T), N(A)) in R^n, together with the dimension identities.

- Nullity reminder: dim N(A) = number of free variables = n − r.
