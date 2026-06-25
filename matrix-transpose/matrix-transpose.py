import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    row, col = len(A), len(A[0])
    
    if row==col:
        for i in range(row):
            for j in range(i+1, row):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        return np.asarray(A)

    else:
        res = [[0 for _ in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
               res[j][i] = A[i][j]
        return np.asarray(res)
        
