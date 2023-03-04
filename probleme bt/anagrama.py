def back(k):
    if k==n:
        #print(*x)
        print([ls[x[i] - 1] for i in range(n)])
    else:
        for i in range(1,n+1):
            x[k]=i
            if v[x[k]]==0:
                v[x[k]]=1
                back(k+1)
                v[x[k]]=0
n="abcd"
ls=[]
for i in range(len(n)):
    ls.append(n[i])
n=len(ls)
x=[0 for i in range(n)]
v=[0 for i in range(n+1)]
back(0)