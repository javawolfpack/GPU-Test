
def fun(a,b,n):
    c=[]
    for i in range(n):
        c+=[a[i]+b[i]]
    return c

if len(sys.argv) < 2:
    print("Requires 1 argument, the number of elements in the array")
    quit()

a=[1,2,3,4]
b=[1,2,3,4]
c=fun(a,b,4)
print(c)
