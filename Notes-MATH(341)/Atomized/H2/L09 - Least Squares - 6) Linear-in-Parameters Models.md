# 6) Linear-in-Parameters Models

*Original Note: [[L09 - Least Squares]]*

Many approximations are linear in parameters even if basis functions are nonlinear in $x$:
$$
\hat{y}(t) = c_1 \phi_1(t) + c_2 \phi_2(t) + \cdots + c_p \phi_p(t).
$$

Example with trigonometric bases (for positive data over time $t$):
$$
\hat{y}(t) = c_1 + c_2 \cos^2(x)\,t + c_3 \sin(2x)\,t + c_4 \cos(4x)\,t + \cdots
$$
As long as the model is linear in the coefficients $c_j$, we can build $A$ with $A_{ij}=\phi_j(t_i)$ and solve least squares.
