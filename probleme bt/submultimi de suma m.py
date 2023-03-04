def back(k):
    s=0
    if k == n:
        # print(*x)
        for i in range(n):
            if x[i] == 1:
                s+=a[i]
        if s==m:
            print([a[i] for i in range(n) if x[i]==1])
    else:
        # dam valoare lui x[k]:
        for i in range(0, 2):
            x[k] = i
            back(k + 1)

a = [3 ,1, 7, 9]
m=10
n = len(a)
x = [0 for i in range(n)]
back(0)