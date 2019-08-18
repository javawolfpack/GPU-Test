import sys
import numpy as np
import time


def fun(a,b,n):
    c=[]
    for i in range(n):
        c+=[a[i]+b[i]]
    return c

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
