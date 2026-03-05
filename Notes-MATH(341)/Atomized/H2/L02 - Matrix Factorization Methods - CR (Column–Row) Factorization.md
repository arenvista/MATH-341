# CR (Column–Row) Factorization

*Original Note: [[L02 - Matrix Factorization Methods]]*

> [!def] CR factorization (selecting independent columns)
> Let $A\in\mathbb{R}^{m\times n}$ have rank $r$. Choose $C\in\mathbb{R}^{m\times r}$ to be any matrix formed by $r$ linearly independent columns of $A$ (pivot columns). Then there exists $R\in\mathbb{R}^{r\times n}$ such that
> $$
> A = C R,
> $$
> where each column of $R$ gives the coefficients expressing the corresponding column of $A$ as a linear combination of the columns in $C$.
> 
> Notes:
> - Shapes: $A$ is $m\times n$, $C$ is $m\times r$, $R$ is $r\times n$.
> - If $C$ has full column rank, one convenient formula is $R = C^{\dagger} A = (C^T C)^{-1} C^T A$.
> - The choice of independent columns is not unique; different choices yield different $(C,R)$ with the same product.

> [!pf] Worked example (CR factorization)
> $$
> A=\begin{bmatrix}
> 1 & 2 & 4\\[2pt]
> 1 & 3 & 5
> \end{bmatrix}
> =
> \underbrace{\begin{bmatrix}
> 1 & 2\\[2pt]
> 1 & 3
> \end{bmatrix}}_{C=[\vec a_1\;\vec a_2]}
> \underbrace{\begin{bmatrix}
> 1 & 0 & 2\\[2pt]
> 0 & 1 & 1
> \end{bmatrix}}_{R}
> $$
> Check: $\vec a_3=\begin{bmatrix}4\\[2pt]5\end{bmatrix}=2\vec a_1+\vec a_2$, so the third column of $R$ is $\begin{bmatrix}2\\[2pt]1\end{bmatrix}$.

> [!pf] Worked example (rank-one as an outer product)
> $$
> A=\begin{bmatrix}2 & 4 & 6\\[2pt] 3 & 6 & 9\end{bmatrix}
> =
> \underbrace{\begin{bmatrix}2\\[2pt]3\end{bmatrix}}_{u}
> \underbrace{\begin{bmatrix}1 & 2 & 3\end{bmatrix}}_{v^T},
> $$
> so $\operatorname{rank}(A)=1$ and $A=uv^T$ is already a CR factorization with $C=u$ and $R=v^T$.
