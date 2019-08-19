import sys
import numpy as np
from numba import jit
import time
import timeit


@jit(nopython=True, parallel=True, fastmath=True)
def fun(a,b,n):
    result = np.zeros((n,n), dtype=np.float32)

    # iterate through rows of a
    for i in range(len(a)):
       # iterate through columns of b
       for j in range(len(b[0])):
           # iterate through rows of b
           for k in range(len(b)):
               result[i][j] += a[i][k] * b[k][j]

    return result


if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(sys.argv[1])
n=n*16 #consistency with cuda3.py implementation
a=np.random.uniform(low=-100, high=100, size=(n,n)).astype(np.float32)
b=np.random.uniform(low=-100, high=100, size=(n,n)).astype(np.float32)
# print(a)
# print(b)
start = time.perf_counter()
c=fun(a,b,n)
end=time.perf_counter()
print("Elapsed Time: " + str(end - start))
