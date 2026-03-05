# Matrix–Vector Multiplication

*Original Note: [[L02]]*

> [!def] Matrix–Vector Multiplication (row-by-column)
> Let $A \in \mathbb{R}^{m \times n}$ and $x \in \mathbb{R}^n$. The product $y = Ax \in \mathbb{R}^m$ is defined componentwise by
> $$
> y_i = \sum_{j=1}^n a_{ij} x_j, \quad i=1,\dots,m.
> $$
> Example (symbolic, then numeric):
> $$
> A=\begin{bmatrix}2 & 5 \\[2pt] 3 & 7\end{bmatrix},\quad
> x=\begin{bmatrix}v_1\\ v_2\end{bmatrix}
> \;\Rightarrow\;
> Ax=\begin{bmatrix}2v_1+5v_2 \\[2pt] 3v_1+7v_2\end{bmatrix}.
> $$
> If $x=[1\; 1]^T$, then $Ax=\begin{bmatrix}7\\ 10\end{bmatrix}$.

> [!def] Column-combination view (columns of A)
> If $A=\begin{bmatrix} \vec a_1 & \cdots & \vec a_n \end{bmatrix}$, then
> $$
> Ax = x_1\vec a_1 + x_2\vec a_2 + \cdots + x_n\vec a_n.
> $$
> For
> $
> A=\begin{bmatrix}2 & 5 \\[2pt] 3 & 7\end{bmatrix}
> $
> and
> $
> x=\begin{bmatrix}v_1\\ v_2\end{bmatrix},
> $
> this gives
> $$
> Ax = v_1\begin{bmatrix}2\\[2pt]3\end{bmatrix} + v_2\begin{bmatrix}5\\[2pt]7\end{bmatrix}.
> $$

> [!imp] Dimensions must match
> To form $Ax$, the number of columns of $A$ must equal the number of entries of $x$ (i.e., $A\in\mathbb{R}^{m\times n}$ and $x\in\mathbb{R}^n$). The result has the same number of rows as $A$ (i.e., $Ax\in\mathbb{R}^m$).
