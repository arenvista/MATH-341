# Orthogonality of Fundamental Subspaces

*Original Note: [[L05]]*

## Orthogonal Complements

> [!def] Orthogonal complement
> Let $V$ be an inner product space and $M\subseteq V$ a subspace. The orthogonal complement of $M$ is
> $$
> M^\perp := \{\, x\in V : \langle m, x\rangle = 0 \text{ for all } m\in M \,\},
> $$
> where $\langle x,y\rangle = x^\top y$ is the standard inner product on $\mathbb{R}^k$.

> [!cor] Direct sum with an orthogonal complement
> In finite dimensions,
> $$
> V = M \oplus M^\perp,
> $$
> i.e., every $v\in V$ decomposes uniquely as $v=m+m^\perp$ with $m\in M$ and $m^\perp\in M^\perp$.

## Orthogonality Relations for a Matrix A

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
# Extractions -------------
# Orthogonality of Fundamental Subspaces

*Original Note: [[L05]]*

## Orthogonal Complements

*Extracted to: [[L05 - Orthogonality of Fundamental Subspaces - Orthogonal Complements]]*

## Orthogonality Relations for a Matrix A

*Extracted to: [[L05 - Orthogonality of Fundamental Subspaces - Orthogonality Relations for a Matrix A]]*

