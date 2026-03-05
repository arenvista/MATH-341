# Householder Reflectors

*Original Note: [[L08 - Lecture L08 — Orthogonal Matrices Projectors, Reflectors, and Rotators]]*

> [!def] Householder reflector
> For $v\in\mathbb{R}^n$ with $\|v\|=1$, the Householder reflector is
> $$
> R = I - 2vv^T.
> $$

> [!thm] Properties of Householder reflectors
> $$
> R^T = R \quad \text{(symmetric)},\qquad
> R^TR = I \quad \text{(orthogonal)},\qquad
> R^2 = I \quad \text{(involution)}.
> $$
> The eigenvalues are $-1$ (once, along $v$) and $+1$ (with multiplicity $n-1$, on $v^\perp$).

> [!pf] Proof sketch
> Symmetry: $(I-2vv^T)^T=I-2vv^T$.  
> Orthogonality: $R^TR=(I-2vv^T)^2=I-4vv^T+4v(v^Tv)v^T=I$ since $v^Tv=1$.  
> Hence $R^{-1}=R^T=R$, so $R^2=I$.  
> Also $Rv=(1-2)v=-v$ and $Rw=w$ for $w\perp v$.

### Using Householder reflectors to sparsify a vector
Goal: Given $x\in\mathbb{R}^m$, construct $R$ so that $Rx=\pm \|x\| e_1$.

- Construct:
  - Choose the sign to avoid cancellation:
    $$
    \alpha = -\operatorname{sign}(x_1)\,\|x\|, \quad
    u = x - \alpha e_1.
    $$
    If $u=0$ (happens when $x$ already aligned with $e_1$), take $R=I$.
  - Normalize $v = u/\|u\|$ and set $R = I - 2vv^T$.
- Then:
  $$
  Rx = \alpha e_1 = \pm \|x\| e_1.
  $$

> [!imp] Numerical note
> Choosing $\alpha=-\operatorname{sign}(x_1)\|x\|$ improves numerical stability by reducing catastrophic cancellation in $u=x-\alpha e_1$.

---
