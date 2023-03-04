import re
f=open("spectacole.in")
g=open("programare.txt","w")
ls=[]
for linie in f:
    linie=re.split("[ -]",linie.strip("\n"))
    print(linie)
    linie=" ".join(linie)
    print(linie)
    x,y,nume=linie.split(" ",2)
    ls.append((x,y,nume))
print(ls)
ls=sorted(ls, key=lambda x:x[1])
print(ls)
anterior=ls[0][1]
g.write(str(ls[0][0]+"-"+ls[0][1]+" "+ls[0][2]))
g.write("\n")
for i in range(1, len(ls)):
    if ls[i][0]>anterior:
        g.write(str(ls[i][0]+"-"+ls[i][1]+" "+ls[i][2]))
        anterior=ls[i][1]
        g.write("\n")