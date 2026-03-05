# Spanning Sets from Echelon Form

*Original Note: [[L05 - Four Fundamental Subspaces]]*

> [!cor] Spanning sets/bases of the fundamental subspaces (from REF/RREF)
> - $\mathrm{Col}(A)\equiv R(A)$: pivot columns of the original matrix $A$ (as indicated by pivot columns in the REF/RREF of $A$).
> - $\mathrm{Nul}(A)$: special solutions (“particular solutions” to $Ax=0$) obtained from REF/RREF.
> - $\mathrm{Row}(A)\equiv R(A^\top)$: nonzero (pivot) rows of REF/RREF of $A$.
> - $\mathrm{Nul}(A^\top)$: special solutions to $A^\top y=0$ (left null space).

> [!imp] Important — Which columns span $\mathrm{Col}(A)$?
> Use the pivot column indices found in REF/RREF of $A$ to select the corresponding columns of the original $A$. Those original columns form a basis of $\mathrm{Col}(A)$ (do not use the columns of REF/RREF themselves).

> [!lem] Left null space from row permutations
> Suppose $P$ is a permutation matrix that reorders the rows so that
> $$
> PA=\begin{bmatrix} R\\ 0 \end{bmatrix},
> $$
> where $R\in\mathbb{R}^{r\times n}$ has full row rank $r$ and the bottom block has $m-r$ zero rows. Partition $P=\begin{bmatrix} P_1\\ P_2 \end{bmatrix}$ conformably (so $P_1$ contains the first $r$ rows of $P$). Then
> $$
> \mathrm{Nul}(A^\top)=R(P_2^\top).
> $$

> [!pf] Proof
> Write any $y\in\mathbb{R}^m$ in the permuted coordinates as $y=Pu$ with $u=\begin{bmatrix}u_1\\ u_2\end{bmatrix}$, $u_1\in\mathbb{R}^r$, $u_2\in\mathbb{R}^{m-r}$. Then
> $$
> A^\top y = A^\top P u = \begin{bmatrix} R^\top & 0 \end{bmatrix} u
> = R^\top u_1.
> $$
> Hence $A^\top y=0 \iff u_1=0$, so $u=\begin{bmatrix}0\\ u_2\end{bmatrix}$ is arbitrary in its lower block. Therefore
> $$
> y = P u = P \begin{bmatrix}0\\ u_2\end{bmatrix} = P_2 u_2
> \quad\Longrightarrow\quad
> \mathrm{Nul}(A^\top)=\{P_2 u_2 : u_2\in\mathbb{R}^{m-r}\}=R(P_2).
> $$
> Taking transposes gives $R(P_2)=R(P_2^\top)$ as subspaces of $\mathbb{R}^m$, completing the claim.
