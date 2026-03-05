# Orthogonal Projectors

*Original Note: [[L06]]*

> [!def] Orthogonal Projector onto a Line
> If $u \in \mathbb{R}^m$ is a unit vector, the orthogonal projector onto $\operatorname{span}\{u\}$ is
> $$P_u = u u^T.$$
> For general nonzero $u$, normalize:
> $$P_u = \frac{u u^T}{u^T u}.$$

- Action on a vector:
  $$
  P_u x = (u u^T) x = u (u^T x) = \langle u, x\rangle\, u.
  $$

- Properties (unit $u$):
  - Symmetric: $P_u^T = P_u$.
  - Idempotent: $P_u^2 = P_u$.
  - Projects onto span$(u)$ along its orthogonal complement.

> [!lem] Projector onto a Subspace Spanned by Orthonormal Columns
> If $Q \in \mathbb{R}^{m \times k}$ has orthonormal columns, the orthogonal projector onto $R(Q)$ is
> $$P = QQ^T,$$
> with $P^T = P$ and $P^2 = P$.
> Moreover, for any $x$, $QQ^T x$ is the unique vector in $R(Q)$ closest to $x$ in Euclidean norm.
