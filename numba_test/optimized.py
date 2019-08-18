import sys
import numpy as np
import time
import numba


@numba.jit(nopython=True, parallel=True)
def fun(a,b,n):
    out = np.empty_like(a)
    for i in range(n):
        c[i]=a[i]+b[i]
    return c

if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(sys.argv[1])
a=np.random.uniform(low=-100, high=100, size=(n), dtype=np.float32)
b=np.random.uniform(low=-100, high=100, size=(n), dtype=np.float32)
start = time.perf_counter()
returnc = fun(a,b,n)
end=time.perf_counter()
# print(c)
print("Elapsed Time: " + str(end - start))
