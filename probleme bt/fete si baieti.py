n=3
fete=[i for i in range(1,n+1)]
m=2
baieti=[i for i in range(n+1,n+m+1)]
p=3
x=[0 for i in range(p)]

def back(k):
    if k==p:
        bok=0
        fok=0
        print(*x[:k])
        for i in x:
            if i in fete:
                fok=1
            else:
                bok=1
        if fok==1 and bok==1:
            print(*x)
    else:
        if k==0:
            start = 1
        else:
            start = x[k - 1] + 1
        for i in range(start,n+m+1):
            x[k]=i
            back(k+1)
back(0)