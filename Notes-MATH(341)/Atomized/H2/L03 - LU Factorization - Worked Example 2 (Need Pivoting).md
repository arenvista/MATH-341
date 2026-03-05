# Worked Example 2 (Need Pivoting)

*Original Note: [[L03 - LU Factorization]]*

> [!pf] Example: Why Pivoting May Be Necessary
> Try $A=\begin{bmatrix}0&1\\[2pt]1&1\end{bmatrix}=LU$ with $L=\begin{bmatrix}1&0\\ \ell&1\end{bmatrix}$ and $U=\begin{bmatrix}u_{11}&u_{12}\\ 0&u_{22}\end{bmatrix}$.
> 
> Matching entries gives $u_{11}=0$ and $\ell\,u_{11}=1\implies 0=1$ (contradiction). Thus no $LU$ exists without row swaps.
> 
> Swap rows with $P=\begin{bmatrix}0&1\\ 1&0\end{bmatrix}$:
> $$
> PA=\begin{bmatrix}1&1\\ 0&1\end{bmatrix}.
> $$
> This is already upper triangular, so we may take
> $$L=I,\qquad U=PA.$$
> Hence $PA=LU$ and the system $Ax=b$ is solved via $Ly=Pb$ then $Ux=y$.
