# Matrix Notation and Projectors

*Original Note: [[L07 - Gram–Schmidt Algorithm]]*

Let U_{k-1} = [u_1 u_2 ... u_{k-1}] ∈ R^{m×(k-1)}. Then:

- Coefficients:
$$
r_{1:(k-1),\,k} = U_{k-1}^T x_k.
$$

- Projection onto Span{u_1, ..., u_{k-1}}:
$$
U_{k-1} (U_{k-1}^T x_k) = \sum_{i=1}^{k-1} \langle u_i, x_k \rangle u_i.
$$

- Orthogonal component and normalization:
$$
v_k = (I - U_{k-1} U_{k-1}^T)\, x_k,
\qquad
u_k = \frac{v_k}{\|v_k\|}.
$$

> [!imp] Additional Explanation
> - U_{k-1} U_{k-1}^T is the orthogonal projector onto Span{u_1, ..., u_{k-1}}.
> - u_i^T x_k is a scalar; u_i (u_i^T x_k) is that scalar times the vector u_i.

---
