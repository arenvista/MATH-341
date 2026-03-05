# Classical Gram–Schmidt (CGS): Inductive Construction

*Original Note: [[L07 - Gram–Schmidt Algorithm]]*

Base case:
$$
u_1 = \frac{x_1}{\|x_1\|}.
$$

Inductive step: Suppose u_1, ..., u_{k-1} are orthonormal and Span{u_1, ..., u_{k-1}} = Span{x_1, ..., x_{k-1}}. Define
$$
v_k = x_k - \sum_{i=1}^{k-1} \langle u_i, x_k \rangle u_i, 
\qquad
u_k = \frac{v_k}{\|v_k\|} \quad \text{(assuming } v_k \neq 0\text{)}.
$$

> [!imp] Additional Explanation
> - v_k is x_k with its components along u_1, ..., u_{k-1} removed (orthogonal component).
> - If v_k = 0, then x_k is already in Span{x_1, ..., x_{k-1}} (loss of linear independence).

> [!thm] Gram–Schmidt Orthonormalization
> Given a linearly independent set {x_1, ..., x_n}, the above construction produces an orthonormal set {u_1, ..., u_n} such that Span{u_1, ..., u_k} = Span{x_1, ..., x_k} for each k.
>
> [!pf] Proof Sketch
> - Base case is immediate.
> - Inductive step: v_k is orthogonal to each u_i by construction; normalizing gives u_k with ∥u_k∥ = 1.
> - Span equality holds because x_k = v_k + ∑_{i=1}^{k-1} ⟨u_i, x_k⟩ u_i and v_k ≠ 0 when x_k adds a new direction.

---
