# Projector Viewpoint for MGS

*Original Note: [[L07 - Modified Gram–Schmidt (MGS)]]*

Define the rank-1 orthogonal projector onto the orthogonal complement of u_i by
$$
E_i = I - u_i u_i^T, \quad \text{where } \|u_i\| = 1.
$$
Applying E_i removes the component along u_i. Sequentially,
$$
v_k = \big(E_{k-1} E_{k-2} \cdots E_{1}\big)\, x_k.
$$

> [!lem] Product of Complement Projectors
> If u_1, ..., u_{k-1} are mutually orthonormal, then
> $$
> E_{k-1} E_{k-2} \cdots E_{1} \;=\; I - \sum_{i=1}^{k-1} u_i u_i^T.
> $$
>
> [!pf] Proof
> Expand the product:
> (I − u_j u_j^T)(I − u_i u_i^T) = I − u_i u_i^T − u_j u_j^T + (u_j u_j^T)(u_i u_i^T).
> Since (u_j u_j^T)(u_i u_i^T) = u_j (u_j^T u_i) u_i^T = 0 for i ≠ j, all mixed terms vanish. By induction over k, the result follows.

Thus, with U_{k-1} = [u_1 ... u_{k-1}],
$$
\big(E_{k-1} \cdots E_1\big) = I - U_{k-1} U_{k-1}^T,
\qquad
v_k = (I - U_{k-1} U_{k-1}^T)\, x_k,
\qquad
u_k = \frac{v_k}{\|v_k\|}.
$$

---
