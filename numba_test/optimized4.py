import numpy as np
from numba import cuda

@cuda.jit
def matadd(A, B, C):
    i, j = cuda.grid(2)
    if i < C.shape[0] and j < C.shape[1]:
        C[i][j] = A[i][j] + B[i][j]
    cuda.syncthreads()

n=4
a=np.random.uniform(low=-100, high=100, size=(n,n)).astype(np.float32)
b=np.random.uniform(low=-100, high=100, size=(n,n)).astype(np.float32)
result = np.zeros((n,n), dtype=np.float32)
matadd(a,b, result)
print(result)
