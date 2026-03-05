# Symmetric Positive Definite (SPD)

*Original Note: [[L04 - Cholesky Factorization]]*

> [!def] Symmetric Matrix
> A matrix $A \in \mathbb{R}^{n \times n}$ is symmetric if
> $$A = A^T.$$

> [!def] Positive Definite Matrix
> A symmetric matrix $A \in \mathbb{R}^{n \times n}$ is positive definite if
> $$v^T A v > 0 \quad \text{for all } v \in \mathbb{R}^n \setminus \{\vec{0}\}.$$

> [!imp] Notes
> - Every SPD matrix is nonsingular (invertible).
> - All eigenvalues of an SPD matrix are positive.

> [!thm] Cholesky Factorization — Existence and Uniqueness
> If $A \in \mathbb{R}^{n \times n}$ is SPD, then there exists a unique upper-triangular matrix $R$ with strictly positive diagonal entries such that
> $$A = R^T R.$$
> Equivalently, there exists a unique lower-triangular $L$ with positive diagonal such that $A = L L^T$.

> [!pf] Proof sketch
> Proceed by induction on $n$. For $n=1$, the claim is trivial. Assume the claim for $(n-1)\times(n-1)$ SPD matrices. Partition
> $$A = \begin{bmatrix} \alpha & a^T \\ a & B \end{bmatrix}, \quad \alpha \in \mathbb{R}, \; a \in \mathbb{R}^{n-1}, \; B \in \mathbb{R}^{(n-1)\times(n-1)}.$$
> Since $A$ is SPD, $\alpha>0$. Define $r_{11}=\sqrt{\alpha}$ and $r_{1,2:n} = r_{11}^{-1} a^T$. The Schur complement $S = B - r_{11}^{-2} a a^T$ is also SPD. By the induction hypothesis, $S = \tilde{R}^T \tilde{R}$ for some upper-triangular $\tilde{R}$ with positive diagonal. Then
> $$R = \begin{bmatrix} r_{11} & r_{1,2:n} \\ 0 & \tilde{R} \end{bmatrix}$$
> satisfies $A=R^T R$. Uniqueness follows from positivity of the diagonal and triangular structure.

> [!imp] Computational formulas (upper-triangular form)
> For $A=[a_{ij}]$ and $R=[r_{ij}]$ with $R$ upper-triangular,
> - Diagonal: $$r_{ii} = \sqrt{a_{ii} - \sum_{k=1}^{i-1} r_{k i}^2} \quad (i=1,\dots,n).$$
> - Off-diagonal: $$r_{ij} = \frac{a_{ij} - \sum_{k=1}^{i-1} r_{k i} r_{k j}}{r_{ii}} \quad (1 \le i < j \le n).$$
