import sys
import numpy as np
from numba import njit, prange, cuda
import time

# @njit(parallel=True)
@cuda.jit
def fun(a, b, n):
    result = np.zeros(n)
    # for i in prange(n):
    #     # print(a[i])
    #     result[i]=a[i]+b[i]
    pos = cuda.grid(1)
    if pos < n:
        result[pos]=a[pos] + b[pos]
    # your loop or numerically intensive computations
    return result


if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(sys.argv[1])
a=np.random.uniform(low=-100, high=100, size=(n))
b=np.random.uniform(low=-100, high=100, size=(n))
start = time.perf_counter()
c=fun(a,b,n)
end=time.perf_counter()
print(c)
print("Elapsed Time: " + str(end - start))
