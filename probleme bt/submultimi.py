def back(k):
    ls=[]
    if k==n:
        #print(*x)
        #if sum(x[i] for i in range(n)) == m:
            print([a[i] for i in range(n) if x[i]==1])
    else:
        #dam valoare lui x[k]:
        for i in range(0,2):
            x[k]=i
            #if sum(x[i] for i in range(n)) <= m:
            back(k+1)

a=[3,1,7,9]
n=len(a)
m=3
x=[0 for i in range(n)]
back(0)