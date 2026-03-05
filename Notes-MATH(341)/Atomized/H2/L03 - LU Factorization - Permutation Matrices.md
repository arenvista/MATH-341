# Permutation Matrices

*Original Note: [[L03 - LU Factorization]]*

> [!def] Definition: Permutation Matrices
> A permutation matrix $P$ is obtained by permuting the rows of the identity matrix $I$. Each row and each column contains exactly one entry equal to $1$ and all others $0$.
> 
> - Left multiplication $PA$ permutes the rows of $A$.
> - Right multiplication $AP$ permutes the columns of $A$.

Example (row permutation mapping $[3,2,4,1]$):
$$
P=
\begin{bmatrix}
0&0&1&0\\
0&1&0&0\\
0&0&0&1\\
1&0&0&0
\end{bmatrix},
\quad
PA=
\begin{bmatrix}
\text{row}_3(A)\\
\text{row}_2(A)\\
\text{row}_4(A)\\
\text{row}_1(A)
\end{bmatrix},
\quad
AP=
\begin{bmatrix}
\cdots & \text{col}_3(A) & \cdots & \text{col}_4(A) & \cdots & \text{col}_1(A)
\end{bmatrix}.
$$

> [!cor] Orthogonality of Permutation Matrices
> For any permutation matrix $P$,
> $$P^{-1}=P^{\mathsf T},\qquad PP^{\mathsf T}=P^{\mathsf T}P=I.$$
> 
> Sketch: $(PP^{\mathsf T})_{ij}=\sum_k P_{ik}P_{jk}=\delta_{ij}$ because rows of $P$ are distinct standard basis vectors.

> [!def] Kronecker Delta
> $$\delta_{ij}=
> \begin{cases}
> 1, & i=j,\\
> 0, & i\ne j.
> \end{cases}
> $$
