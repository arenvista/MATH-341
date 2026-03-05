# Homogeneous Systems

*Original Note: [[L05 - Rectangular Systems — Echelon Form]]*

> [!case] Example — Null space from echelon form
> Consider the (augmented) echelon form of a homogeneous system:
> $$
> \begin{bmatrix}
> \mathbf{1} & 2 & 2 & 3 \;\;|\;\; 0\\
> 0 & 0 & \mathbf{-3} & -3 \;\;|\;\; 0
> \end{bmatrix}
> $$
> Pivot positions are in columns 1 and 3. Let the free variables be $x_2=s$ and $x_4=t$.
> 
> From the second row: $-3x_3-3x_4=0 \Rightarrow x_3=-t$.
> 
> From the first row: $x_1+2x_2+2x_3+3x_4=0 \Rightarrow x_1=-2s-2(-t)-3t=-2s-t$.
> 
> Therefore the solution set (null space) is
> $$
> \mathrm{Nul}(A)
> = \left\{
> \begin{bmatrix} x_1\\x_2\\x_3\\x_4 \end{bmatrix}
> =
> s \begin{bmatrix} -2\\ 1\\ 0\\ 0 \end{bmatrix}
> + t \begin{bmatrix} -1\\ 0\\ -1\\ 1 \end{bmatrix}
> : \; s,t \in \mathbb{R}
> \right\}.
> $$

> [!def] General form of solutions to a homogeneous system
> Let $A\in\mathbb{R}^{m\times n}$ have rank $r$. Then there are $r$ pivot variables and $n-r$ free variables. The general solution to $Ax=0$ can be written as
> $$
> x \;=\; \sum_{i=1}^{n-r} x_{f_i}\,h_i,
> $$
> where each $x_{f_i}$ is a free variable and $\{h_i\}_{i=1}^{n-r}$ are the special solutions (a basis) of $\mathrm{Nul}(A)$ obtained by setting one free variable to $1$ and the others to $0$.
