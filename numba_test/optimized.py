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
