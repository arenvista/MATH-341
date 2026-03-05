# Solving Systems with QR

*Original Note: [[L07 - QR Factorization via Gram–Schmidt]]*

- Square, nonsingular A ∈ R^{n×n}:
  - Ax = b ⇒ QR x = b.
  - Left-multiply by Q^T: R x = Q^T b.
  - Solve the upper-triangular system R x = Q^T b by back substitution.

- Least squares, overdetermined (m ≥ n), full column rank:
  - Minimize ∥Ax − b∥.
  - Since Q has orthonormal columns, ∥Ax − b∥ = ∥Q^T(Ax − b)∥ = ∥R x − Q^T b∥.
  - Solve R x = Q^T b (top n components), again by back substitution.

---
