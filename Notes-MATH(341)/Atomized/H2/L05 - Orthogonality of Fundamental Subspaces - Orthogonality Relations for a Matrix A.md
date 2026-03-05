# Orthogonality Relations for a Matrix A

*Original Note: [[L05 - Orthogonality of Fundamental Subspaces]]*

> [!thm] Orthogonality of the four fundamental subspaces
> For $A\in\mathbb{R}^{m\times n}$,
> $$
> R(A)^\perp=\mathrm{Nul}(A^\top) \quad\text{and}\quad R(A^\top)^\perp=\mathrm{Nul}(A).
> $$

> [!pf] Proof
> Let $x\in\mathbb{R}^m$. Then $x\in R(A)^\perp$ iff $\langle x,Ay\rangle=0$ for all $y\in\mathbb{R}^n$, i.e.,
> $$
> \langle x,Ay\rangle = (Ay)^\top x = y^\top (A^\top x) = \langle y, A^\top x\rangle = 0 \quad \forall\, y
> \iff A^\top x=0 \iff x\in \mathrm{Nul}(A^\top).
> $$
> The second identity follows by applying the first to $A^\top$:
> $$
> R(A^\top)^\perp=\mathrm{Nul}((A^\top)^\top)=\mathrm{Nul}(A).
> $$

> [!cor] Consequences
> - Direct sums:
>   $$
>   \mathbb{R}^m = R(A) \oplus \mathrm{Nul}(A^\top),\qquad
>   \mathbb{R}^n = R(A^\top) \oplus \mathrm{Nul}(A).
>   $$
> - Dimensions (rank–nullity decompositions):
>   $$
>   \dim R(A) + \dim \mathrm{Nul}(A^\top) = m,\qquad
>   \dim R(A^\top) + \dim \mathrm{Nul}(A) = n.
>   $$

#^
