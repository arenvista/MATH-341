# QR vs LU: Quick Comparison

*Original Note: [[L07 - QR Factorization via Gram–Schmidt]]*

| Topic                                   | QR                                                | LU (without pivoting)                       |
| --------------------------------------- | ------------------------------------------------- | ------------------------------------------- |
| Existence                               | For A with linearly independent columns (m ≥ n)   | For square A; may require pivoting          |
| Shape                                   | A = Q (m×n) R (n×n), R upper triangular           | A = L U, L lower, U upper (square A)        |
| Uniqueness                              | Unique if diag(R) > 0                             | Not unique (depends on pivoting/scaling)    |
| Works for rectangular A                 | Yes (full column rank)                            | No (typically square only)                   |
| Solve Ax = b (square A)                 | One back substitution (R x = Q^T b)               | Forward (L y = b) + back (U x = y)          |
| Least squares (overdetermined)          | Yes (natural via Q^T)                             | Not standard                                |

---
