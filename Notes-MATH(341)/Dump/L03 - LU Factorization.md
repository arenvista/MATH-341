# LU Factorization

*Original Note: [L03](../s01/L03.md)*

## Overview and Goal

> [!def] LU Factorization
> Goal: Solve a linear system $Ax=b$ efficiently by Gaussian elimination and re-use the work for multiple right-hand sides $b$.
>
> Idea: Use row operations to transform the augmented system $[A\,|\,b] \to [U\,|\,y]$ so that
> $$
> \left.
> \begin{array}{l}
> Ax=b \\
> Ux=y
> \end{array}
> \right\}\ \text{share the same solution }x.
> $$
> When the elimination can proceed without row swaps, $A$ factors as $A=LU$ with $L$ unit lower triangular and $U$ upper triangular.

> [!def] Leading principal submatrix
> The $k\times k$ leading principal submatrix of $A\in\mathbb{R}^{n\times n}$ is the submatrix formed by the first $k$ rows and first $k$ columns of $A$.

> [!thm] Existence (no pivoting)
> If $A\in\mathbb{R}^{n\times n}$ is nonsingular and all leading principal submatrices of $A$ are nonsingular, then $A$ admits an LU factorization with $L$ unit lower triangular and $U$ upper triangular (no row swaps required).


## Elimination Matrices and the $LU$ Product

Visualizing elimination by stages (x = arbitrary entry, o = eliminated to zero):
$$
\begin{aligned}
&\begin{bmatrix}
x&x&x&x\\
x&x&x&x\\
x&x&x&x\\
x&x&x&x
\end{bmatrix}\xrightarrow{L_1}
\begin{bmatrix}
x&x&x&x\\
o&x&x&x\\
o&x&x&x\\
o&x&x&x
\end{bmatrix}\xrightarrow{L_2}
\begin{bmatrix}
x&x&x&x\\
o&x&x&x\\
o&o&x&x\\
o&o&x&x
\end{bmatrix}\xrightarrow{L_3}
\begin{bmatrix}
x&x&x&x\\
o&x&x&x\\
o&o&x&x\\
o&o&o&x
\end{bmatrix} \\
&\qquad A\quad\ \ \ L_1A\quad\ \ \ L_2L_1A\qquad L_3L_2L_1A=U
\end{aligned}
$$

- Each $L_i$ is a unit lower triangular (and hence invertible) elimination matrix implementing one elimination stage.
- Therefore,
  $$
  U=L_{n-1}\cdots L_2L_1A
  \quad\Longrightarrow\quad
  A=L^{-1}U\ \ \text{with}\ \ L^{-1}=L_{n-1}\cdots L_2L_1.
  $$
  Equivalently,
  $$
  A=LU
  \quad\text{with}\quad
  L=L_1^{-1}L_2^{-1}\cdots L_{n-1}^{-1}.
  $$

> [!cor] Inverses of one-step elimination matrices
> If $E$ is a one-step unit lower triangular elimination matrix (it differs from $I$ only in a single column below the diagonal), then $E^{-1}$ is obtained by flipping the signs of those subdiagonal entries in that column.
> This sign-flip rule holds for individual elimination matrices $L_i$, not for an arbitrary lower triangular matrix.


## Example 1: Computing $LU$ Without Pivoting

