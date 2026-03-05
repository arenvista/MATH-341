# Column Space — Example

*Original Note: [[L04 - Four Fundamental Subspaces]]*

> [!def] Column Space
> The column space $\mathrm{Col}(A)$ is the span of the columns of $A$. Its dimension is the rank of $A$.

Consider
$$
A =
\begin{bmatrix}
1 & 2 & 1 & 3 & 3 \\
2 & 4 & 0 & 4 & 4 \\
1 & 2 & 3 & 5 & 5 \\
2 & 4 & 0 & 4 & 7
\end{bmatrix}
\;\;\xrightarrow{\ \text{row ops}\ }\;\;
E =
\begin{bmatrix}
1 & 2 & 1 & 3 & 3 \\
0 & 0 & -2 & -2 & -2 \\
0 & 0 & 0 & 0 & 3 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix},
$$
where $E$ is a row echelon form (one possible REF).

- Pivot columns (indices): $\{1, 3, 5\}$.
- Rank:
$$
\mathrm{rank}(A) = \text{number of pivots} = 3.
$$
- Basis for the column space (the pivot columns of $A$):
$$
\mathrm{Basis}(\mathrm{Col}(A)) =
\left\{
\begin{bmatrix} 1 \\ 2 \\ 1 \\ 2 \end{bmatrix},
\begin{bmatrix} 1 \\ 0 \\ 3 \\ 0 \end{bmatrix},
\begin{bmatrix} 3 \\ 4 \\ 5 \\ 7 \end{bmatrix}
\right\}.
$$

> [!imp] Key equivalences
> $$
> \mathrm{rank}(A)
> = \text{number of pivots}
> = \dim(\mathrm{Col}(A))
> = \text{number of nonzero rows in REF}
> = \text{number of basic (pivot) columns of } A.
> $$
