f=open("intervale.in")
l_activ=[]
n=int(f.readline())
for i in range(n):
    activ=[int(x) for x in f.readline().split()]
    l_activ.append(activ+[i+1])
print(l_activ)
f.close()
l_activ.sort(key=lambda x:x[1]) #dupa termenul limita
print(l_activ)
t_inceput=0
P=0 #intarzierea maxima
for li,ti,i in l_activ:
    t_final=t_inceput+li
    print(f"Activitatea {i} - intervalul [{t_inceput},{t_final})")
    pi = max(0,t_final-ti)
    P=max(pi,P)
    t_inceput=t_final

print(f"Intarziere planificare: {P}")