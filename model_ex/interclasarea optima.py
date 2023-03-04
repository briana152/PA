#L1 = 20, L2 = 30, L3 = 20, L4 = 35
import re

def citire(fisier):
    ls=[]
    with open(fisier) as f:
        prop = re.split("[=, ]+", f.readline().strip("\n"))
        for x in prop:
            if x.isdigit():
                ls.append(int(x))
    return ls

lista_distante=citire("intervale.in")
print(lista_distante)
lista_distante.sort()
print(f"lista dupa sortare: {lista_distante}")
s_ultim=0
dist=0
rez=[]
m=len(lista_distante)
for i in range(0,len(lista_distante)+m,2):
    if len(lista_distante)-m==m-1:
        break
    s_ultim=lista_distante[i]+lista_distante[i+1]
    lista_distante.insert(len(lista_distante),s_ultim)
    rez.append(s_ultim)
s=0
for i in range(len(rez)):
    s+=rez[i]
print(s)