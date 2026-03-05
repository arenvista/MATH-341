# 7) Nonlinear Models and Data Linearization

*Original Note: [[L09 - Least Squares]]*

Some nonlinear models can be linearized via transformations.

- Exponential model: $y = c_1 e^{c_2 t}$ with $y>0$.
  $$
  \ln y = \ln c_1 + c_2 t
  \quad\Longrightarrow\quad
  Y := \ln y = k + c_2 t,\ \ k:=\ln c_1.
  $$
  Regress $Y$ on $t$, then recover $c_1=e^k$.

- Power-law model: $y = c_1 t^{c_2}$ with $y>0$, $t>0$.
  $$
  \ln y = \ln c_1 + c_2 \ln t
  \quad\Longrightarrow\quad
  Y := \ln y = k + c_2 X,\ \ X:=\ln t,\ \ k:=\ln c_1.
  $$
  Regress $Y$ on $X=\ln t$, then recover $c_1=e^k$.

> [!imp] Important caveats
> - Transforming the data (e.g., taking logs) changes the error model; least squares in transformed space is not the same objective as least squares in original space.
> - Ensure domain restrictions (e.g., $y>0$, $t>0$) are satisfied.
