# Gram–Schmidt Algorithm

*Original Note: [[L07]]*

Use case: Gram–Schmidt is particularly useful for QR factorization.

Objective: Given a linearly independent set of vectors B = {x_1, x_2, ..., x_n} in an inner-product space (e.g., R^m with ⟨y, z⟩ = y^T z), construct an orthonormal set U = {u_1, u_2, ..., u_n} such that Span(U) = Span(B).

Notation: Norm is denoted by ∥·∥, inner product by ⟨·, ·⟩.

> [!def] Orthogonal Projection (Fourier Expansion)
> If {u_1, ..., u_k} is an orthonormal set, then for any x,
> $$\operatorname{proj}_{\operatorname{span}\{u_1,\dots,u_k\}}(x) = \sum_{i=1}^k \langle u_i, x \rangle u_i.$$

---

## Classical Gram–Schmidt (CGS): Inductive Construction

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

## Matrix Notation and Projectors

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

## Classical Gram–Schmidt (CGS) — Algorithm

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
# Extractions -------------
# Gram–Schmidt Algorithm

*Original Note: [[L07]]*

Use case: Gram–Schmidt is particularly useful for QR factorization.

Objective: Given a linearly independent set of vectors B = {x_1, x_2, ..., x_n} in an inner-product space (e.g., R^m with ⟨y, z⟩ = y^T z), construct an orthonormal set U = {u_1, u_2, ..., u_n} such that Span(U) = Span(B).

Notation: Norm is denoted by ∥·∥, inner product by ⟨·, ·⟩.

> [!def] Orthogonal Projection (Fourier Expansion)
> If {u_1, ..., u_k} is an orthonormal set, then for any x,
> $$\operatorname{proj}_{\operatorname{span}\{u_1,\dots,u_k\}}(x) = \sum_{i=1}^k \langle u_i, x \rangle u_i.$$

---

## Classical Gram–Schmidt (CGS): Inductive Construction

*Extracted to: [[L07 - Gram–Schmidt Algorithm - Classical Gram–Schmidt (CGS) Inductive Construction]]*

## Matrix Notation and Projectors

*Extracted to: [[L07 - Gram–Schmidt Algorithm - Matrix Notation and Projectors]]*

## Classical Gram–Schmidt (CGS) — Algorithm

*Extracted to: [[L07 - Gram–Schmidt Algorithm - Classical Gram–Schmidt (CGS) — Algorithm]]*

