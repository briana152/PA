def back(k):
    if k==m:
        print(*x)
    else:
        for i in range(1,n+1):
            x[k]=i
            if (k==0) or (x[k] > x[k-1]):
                back(k+1)
        """
        #putem da valori lui x[k]incepand cu x[k-1]+1
        if k==0:
            start=1
        else:
            start=x[k-1]+1
        for i in range(start, n + 1):
            x[k] = i
            back(k + 1)
        """

n=5
m=3
x=[0 for i in range(m)]
back(0)