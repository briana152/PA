n=4
x=[0 for i in range(n)]
v=[0 for i in range(n+1)]
def back(k):
    if k==n:
        print(*x)
    else:
        for i in range(1,n+1):
            x[k]=i
            if v[x[k]]==0:
                v[x[k]]=1
                back(k+1)
                v[x[k]]=0

back(0)