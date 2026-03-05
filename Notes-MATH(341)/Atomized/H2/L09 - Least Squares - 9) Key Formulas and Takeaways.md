# 9) Key Formulas and Takeaways

*Original Note: [[L09 - Least Squares]]*

- Projection condition: $A^T(b-A\hat{x})=0$.
- Normal equations: $A^T A \hat{x} = A^T b$; $\hat{x}=(A^T A)^{-1}A^T b$ if $A$ has full column rank.
- Error metrics: $\mathrm{SSE}=\|b-A\hat{x}\|_2^2$, $\mathrm{RMSE}=\sqrt{\mathrm{SSE}/N}$.
- Prefer QR or SVD over normal equations for numerical stability.
