# Orthogonal Complements

*Original Note: [[L05 - Orthogonality of Fundamental Subspaces]]*

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