> [!pf] Example 1: Factor $A=LU$
> $$
> A=
> \begin{bmatrix}
> 2&1&1&0\\
> 4&3&3&1\\
> 8&7&9&5\\
> 6&7&9&5
> \end{bmatrix}
> $$
> Stage 1 (eliminate below $a_{11}$):
> $$
> L_1=
> \begin{bmatrix}
> 1&0&0&0\\
> -2&1&0&0\\
> -4&0&1&0\\
> -3&0&0&1
> \end{bmatrix},\quad
> L_1A=
> \begin{bmatrix}
> 2&1&1&0\\
> 0&1&1&1\\
> 0&3&5&5\\
> 0&4&6&5
> \end{bmatrix}.
> $$
> Stage 2 (eliminate below $a_{22}$):
> $$
> L_2=
> \begin{bmatrix}
> 1&0&0&0\\
> 0&1&0&0\\
> 0&-3&1&0\\
> 0&-4&0&1
> \end{bmatrix},\quad
> L_2L_1A=
> \begin{bmatrix}
> 2&1&1&0\\
> 0&1&1&1\\
> 0&0&2&2\\
> 0&0&2&1
> \end{bmatrix}.
> $$
> Stage 3 (eliminate below $a_{33}$):
> $$
> L_3=
> \begin{bmatrix}
> 1&0&0&0\\
> 0&1&0&0\\
> 0&0&1&0\\
> 0&0&-1&1
> \end{bmatrix},\quad
> U=L_3L_2L_1A=
> \begin{bmatrix}
> 2&1&1&0\\
> 0&1&1&1\\
> 0&0&2&2\\
> 0&0&0&-1
> \end{bmatrix}.
> $$
> Recover $L=L_1^{-1}L_2^{-1}L_3^{-1}$ using the sign-flip rule for each $L_i$:
> $$
> L=
> \begin{bmatrix}
> 1&0&0&0\\
> 2&1&0&0\\
> 4&3&1&0\\
> 3&4&1&1
> \end{bmatrix}.
> $$
> Check: $LU=A$ (multiplying confirms the original $A$).


## Example 2: Why Pivoting May Be Necessary

> [!pf] Example 2: Attempting $A=LU$ fails without pivoting
> Suppose
> $$
> A=\begin{bmatrix}0&1\\[2pt]1&1\end{bmatrix},\quad
> L=\begin{bmatrix}1&0\\[2pt]a&1\end{bmatrix},\quad
> U=\begin{bmatrix}b&c\\[2pt]0&d\end{bmatrix}.
> $$
> Matching entries in $LU=A$:
> - $(1,1)$: $b=0$.
> - $(2,1)$: $ab=1$.
> This is a contradiction, so $A$ has no $LU$ with $L$ unit lower triangular unless we first swap rows (pivot).

Row swapping via a permutation matrix resolves this.

> [!def] Permutation matrices
> A permutation matrix $P$ is obtained by permuting the rows of the identity: each row and each column contains exactly one entry equal to $1$ and zeros elsewhere.
> - Left multiplication by $P$ permutes rows: $PA$.
> - Right multiplication by $P$ permutes columns: $AP$.

Example (a 4×4 row-permutation that maps rows $3\to 1$, $2\to 2$, $4\to 3$, $1\to 4$):
$$
P_1=
\begin{bmatrix}
0&0&1&0\\
0&1&0&0\\
0&0&0&1\\
1&0&0&0
\end{bmatrix}.
$$

> [!cor] Inverse and transpose
> For any permutation matrix $P$, $P^{-1}=P^T$ and $PP^T=I$.

Returning to Example 2:
$$
P=\begin{bmatrix}0&1\\[2pt]1&0\end{bmatrix},\quad
PA=\begin{bmatrix}1&1\\[2pt]0&1\end{bmatrix}=LU
\quad\text{with}\quad
L=I,\ \ U=\begin{bmatrix}1&1\\[2pt]0&1\end{bmatrix}.
$$
Thus $PA=LU$ exists even though $A\neq LU$ without pivoting.


## Partial Pivoting

> [!def] Partial Pivoting
> At elimination step $k$, search column $k$ among rows $k,k{+}1,\dots,n$ for the entry of largest magnitude and swap that row with row $k$. This chooses a large-magnitude pivot $a_{kk}$ and improves numerical stability by reducing growth in rounding errors.
>
> In practice we compute
> $$
> PA=LU,
> $$
> where $P$ encodes the sequence of row swaps selected by partial pivoting.

Solving $Ax=b$ with partial pivoting:
1. Compute $PA=LU$.
2. Solve $Ly=Pb$ by forward substitution.
3. Solve $Ux=y$ by back substitution.

This yields the same solution $x$ as $Ax=b$ because $P$ only permutes equations.
