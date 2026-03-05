# From Elimination to LU

*Original Note: [[L03 - LU Factorization]]*

> [!lem] Elimination Matrices and the LU Product
> One step of Gaussian elimination (eliminating entries below the pivot in column $k$) is achieved by left-multiplication with a unit lower triangular elimination matrix $L_k$:
> $$L_k = I - \sum_{i=k+1}^n m_{ik}\,e_{ik} \quad\text{where } m_{ik}=\frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}.$$
> After $n-1$ steps,
> $$L_{n-1}\cdots L_2L_1\,A = U.$$
> Since each $L_k$ is nonsingular and unit lower triangular, so is
> $$L:=L_1^{-1}L_2^{-1}\cdots L_{n-1}^{-1},$$
> and hence
> $$A = L\,U.$$
> 
> Key fact (used in practice): For an elimination matrix $L_k = I - m\,e_{ik}$, its inverse is $L_k^{-1}=I + m\,e_{ik}$ (i.e., change the sign of the subdiagonal multipliers for that single step).


> [!thm] Existence (No Pivoting)
> If all leading principal minors of $A$ are nonzero (equivalently: all leading principal submatrices are nonsingular), then $A$ admits an LU factorization without pivoting:
> $$A=LU,$$
> where $L$ is unit lower triangular and $U$ is upper triangular.


### Visualizing Elimination
At each step, entries below the diagonal in one column are zeroed:

$$
\begin{aligned}
&\begin{bmatrix}
x & x & x & x\\
x & x & x & x\\
x & x & x & x\\
x & x & x & x
\end{bmatrix}
\xrightarrow{L_1}
\begin{bmatrix}
x & x & x & x\\
0 & x & x & x\\
0 & x & x & x\\
0 & x & x & x
\end{bmatrix}
\xrightarrow{L_2}
\begin{bmatrix}
x & x & x & x\\
0 & x & x & x\\
0 & 0 & x & x\\
0 & 0 & x & x
\end{bmatrix}
\xrightarrow{L_3}
\begin{bmatrix}
x & x & x & x\\
0 & x & x & x\\
0 & 0 & x & x\\
0 & 0 & 0 & x
\end{bmatrix} \\
&A \quad\ \ \ \ \ \ L_1A \qquad\ \ \ \ \ L_2L_1A \qquad\ \ \ \ \ L_3L_2L_1A=U
\end{aligned}
$$

Because $L_k$ are invertible, we may write
$$A=L_1^{-1}L_2^{-1}\cdots L_{n-1}^{-1}\,U=:LU.$$
