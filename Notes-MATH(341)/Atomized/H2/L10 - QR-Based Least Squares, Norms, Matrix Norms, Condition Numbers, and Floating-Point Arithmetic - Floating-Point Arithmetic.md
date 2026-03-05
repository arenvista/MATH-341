# Floating-Point Arithmetic

*Original Note: [[L10 - QR-Based Least Squares, Norms, Matrix Norms, Condition Numbers, and Floating-Point Arithmetic]]*

> [!def] Floating-point representation
> A (normalized) floating-point number in base $\beta$ with $t$ significant digits has the form
> $$
> x = \pm\big( d_1.d_2 d_3 \dots d_t \big)_\beta \times \beta^{\,e},\quad d_1\in\{1,\dots,\beta-1\},\ d_k\in\{0,\dots,\beta-1\}.
> $$
> Components:
> - Mantissa (significand): $d_1 d_2 \dots d_t$
> - Base: $\beta$
> - Exponent: $e$

Let $\mathrm{fl}(x)$ denote the floating-point representation (after rounding) of the real $x$. In general:
$$
\mathrm{fl}(x+y) \ne \mathrm{fl}(x) + \mathrm{fl}(y),\qquad
\mathrm{fl}(xy) \ne \mathrm{fl}(x)\,\mathrm{fl}(y).
$$

### Example: Gaussian elimination and pivoting in finite precision

Consider
$$
\begin{aligned}
-10^{-4}\,x + y &= 1,\\
\ \ \ \ \ \ \ \ x + y &= 2.
\end{aligned}
$$

Exact solution:
$$
(1+10^{-4})x = 1 \ \Rightarrow\ x \approx 0.99990001,\quad y \approx 1.00009999.
$$

- Elimination without pivoting (use the first row as pivot):
  - Multiplier is $10^{4}$; the second row becomes
    $$
    [\,0,\ 1 + 10^{4}\ |\ 2 + 10^{4}\,] = [\,0,\ 10001\ |\ 10002\,].
    $$
  - With limited $t$-digit mantissa, these may round to $[\,0,\ 1.000\times 10^4\ |\ 1.000\times 10^4\,]$, giving $y=1$ and then $x=0$ from the first equation.

- Partial pivoting (swap rows first):
  - Use the row with larger $|a_{11}|$ as pivot:
    $$
    \begin{bmatrix} 1 & 1 &|& 2 \\ -10^{-4} & 1 &|& 1 \end{bmatrix}
    \xrightarrow{\ R_2 \leftarrow R_2 + 10^{-4} R_1\ }
    \begin{bmatrix} 1 & 1 &|& 2 \\ 0 & 1+10^{-4} &|& 1+2\cdot 10^{-4} \end{bmatrix}.
    $$
  - No large growth occurs; rounding errors are greatly reduced, and the computed solution is close to the exact one.

> [!imp] Takeaway
> - Avoid large multipliers in elimination: use (partial) pivoting.
> - Large intermediate numbers amplify rounding and truncation errors.
> - QR-based methods are often more stable for least-squares than forming normal equations $A^\top A$ explicitly.
