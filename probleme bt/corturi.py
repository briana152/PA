def back(k):
    if k==m:
        if sum(x[i] for i in range(m))==n: # and x[0]==c[0]:
            print(*x)
    else:
        for i in range(1,max(c)+1):
            x[k]=i
            if x[k]<=c[k]:
                if sum(x[:k])<=n:
                    back(k+1)
n=9
m=3
c=[5,2,4]
x=[0 for i in range(m)]
#print(max(c))
back(0)