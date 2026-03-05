# Classical Gram–Schmidt (CGS) — Algorithm

*Original Note: [[L07 - Gram–Schmidt Algorithm]]*

- Input: Linearly independent vectors x_1, ..., x_n ∈ R^m.
- For k = 1 to n:
  - v_k ← x_k
  - For i = 1 to k−1:
    - r_{ik} ← u_i^T x_k  (CGS as originally written) 
  - v_k ← x_k − ∑_{i=1}^{k−1} r_{ik} u_i
  - r_{kk} ← ∥v_k∥
  - u_k ← v_k / r_{kk}

> [!imp] Numerical Stability
> Classical Gram–Schmidt can suffer loss of orthogonality in finite-precision arithmetic. Modified Gram–Schmidt (MGS) is more stable.

---
