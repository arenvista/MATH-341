# Modified Gram–Schmidt (MGS)

*Original Note: [[L07]]*

MGS improves numerical stability by orthogonalizing step-by-step against updated residuals.

Algorithm:
- For k = 1 to n:
  - v_k ← a_k
  - For i = 1 to k−1:
    - r_{ik} ← q_i^T v_k
    - v_k ← v_k − r_{ik} q_i
  - r_{kk} ← ∥v_k∥
  - q_k ← v_k / r_{kk}

> [!imp] Additional Explanation
> - In MGS, each subtraction uses the current residual v_k, which reduces round-off error accumulation compared to CGS.

---

## Projector Viewpoint for MGS

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

## Summary: Key Identities

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
# Extractions -------------
# Modified Gram–Schmidt (MGS)

*Original Note: [[L07]]*

MGS improves numerical stability by orthogonalizing step-by-step against updated residuals.

Algorithm:
- For k = 1 to n:
  - v_k ← a_k
  - For i = 1 to k−1:
    - r_{ik} ← q_i^T v_k
    - v_k ← v_k − r_{ik} q_i
  - r_{kk} ← ∥v_k∥
  - q_k ← v_k / r_{kk}

> [!imp] Additional Explanation
> - In MGS, each subtraction uses the current residual v_k, which reduces round-off error accumulation compared to CGS.

---

## Projector Viewpoint for MGS

*Extracted to: [[L07 - Modified Gram–Schmidt (MGS) - Projector Viewpoint for MGS]]*

## Summary: Key Identities

*Extracted to: [[L07 - Modified Gram–Schmidt (MGS) - Summary Key Identities]]*

