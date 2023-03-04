n=4
x=[0 for i in range(n)]
back(0)

def back(k):
    if k==n:
        print(*x)
    else:
        for i in range(1,10):