# 3) Data Fitting via Least Squares

*Original Note: [[L09 - Least Squares]]*

Goal: Given data $\{(x_i,y_i)\}_{i=1}^N$ and a model $\hat{y}_i = f(x_i;\theta)$ with parameters $\theta$, choose $\theta$ to minimize the sum of squared residuals:
$$
\operatorname{SSE}(\theta) = \sum_{i=1}^N (y_i - \hat{y}_i)^2 = \|A\theta - b\|_2^2.
$$

> [!def] Residual, SSE, RMSE
> - Residual vector: $r = b - A\hat{\theta}$.
> - Sum of Squared Errors (SSE): $\|r\|_2^2 = \sum_i r_i^2$.
> - Root Mean Squared Error (RMSE): $\sqrt{\frac{1}{N} \sum_i r_i^2} = \sqrt{\frac{\mathrm{SSE}}{N}}$.

```tikz
\begin{document}
\begin{tikzpicture}[domain=0:5]

	% Grid
	\draw[very thin,color=gray!30] (-0.5,-0.5) grid (5.5,5.5);

	% Axes
	\draw[->] (-0.2,0) -- (5.5,0) node[right] {$x$};
	\draw[->] (0,-0.2) -- (0,5.5) node[above] {$y$};

	% Data points
	\filldraw[black] (0.5,1.2) circle (2pt);
	\filldraw[black] (1.2,1.9) circle (2pt);
	\filldraw[black] (2.0,2.5) circle (2pt);
	\filldraw[black] (3.0,3.7) circle (2pt);
	\filldraw[black] (4.2,4.1) circle (2pt);

	% Best fit line (approximate)
	\draw[color=red, thick]
	plot (\x,{0.8*\x + 0.8})
	node[right] {$\hat{y} = ax + b$};

	% Residual lines (vertical distances)
	\draw[dashed,blue] (0.5,1.2) -- (0.5,{0.8*0.5+0.8});
	\draw[dashed,blue] (1.2,1.9) -- (1.2,{0.8*1.2+0.8});
	\draw[dashed,blue] (2.0,2.5) -- (2.0,{0.8*2.0+0.8});
	\draw[dashed,blue] (3.0,3.7) -- (3.0,{0.8*3.0+0.8});
	\draw[dashed,blue] (4.2,4.1) -- (4.2,{0.8*4.2+0.8});

	% Label
	\node at (3.8,1.0) {\small Minimize $\sum (y_i - \hat{y}_i)^2$};

\end{tikzpicture}
\end{document}
```

> [!def] Algorithm: Linear Least Squares via Normal Equations
> 1. Given data $\{(x_i,y_i)\}_{i=1}^N$.
> 2. Choose a model (e.g., linear, polynomial) that is linear in its parameters.
> 3. Build the design matrix $A$ and right-hand side $b$ using the data.
> 4. Solve the normal equations $A^TA\,\theta = A^T b$ for $\theta$.
> 5. Compute residuals and error metrics (SSE, RMSE); refine the model if needed.
