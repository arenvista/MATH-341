# 5) Example: Best-Fit Parabola

*Original Note: [[L09 - Least Squares]]*

Model: $\hat{y} = a x^2 + b x + c$ with the same data.

Design matrix and right-hand side:
$$
A=
\begin{bmatrix}
1 & -1 & 1\\
0 & 0 & 1\\
1 & 1 & 1\\
4 & 2 & 1
\end{bmatrix},
\quad
b=
\begin{bmatrix}
1\\0\\0\\-2
\end{bmatrix}.
$$

Normal equations:
$$
A^T A=
\begin{bmatrix}
18 & 8 & 6\\
8 & 6 & 2\\
6 & 2 & 4
\end{bmatrix},
\quad
A^T b =
\begin{bmatrix}
-7\\ -5\\ -1
\end{bmatrix}.
$$

Solution:
$$
a=-0.25,\quad b=-0.65,\quad c=0.45,\quad
\hat{y}=-0.25x^2-0.65x+0.45.
$$

Residuals and error:
- Residuals $r_i = y_i - \hat{y}_i$ at $x=-1,0,1,2$ are $(0.15,-0.45,0.45,-0.15)$.
- $\mathrm{SSE} = 0.45$, $\mathrm{RMSE} = \sqrt{0.45/4} \approx 0.3354$.
- The quadratic fit reduces error relative to the line in this dataset.

```tikz
\begin{document}
\begin{tikzpicture}[domain=-1.5:2.5]

	% Grid
	\draw[very thin,color=gray!30] (-1.5,-2.8) grid (2.5,1.8);

	% Axes
	\draw[->] (-1.5,0) -- (2.6,0) node[right] {$x$};
	\draw[->] (0,-2.8) -- (0,1.8) node[above] {$y$};

	% Data points
	\filldraw[black] (-1,1) circle (2.5pt) node[above left] {$(-1,1)$};
	\filldraw[black] (0,0) circle (2.5pt) node[above right] {$(0,0)$};
	\filldraw[black] (1,0) circle (2.5pt) node[above right] {$(1,0)$};
	\filldraw[black] (2,-2) circle (2.5pt) node[below right] {$(2,-2)$};

	% Quadratic least squares curve
	\draw[color=red, thick]
	plot (\x,{-0.25*\x*\x -0.65*\x +0.45})
	node[right] {$\hat{y}=-0.25x^2-0.65x+0.45$};

	% Residuals (vertical)
	\draw[dashed,blue] (-1,1) -- (-1,{-0.25*(-1)*(-1)-0.65*(-1)+0.45});
	\draw[dashed,blue] (0,0) -- (0,{0.45});
	\draw[dashed,blue] (1,0) -- (1,{-0.25-0.65+0.45});
	\draw[dashed,blue] (2,-2) -- (2,{-0.25*4-0.65*2+0.45});

	% Labels
	\node at (1.6,1.4) {\small $r_i = y_i - \hat{y}_i$};
	\node at (1.3,-2.4) {\small Minimize $\sum r_i^2 = \|A\theta-b\|_2^2$};

\end{tikzpicture}
\end{document}
```

> [!imp] Conditioning
> Using normal equations squares the condition number:
> $$
> \kappa_2(A^T A) = \kappa_2(A)^2.
> $$
> This can significantly degrade numerical stability. Prefer QR or SVD in practice, especially for ill-conditioned problems.
