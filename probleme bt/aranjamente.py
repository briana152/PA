def back2(k):
    if k == m:
        print(*x)
        print([elevi[x[i]-1] for i in range(m)])
    else:
        for i in range(1, n + 1):
            x[k] = i
            if v[x[k]]==0:
                v[x[k]]  = 1
                back2(k + 1)
                v[x[k]] = 0



n = 4
elevi=["Ion","Ioana","Mihai","Mihaela"]
m=3
x = [0 for i in range(m)]
v = [0 for i in range(n+1)]
back2(0)