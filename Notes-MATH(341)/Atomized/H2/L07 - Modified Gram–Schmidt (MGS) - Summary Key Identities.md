# Summary: Key Identities

*Original Note: [[L07 - Modified Gram–Schmidt (MGS)]]*

- Projection onto Span{u_1, ..., u_{k-1}}:
  $$
  \operatorname{proj}_{\mathrm{span}}(x_k) = U_{k-1} U_{k-1}^T x_k.
  $$
- Orthogonal component:
  $$
  v_k = (I - U_{k-1} U_{k-1}^T) x_k.
  $$
- Normalization:
  $$
  u_k = \frac{v_k}{\|v_k\|}.
  $$
- QR entries:
  $$
  r_{ik} = q_i^T a_k \quad (i \le k), \qquad r_{kk} = \|v_k\| > 0, \qquad A = Q R.
  $$

> [!imp] Practical Notes
> - Ensure m ≥ n and columns of A are linearly independent for a full-column QR.
> - Enforce r_{kk} > 0 for uniqueness of (Q, R).
> - Prefer MGS (or Householder QR) for better numerical stability in practice.
