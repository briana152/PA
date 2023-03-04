ls=[3,-2,5,-1,4,-7,6,-3]
r=4
ls.sort()
print(ls)
ok=0
for i in range(len(ls)):
    if ls[i]>0 and r>0 and ok==0:
        ok=1
        if ls[i]<ls[i-1]:
            index=i
        else:
            index=i-1
    if ls[i]<0 and r>0:
        ls[i]=-ls[i]
        r-=1
if r%2==1:
    ls[index]=-ls[index]
print(ls)
print(sum(ls[i] for i in range(len(ls))))