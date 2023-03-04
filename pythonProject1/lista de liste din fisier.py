def incarca_fisier(fisier):
    f = open(fisier, "r")
    lista_mare = []
    linie=f.readline()
    while linie !='':
        lista_linie=[int(x) for x in linie.split()]
        lista_mare.append(lista_linie)
        linie=f.readline()
    return lista_mare
    f.close()

print(incarca_fisier("date.in"))
