# 1) Motivating Overdetermined System

*Original Note: [[L09 - Least Squares]]*

$$
\begin{bmatrix}
1 & 1 \\
1 & -1 \\
1 & 1
\end{bmatrix}
\begin{bmatrix}
x_1 \\ x_2
\end{bmatrix}
=
\begin{bmatrix}
2 \\ 1 \\ 3
\end{bmatrix}
\quad\Longleftrightarrow\quad
x_1 \begin{bmatrix}1\\1\\1\end{bmatrix}
+
x_2 \begin{bmatrix}1\\-1\\1\end{bmatrix}
=
\begin{bmatrix}2\\1\\3\end{bmatrix}.
$$

- The columns of $A$ (call them $v_1, v_2$) span a plane in $\mathbb{R}^3$.
- If $b$ is not in that plane, the system has no exact solution; the least squares solution projects $b$ onto $\operatorname{Col}(A)$.

Solving by normal equations:
$$
A^T A =
\begin{bmatrix}3 & 1\\ 1 & 3\end{bmatrix},
\quad
A^T b =
\begin{bmatrix}6\\4\end{bmatrix},
\quad
\Rightarrow
\begin{bmatrix}3 & 1\\ 1 & 3\end{bmatrix}
\begin{bmatrix}x_1\\x_2\end{bmatrix}
=
\begin{bmatrix}6\\4\end{bmatrix}
\ \Rightarrow\
x_1=\tfrac{7}{4},\ x_2=\tfrac{3}{4}.
$$
