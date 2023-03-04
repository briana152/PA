n=int(input("n= "))
h=int(input("m= "))
ls1=[]
ls2=[]
for i in range(n):
    ls1= input().split()
    ls2.append(ls1)
for i in range(len(ls2)):
    ls2[i][2]=int(ls2[i][2])
ls2.sort(key=lambda x:x[-1])
print(ls2)
nr=0
rez=[]
for i in range(len(ls2)):
    if ls2[i]==0:
        pass
    elif ls2[i+1][2]-ls2[i][2]<=h:
        nr+=1
        rez.append(ls2[i][0]+" "+ls2[i][1]+","+ls2[i+1][0]+" "+ls2[i+1][1])
        ls2[i]=0
        ls2[i+1]=0
if nr!=0:
    print(nr)
    print(rez)
else:
    print("-1")
