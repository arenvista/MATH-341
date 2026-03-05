# 4) Example: Best-Fit Line

*Original Note: [[L09 - Least Squares]]*

Data: $\{(-1,1), (0,0), (1,0), (2,-2)\}$ with model $\hat{y}=a x + b$.

Design matrix and right-hand side:
$$
A=
\begin{bmatrix}
-1 & 1\\
0 & 1\\
1 & 1\\
2 & 1
\end{bmatrix},
\quad
b=
\begin{bmatrix}
1\\0\\0\\-2
\end{bmatrix}.
$$

Normal equations:
$$
A^T A =
\begin{bmatrix}
6 & 2\\
2 & 4
\end{bmatrix},
\quad
A^T b =
\begin{bmatrix}
-5\\
-1
\end{bmatrix},
\quad
\Rightarrow
\begin{bmatrix}
6 & 2\\
2 & 4
\end{bmatrix}
\begin{bmatrix}a\\b\end{bmatrix}
=
\begin{bmatrix}-5\\-1\end{bmatrix}.
$$

Solution:
$$
a=-0.9,\quad b=0.2,\quad \hat{y}=-0.9x+0.2.
$$

Residuals and error:
- Residuals $r_i = y_i - \hat{y}_i$ at $x=-1,0,1,2$ are $(-0.1,-0.2,0.7,-0.4)$.
- $\mathrm{SSE} = 0.70$, $\mathrm{RMSE} = \sqrt{0.70/4} \approx 0.4183$.

```tikz
\begin{document}
\begin{tikzpicture}[domain=-1.5:2.5]

	% Grid
	\draw[very thin,color=gray!30] (-1.5,-2.5) grid (2.5,1.5);

	% Axes
	\draw[->] (-1.5,0) -- (2.6,0) node[right] {$x$};
	\draw[->] (0,-2.6) -- (0,1.6) node[above] {$y$};

	% Data points
	\filldraw[black] (-1,1) circle (2.5pt) node[above left] {$(-1,1)$};
	\filldraw[black] (0,0) circle (2.5pt) node[above right] {$(0,0)$};
	\filldraw[black] (1,0) circle (2.5pt) node[above right] {$(1,0)$};
	\filldraw[black] (2,-2) circle (2.5pt) node[below right] {$(2,-2)$};

	% Least squares line
	\draw[color=red, thick]
	plot (\x,{-0.9*\x + 0.2})
	node[right] {$\hat{y}=-0.9x+0.2$};

	% Residuals (vertical)
	\draw[dashed,blue] (-1,1) -- (-1,{ -0.9*(-1) + 0.2});
	\draw[dashed,blue] (0,0) -- (0,{ -0.9*(0) + 0.2});
	\draw[dashed,blue] (1,0) -- (1,{ -0.9*(1) + 0.2});
	\draw[dashed,blue] (2,-2) -- (2,{ -0.9*(2) + 0.2});

	% Label for residual meaning
	\node at (1.6,1.2) {\small $r_i = y_i - \hat{y}_i$};
	\node at (1.3,-2.2) {\small Minimize $\sum r_i^2$};

\end{tikzpicture}
\end{document}
```
