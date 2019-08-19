import sys
import numpy as np
from numba import njit, prange, cuda
import time

# @njit(parallel=True)
@cuda.jit
def fun(a, b, n, result):
    # for i in prange(n):
    #     # print(a[i])
    #     result[i]=a[i]+b[i]
    pos = cuda.grid(1)
    if pos < n:
        result[pos]=a[pos] + b[pos]
    # your loop or numerically intensive computations
    return result

bpg = 50
tpb = 32
n = bpg * tpb

@jit(argtypes=[float32[:,:], float32[:,:], float32[:,:]], target='gpu')
def cu_square_matrix_mul(A, B, C):
    sA = cuda.shared.array(shape=n, dtype=float32)
    sB = cuda.shared.array(shape=n, dtype=float32)

    i = cuda.grid(1)


    acc = 0.
    for i in range(n):
        if i < n:
            sA[i] = A[i]
            sB[i] = B[i]

        cuda.syncthreads()

        if i<n
            for j in range(n):
                acc += sA[i] * sB[i]

        cuda.syncthreads()

    if i<n:
        C[i] = acc


@cuda.jit
def matadd(A, B, C):
    """Perform matrix addition of C = A + B
    """
    i = cuda.grid(1)
    d_A = cuda.to_device(A)
    d_A = cuda.to_device(B)
    d_C = cuda.to_device(C)
    if i < d_C.shape[0]:
        d_C[i] = d_A[i]+d_B[i]
    # return C
    C=d_C.copy_to_host()


if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(sys.argv[1])
a=np.random.uniform(low=-100, high=100, size=(n))
b=np.random.uniform(low=-100, high=100, size=(n))
start = time.perf_counter()
result = np.zeros(n)
matadd(a,b, result)
end=time.perf_counter()
print(result)
print("Elapsed Time: " + str(end - start))
