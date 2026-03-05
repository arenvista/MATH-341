# Worked Example 1 (No Pivoting)

*Original Note: [[L03 - LU Factorization]]*

> [!pf] Example: Compute $A=LU$
> Given
> $$
> A=
> \begin{bmatrix}
> 2 & 1 & 1 & 0\\
> 4 & 3 & 3 & 1\\
> 8 & 7 & 9 & 5\\
> 6 & 7 & 9 & 5
> \end{bmatrix},
> $$
> perform elimination to get $U$ and recover $L$ from the multipliers.
> 
> Step 1 (pivot $a_{11}=2$):
> - Multipliers: $m_{21}=2,\ m_{31}=4,\ m_{41}=3$.
> - Elimination matrix:
> $$
> L_1=
> \begin{bmatrix}
> 1&0&0&0\\
> -2&1&0&0\\
> -4&0&1&0\\
> -3&0&0&1
> \end{bmatrix},
> \quad
> L_1A=
> \begin{bmatrix}
> 2 & 1 & 1 & 0\\
> 0 & 1 & 1 & 1\\
> 0 & 3 & 5 & 5\\
> 0 & 4 & 6 & 5
> \end{bmatrix}.
> $$
> 
> Step 2 (pivot $a_{22}^{(1)}=1$):
> - Multipliers: $m_{32}=3,\ m_{42}=4$.
> - Elimination matrix:
> $$
> L_2=
> \begin{bmatrix}
> 1&0&0&0\\
> 0&1&0&0\\
> 0&-3&1&0\\
> 0&-4&0&1
> \end{bmatrix},
> \quad
> L_2L_1A=
> \begin{bmatrix}
> 2 & 1 & 1 & 0\\
> 0 & 1 & 1 & 1\\
> 0 & 0 & 2 & 2\\
> 0 & 0 & 2 & 1
> \end{bmatrix}.
> $$
> 
> Step 3 (pivot $a_{33}^{(2)}=2$):
> - Multiplier: $m_{43}=1$.
> - Elimination matrix:
> $$
> L_3=
> \begin{bmatrix}
> 1&0&0&0\\
> 0&1&0&0\\
> 0&0&1&0\\
> 0&0&-1&1
> \end{bmatrix},
> \quad
> U=L_3L_2L_1A=
> \begin{bmatrix}
> 2 & 1 & 1 & 0\\
> 0 & 1 & 1 & 1\\
> 0 & 0 & 2 & 2\\
> 0 & 0 & 0 & -1
> \end{bmatrix}.
> $$
> 
> Recover $L$ from inverses of elimination matrices:
> $$
> L=L_1^{-1}L_2^{-1}L_3^{-1}=
> \begin{bmatrix}
> 1&0&0&0\\
> 2&1&0&0\\
> 4&3&1&0\\
> 3&4&1&1
> \end{bmatrix}.
> $$
> 
> Check: $LU=A$ (verified by direct multiplication).


> [!cor] Quick Inverse Rule (Per Step)
> For a single elimination step $L_k=I-m\,e_{ik}$ (unit lower triangular),
> $$L_k^{-1}=I+m\,e_{ik},$$
> i.e., flip the signs of the newly created subdiagonal entries for that step.
> 
> Caution: This sign-flip rule applies to each elimination matrix $L_k$ individually; it does not mean “flip all signs below the diagonal” for a general lower triangular matrix.
