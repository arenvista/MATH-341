# Quick Summary Table

*Original Note: [[L08 - Lecture L08 — Orthogonal Matrices Projectors, Reflectors, and Rotators]]*

- Projector onto $u^\perp$: $Q=I-uu^T$ (unit $u$); complementary $P_u=uu^T$.
- Reflector across $u^\perp$: $R=I-2uu^T$ (unit $u$); symmetric, orthogonal, $R^2=I$.
- Givens rotation in $(i,j)$-plane: $P_{i,j}(c,s)$ with $c^2+s^2=1$, 2×2 block $\begin{bmatrix}c&s\\-s&c\end{bmatrix}$.
- Vector annihilation:
  - Householder: one step to map $x\mapsto \pm\|x\|e_1$.
  - Givens: sequence $P_{1,n}\cdots P_{1,2}$ maps $x\mapsto \|x\|e_1$.
- QR by Householder: $A=QR$ with $Q$ orthogonal, $R$ upper triangular, via left-multiplication by reflectors.
