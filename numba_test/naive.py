
def fun(a,b,n):
    c=[]
    for i in range(n):
        c+=[a[i]+b[i]]
    return c


a=[1,2,3,4]
b=[1,2,3,4]
c=fun(a,b,4)
print(c)
