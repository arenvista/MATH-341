# Matrix–Matrix Multiplication

*Original Note: [[L02]]*

> [!def] Matrix–Matrix Multiplication (entrywise/inner-product formula)
> Let $A\in\mathbb{R}^{m\times p}$ and $B\in\mathbb{R}^{p\times n}$. Their product $C=AB\in\mathbb{R}^{m\times n}$ has entries
> $$
> c_{ij} \;=\; \sum_{k=1}^{p} a_{ik}\,b_{kj}, \quad i=1,\dots,m,\;\; j=1,\dots,n.
> $$
> Equivalently: each $c_{ij}$ is the inner product of row $i$ of $A$ with column $j$ of $B$.

> [!pf] Worked example (inner-product computation)
> $$
> \begin{bmatrix}
> 1 & 2\\[2pt]
> 3 & 4
> \end{bmatrix}
> \begin{bmatrix}
> 5 & 7\\[2pt]
> 6 & 8
> \end{bmatrix}
> =
> \begin{bmatrix}
> 1\cdot 5 + 2\cdot 6 & 1\cdot 7 + 2\cdot 8\\[2pt]
> 3\cdot 5 + 4\cdot 6 & 3\cdot 7 + 4\cdot 8
> \end{bmatrix}
> =
> \begin{bmatrix}
> 17 & 23\\[2pt]
> 39 & 53
> \end{bmatrix}.
> $$

> [!def] Outer-product expansion
> The same product can be expressed as a sum of rank-one outer products:
> $$
> AB \;=\; \sum_{k=1}^{p} \big(A_{:,k}\big)\,\big(B_{k,:}\big),
> $$
> where $A_{:,k}$ is the $k$-th column of $A$ and $B_{k,:}$ is the $k$-th row of $B$.
> 
> Worked example (same matrices as above):
> $$
> \underbrace{\begin{bmatrix}1\\[2pt]3\end{bmatrix}\begin{bmatrix}5 & 7\end{bmatrix}}_{\displaystyle C_1=
> \begin{bmatrix}5 & 7\\[2pt]15 & 21\end{bmatrix}}
> \;+\;
> \underbrace{\begin{bmatrix}2\\[2pt]4\end{bmatrix}\begin{bmatrix}6 & 8\end{bmatrix}}_{\displaystyle C_2=
> \begin{bmatrix}12 & 16\\[2pt]24 & 32\end{bmatrix}}
> \;=\;
> \begin{bmatrix}17 & 23\\[2pt]39 & 53\end{bmatrix}.
> $$

> [!cor] Rank-one decompositions and rank
> - A matrix has rank one if and only if it can be written as an outer product $uv^T$ with nonzero vectors $u,v$.
> - Any matrix of rank $r$ can be written as a sum of $r$ rank-one matrices. Moreover, $r$ is the smallest number of rank-one terms needed.
