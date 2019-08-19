import sys
import numpy as np
import time
import timeit



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

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(sys.argv[1])
a=np.random.uniform(low=-100, high=100, size=(n,n))
b=np.random.uniform(low=-100, high=100, size=(n,n))
# print(a)
# print(b)
start = time.perf_counter()
c=fun(a,b,n)
# wrapped = wrapper(fun, a,b,n)
# print(timeit.timeit(wrapped))
end=time.perf_counter()
# print(c)
# print("Elapsed Time: " + str(end - start))
