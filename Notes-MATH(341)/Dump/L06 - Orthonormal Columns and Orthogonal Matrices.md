# Orthonormal Columns and Orthogonal Matrices

*Original Note: [L06](../s01/L06.md)*

Let Q = [u_1, u_2, …, u_n] collect vectors u_i as columns.

If the columns are orthonormal, then
$$
Q^T Q =
\begin{bmatrix}
u_1^T\\
u_2^T\\
\vdots\\
u_n^T
\end{bmatrix}
\begin{bmatrix}
u_1 & u_2 & \cdots & u_n
\end{bmatrix} = I.
$$

> [!cor] Nomenclature and Basic Facts
> - Rectangular Q with orthonormal columns: Q^T Q = I (columns form an orthonormal set).
> - Square Q with orthonormal columns (n = m): Q is orthogonal, i.e., Q^T Q = QQ^T = I, hence Q^{-1} = Q^T.

> [!def] Orthogonal Matrices
> A square matrix Q is orthogonal if Q^T Q = I. Equivalently, Q preserves Euclidean norms:
> $$
> \|Qx\|^2 = \langle Qx, Qx \rangle = x^T Q^T Q x = x^T x = \|x\|^2 \quad \text{for all } x.
> $$
> Examples include rotation matrices, reflection matrices, and permutation matrices.
