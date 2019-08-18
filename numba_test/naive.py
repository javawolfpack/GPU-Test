import sys

def fun(a,b,n):
    c=[]
    for i in range(n):
        c+=[a[i]+b[i]]
    return c

if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

n=int(argv[1])
a=[random.uniform(-100,100) for _ in xrange(n)]
b=[random.uniform(-100,100) for _ in xrange(n)]
c=fun(a,b,n)
print(c)
