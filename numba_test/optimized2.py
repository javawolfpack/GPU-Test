import sys
import numpy as np
from numba import cuda
import time
import math

#https://nyu-cds.github.io/python-numba/05-cuda/


# CUDA kernel
@cuda.jit
def matmul(A, B, C):
    """Perform matrix multiplication of C = A * B
    """
    row, col = cuda.grid(2)
    if row < C.shape[0] and col < C.shape[1]:
        tmp = 0.
        for k in range(A.shape[1]):
            tmp += A[row, k] * B[k, col]
        C[row, col] = tmp


if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(sys.argv[1])
n=n*16 #consistency with cuda3.py implementation
a=np.random.uniform(low=-100, high=100, size=(n,n)).astype(np.float32)
b=np.random.uniform(low=-100, high=100, size=(n,n)).astype(np.float32)
result = np.zeros((n,n), dtype=np.float32)

# Copy the arrays to the device
A_global_mem = cuda.to_device(a)
B_global_mem = cuda.to_device(b)
# Allocate memory on the device for the result
C_global_mem = cuda.to_device(result)

# Configure the blocks
threadsperblock = (16, 16)
blockspergrid_x = int(math.ceil(a.shape[0] / threadsperblock[0]))
blockspergrid_y = int(math.ceil(b.shape[1] / threadsperblock[1]))
blockspergrid = (blockspergrid_x, blockspergrid_y)
# Start the kernel
matmul[blockspergrid, threadsperblock](A_global_mem, B_global_mem, C_global_mem)

# Copy the result back to the host
C = C_global_mem.copy_to_host()

# print(C)
