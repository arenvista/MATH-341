import numpy as np
from numpy.typing import NDArray
from typing import Tuple

def pmatrix(matrix):
    for row in matrix: print(row)
    
def _latex_matrix(M: NDArray) -> str:
    rows = []
    for row in M:
        rows.append(" & ".join(str(val) for val in row))
    body = " \\\\\n".join(rows)
    return "\\begin{bmatrix}\n" + body + "\n\\end{bmatrix}"

def tex_mult(A: NDArray, X: NDArray) -> Tuple[NDArray, str]:
    if A.shape[1] != X.shape[0]:
        raise ValueError(f"Invalid Shape: A{A.shape} | X{X.shape}")
    m, n = A.shape
    _, p = X.shape

    result = np.zeros((m, p), dtype=A.dtype)

    # Compute result
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i, j] += A[i, k] * X[k, j]

    # Build expanded multiplication matrix
    expanded_rows = []
    for i in range(m):
        row_entries = []
        for j in range(p):
            terms = [f"{A[i,k]} \\cdot {X[k,j]}" for k in range(n)]
            row_entries.append(" + ".join(terms))
        expanded_rows.append(" & ".join(row_entries))

    expanded_body = " \\\\\n".join(expanded_rows)
    expanded_matrix = (
        "\\begin{bmatrix}\n" +
        expanded_body +
        "\n\\end{bmatrix}"
    )

    # Build final LaTeX string
    latex_string = (
        "$$\n"
        "Ax =\n"
        f"{_latex_matrix(A)}\n"
        f"{_latex_matrix(X)} =\n"
        f"{expanded_matrix} =\n"
        f"{_latex_matrix(result)}\n"
        "$$"
    )

    return result, latex_string

        
def main():
    # ((2*2) + (0*0) + (0*0)
    A = [
        [2,0,0],
        [0,1,0],
        [0,0,2]
    ]
    B = [
        [2,0,0],
        [0,2,0],
        [0,0,2]
    ]

    C = [ 
        ["[1,1]","(1,2)","(1,3)"], 
         ["(2,1)","(2,2)","(2,3)"], 
         ["(3,1)","(3,2)","(3,3)"]
    ]
    A = np.array(A)
    B = np.array(B)
    a,b = tex_mult(A,B)
    print(b)
    print(a)


if __name__ == "__main__":
    main()
