v=[1,5,10]
n=len(v)
x=[0 for i in range(n)]
s=20
suma=0
def back(k):
    global suma
    if k==n:
        if suma==s:
            print(*x)
    else:
        for i in range(s//v[k]+1):
            x[k]=i
            suma+=x[k]*v[k]
            if suma<=s:
                #print(*x[:k+1])
                back(k+1)
            suma-=x[k]*v[k]
back(0)
