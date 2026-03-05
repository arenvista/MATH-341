# Orthonormal Columns and Orthogonal Matrices

*Original Note: [[L06]]*

Let $Q = [u_1\, u_2\, \cdots\, u_n]$ collect vectors as columns.

> [!lem] Orthonormal Columns Imply $Q^T Q = I$
> If the columns of $Q \in \mathbb{R}^{m \times n}$ are orthonormal, then
> $$Q^T Q = \begin{bmatrix} u_1^T \\ \vdots \\ u_n^T \end{bmatrix} [\,u_1 \ \cdots \ u_n\,] = I_n.$$

> [!cor] Nomenclature ^Nomenclature
> - If $Q$ is rectangular with orthonormal columns, we say “$Q$ has orthonormal columns” (or “$Q$ is column-orthonormal”).
> - If $Q$ is square and $Q^T Q = I$, we say “$Q$ is an orthogonal matrix.”

> [!def] Orthogonal Matrix
> A square matrix $Q \in \mathbb{R}^{n \times n}$ is orthogonal if and only if $Q^T Q = I$. Equivalently, $Q$ preserves inner products and norms:
> $$\langle Qx, Qy\rangle = \langle x, y\rangle, \quad \|Qx\| = \|x\| \quad \text{for all } x,y.$$
> In particular,
> $$\|Qx\|^2 = \langle Qx, Qx\rangle = x^T Q^T Q x = x^T x = \|x\|^2,$$
> and $Q^{-1} = Q^T$.

- Examples: rotations, reflections, permutation matrices (all preserve lengths and angles).
