# Orthogonal Complements and the Four Fundamental Subspaces

*Original Note: [[L06]]*

> [!thm] Orthogonal Complements of Range and Nullspace
> For any matrix $A \in \mathbb{R}^{m \times n}$,
> - $R(A)^\perp = N(A^T)$ in $\mathbb{R}^m$.
> - $R(A^T)^\perp = N(A)$ in $\mathbb{R}^n$.

> [!pf] Proof
> Let $x \in \mathbb{R}^m$. Then $x \in R(A)^\perp$ if and only if
> $$\langle x, Ay\rangle = 0 \quad \text{for all } y \in \mathbb{R}^n.$$
> Using $\langle u,v\rangle = u^T v$,
> $$\langle x, Ay\rangle = (Ay)^T x = y^T A^T x = \langle y, A^T x\rangle.$$
> If this equals $0$ for all $y$, then $A^T x = 0$, so $x \in N(A^T)$. Conversely, if $A^T x=0$, then $\langle x, Ay\rangle = 0$ for all $y$, hence $x \in R(A)^\perp$. Thus $R(A)^\perp = N(A^T)$.
> Replacing $A$ by $A^T$ gives $R(A^T)^\perp = N(A)$.

> [!thm] Direct Sum Decompositions
> Let $r = \operatorname{rank}(A)$. Then
> - $\mathbb{R}^n = N(A) \oplus R(A^T)$ with $\dim N(A) = n - r$ and $\dim R(A^T) = r$.
> - $\mathbb{R}^m = R(A) \oplus N(A^T)$ with $\dim R(A) = r$ and $\dim N(A^T) = m - r$.

> [!pf] Proof
> From $R(A^T)^\perp = N(A)$, the subspaces are orthogonal and intersect trivially. Their dimensions sum to $n$: $\dim N(A) + \dim R(A^T) = (n-r) + r = n$, hence $\mathbb{R}^n = N(A) \oplus R(A^T)$. The second identity is analogous using $R(A)^\perp = N(A^T)$ and $m = r + (m-r)$.
