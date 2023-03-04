#cu doua liste:
A=[3,-2,5,-1,4]
B=[7,8,-5,2,-4,-1,5]
A.sort()
B.sort()
p=0
rez=[]
A.insert(0,0)
B.insert(0,0)
#print(A,B)
for i in range(1,min(len(A),len(B))):
    if A[-i]>0 and B[-i]>0:
        p=p+A[-i]*B[-i]
        rez.append(A[-i]);rez.append(B[-i])
        
    elif (A[-i]<0 and B[-i]>0) or (A[-i]>0 and B[-i]<0):
        break

    if A[i] < 0 and B[i] < 0:
        p = p + A[i] * B[i]
        rez.append(A[i]);rez.append(B[i])

    elif (A[i]<0 and B[i]>0) or (A[i]>0 and B[i]<0):
        break

print(p,rez,end="\n")