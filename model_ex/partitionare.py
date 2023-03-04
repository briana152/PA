def citire_fisier(nume_fisier):
    lista_intervale_spectacole=[]
    with open(nume_fisier) as f:
        for linie in f:
            s, f=(int(x) for x in linie.strip().split())
            lista_intervale_spectacole.append([s,f])
    return lista_intervale_spectacole

ls=citire_fisier("intervale.in")
ls.sort()
print(ls)
def dictionare(liste):
    dict = {}
    dict[0]=[liste[0]]
    lista_sali=[0]
    lista_ultimi_timpi=[liste[0][1]]
    del liste[0]
    for i in range(0, len(liste)):
        ok=0
        for j in range(len(lista_ultimi_timpi)):
            if liste[i][0]>lista_ultimi_timpi[j]:
                ok=1
                lista_ultimi_timpi[j]=liste[i][1]
                dict[j].append(liste[i])
                break
        if ok==0:
            lista_ultimi_timpi.append(liste[i][1])
            lista_sali.append(j+1)
            dict[j+1]=[liste[i]]
    print(lista_sali)
    print(lista_ultimi_timpi)
    print(dict)
    return len(lista_sali)

x=dictionare(ls)
print(f"pentru a programa toate activitatile o sa avem nevoie de {x} sali")



