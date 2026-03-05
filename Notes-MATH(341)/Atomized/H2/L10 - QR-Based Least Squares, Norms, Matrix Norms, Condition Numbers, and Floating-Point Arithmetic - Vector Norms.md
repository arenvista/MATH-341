# Vector Norms

*Original Note: [[L10 - QR-Based Least Squares, Norms, Matrix Norms, Condition Numbers, and Floating-Point Arithmetic]]*

> [!def] Vector norm
> A function $\|\cdot\|:\mathbb{R}^n \to \mathbb{R}$ is a norm if, for all $x,y \in \mathbb{R}^n$ and scalars $\alpha$:
> - Positive definiteness: $\|x\|\ge 0$ and $\|x\|=0 \Leftrightarrow x=0$.
> - Absolute homogeneity: $\|\alpha x\| = |\alpha|\,\|x\|$.
> - Triangle inequality: $\|x+y\| \le \|x\| + \|y\|$.

Examples (the $\ell_p$ family):
$$
\begin{aligned}
\|x\|_1 &= \sum_{i=1}^n |x_i|,\\
\|x\|_2 &= \Big(\sum_{i=1}^n |x_i|^2\Big)^{1/2} = (x^\top x)^{1/2},\\
\|x\|_\infty &= \max_{1\le i\le n} |x_i|,\\
\|x\|_p &= \Big(\sum_{i=1}^n |x_i|^p\Big)^{1/p},\quad 1\le p<\infty.
\end{aligned}
$$
