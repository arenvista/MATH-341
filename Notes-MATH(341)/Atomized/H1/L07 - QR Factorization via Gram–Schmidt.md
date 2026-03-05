# QR Factorization via Gram–Schmidt

*Original Note: [[L07]]*

Let A = [a_1 a_2 ... a_n] ∈ R^{m×n} with m ≥ n and columns linearly independent.

> [!thm] QR Factorization (Full Column Rank)
> There exist Q ∈ R^{m×n} with orthonormal columns (Q^T Q = I_n) and R ∈ R^{n×n} upper triangular with positive diagonal such that
> $$
> A = Q R.
> $$
> The factorization is unique if R has positive diagonal entries.

Construction via Gram–Schmidt:
- Set q_1 = a_1 / ∥a_1∥.
- For k = 2, ..., n:
  - r_{ik} = q_i^T a_k for i = 1, ..., k−1.
  - v_k = a_k − ∑_{i=1}^{k−1} r_{ik} q_i.
  - r_{kk} = ∥v_k∥ > 0.
  - q_k = v_k / r_{kk}.

Matrix form:
$$
A = Q R, \quad
Q = [q_1 \; q_2 \; \cdots \; q_n], \quad
R = \begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n} \\
0      & r_{22} & \cdots & r_{2n} \\
\vdots & \ddots & \ddots & \vdots \\
0      & \cdots & 0      & r_{nn}
\end{bmatrix},
\quad
r_{ij} = q_i^T a_j \text{ for } i \le j.
$$

> [!imp] Additional Explanation
> - For each k, a_k decomposes as
>   $$
>   a_k = \sum_{i=1}^{k} r_{ik} q_i.
>   $$
> - Choosing r_{kk} > 0 ensures uniqueness of Q and R.

---

## Solving Systems with QR

- Square, nonsingular A ∈ R^{n×n}:
  - Ax = b ⇒ QR x = b.
  - Left-multiply by Q^T: R x = Q^T b.
  - Solve the upper-triangular system R x = Q^T b by back substitution.

- Least squares, overdetermined (m ≥ n), full column rank:
  - Minimize ∥Ax − b∥.
  - Since Q has orthonormal columns, ∥Ax − b∥ = ∥Q^T(Ax − b)∥ = ∥R x − Q^T b∥.
  - Solve R x = Q^T b (top n components), again by back substitution.

---

## QR vs LU: Quick Comparison

| Topic                                   | QR                                                | LU (without pivoting)                       |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| Existence                               | For A with linearly independent columns (m ≥ n)   | For square A; may require pivoting          |
| Shape                                   | A = Q (m×n) R (n×n), R upper triangular           | A = L U, L lower, U upper (square A)        |
| Uniqueness                              | Unique if diag(R) > 0                             | Not unique (depends on pivoting/scaling)    |
| Works for rectangular A                 | Yes (full column rank)                            | No (typically square only)                   |
| Solve Ax = b (square A)                 | One back substitution (R x = Q^T b)               | Forward (L y = b) + back (U x = y)          |
| Least squares (overdetermined)          | Yes (natural via Q^T)                             | Not standard                                |

---
# Extractions -------------
# QR Factorization via Gram–Schmidt

*Original Note: [[L07]]*

Let A = [a_1 a_2 ... a_n] ∈ R^{m×n} with m ≥ n and columns linearly independent.

> [!thm] QR Factorization (Full Column Rank)
> There exist Q ∈ R^{m×n} with orthonormal columns (Q^T Q = I_n) and R ∈ R^{n×n} upper triangular with positive diagonal such that
> $$
> A = Q R.
> $$
> The factorization is unique if R has positive diagonal entries.

Construction via Gram–Schmidt:
- Set q_1 = a_1 / ∥a_1∥.
- For k = 2, ..., n:
  - r_{ik} = q_i^T a_k for i = 1, ..., k−1.
  - v_k = a_k − ∑_{i=1}^{k−1} r_{ik} q_i.
  - r_{kk} = ∥v_k∥ > 0.
  - q_k = v_k / r_{kk}.

Matrix form:
$$
A = Q R, \quad
Q = [q_1 \; q_2 \; \cdots \; q_n], \quad
R = \begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n} \\
0      & r_{22} & \cdots & r_{2n} \\
\vdots & \ddots & \ddots & \vdots \\
0      & \cdots & 0      & r_{nn}
\end{bmatrix},
\quad
r_{ij} = q_i^T a_j \text{ for } i \le j.
$$

> [!imp] Additional Explanation
> - For each k, a_k decomposes as
>   $$
>   a_k = \sum_{i=1}^{k} r_{ik} q_i.
>   $$
> - Choosing r_{kk} > 0 ensures uniqueness of Q and R.

---

## Solving Systems with QR

*Extracted to: [[L07 - QR Factorization via Gram–Schmidt - Solving Systems with QR]]*

## QR vs LU: Quick Comparison

*Extracted to: [[L07 - QR Factorization via Gram–Schmidt - QR vs LU Quick Comparison]]*

