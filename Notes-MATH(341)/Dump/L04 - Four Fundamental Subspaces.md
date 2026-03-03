# Four Fundamental Subspaces

*Original Note: [L04](../s01/L04.md)*

## Column Space: Example and Rank

Consider
$$
A =
\begin{bmatrix}
1 & 2 & 1 & 3 & 3 \\
2 & 4 & 0 & 4 & 4 \\
1 & 2 & 3 & 5 & 5 \\
2 & 4 & 0 & 4 & 7
\end{bmatrix}
\ \xrightarrow{\ \text{row operations}\ }\
E =
\begin{bmatrix}
1 & 2 & 1  & 3  & 3 \\
0 & 0 & -2 & -2 & -2 \\
0 & 0 & 0  & 0  & -3 \\
0 & 0 & 0  & 0  & 0
\end{bmatrix}.
$$

- Pivot columns (from $E$): columns $1, 3, 5$.
- Therefore, $\operatorname{rank}(A) = 3$.

> [!thm] Pivot-Column Basis
> The pivot columns of the original matrix $A$ (corresponding to pivot columns in an echelon form of $A$) form a basis for $\operatorname{Col}(A)$.

> [!cor] Rank Equivalences
> For any matrix $A$,
> - $\operatorname{rank}(A)$ = number of pivots,
> - = number of basis vectors of $\operatorname{Col}(A)$,
> - = number of nonzero rows in any echelon form of $A$,
> - = number of basic (pivot) columns of $A$.

Basis for the column space:
$$
\text{Basis}(\operatorname{Col}(A)) =
\left\{
\begin{bmatrix} 1 \\ 2 \\ 1 \\ 2 \end{bmatrix},
\begin{bmatrix} 1 \\ 0 \\ 3 \\ 0 \end{bmatrix},
\begin{bmatrix} 3 \\ 4 \\ 5 \\ 7 \end{bmatrix}
\right\}.
$$

> [!imp] Reminder
> Always take basis vectors for $\operatorname{Col}(A)$ from the original matrix $A$, not from its echelon form.
