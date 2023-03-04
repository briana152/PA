#a
"""""
def note(*liste):
    dict = {}
    for l in liste:
        nr = 0
        for x in l:
            if x >= 5:
                nr += 1
        if dict.get(nr, 0) == 0:
            dict[nr] = [l]
        else:
            dict[nr].append(l)
    return dict

print(note([5, 4, 2, 7, 10], [6, 7, 8, 10, 3], [10, 7, 4, 10, 9], [5, 6, 8, 4, 1], [5, 5, 6, 10, 7, 9]))

#b
lista_cuvinte = ["acasa", "masa", "este", "scaun", "perete", "dulap"]
lista_sufixe = ["sa", "te"]
lista_rez = [ x for x in lista_cuvinte if x[len(x)-2:] in lista_sufixe]
print(lista_rez)
"""
""""
#a
def vocale(*cuvinte):
    voc="aeiou"
    dict = {}
    for cuv in cuvinte:
        nr = 0
        for i in cuv:
            if i in voc:
                nr += 1
        if dict.get(nr, 0) == 0:
            dict[nr] = [cuv]
        else:
            dict[nr].append(cuv)
    dict
    return dict
print(vocale("acasa", "masa", "scaun", "oaie", "oare"))

# b
lista_cuv = ["acasa", "masa", "este", "scaun"]
lista_rez = [i for i in lista_cuv if i[0]==i[len(i)-1]]
print(lista_rez)
"""
""""
def litere(*cuvinte):
    d={}
    vocale="aeiou"
    for cuv in cuvinte:
        lsv=[]
        lsc=[]
        for i in range(len(cuv)):
            if cuv[i] in vocale:
                lsv.append(cuv[i])
            else:
                lsc.append(cuv[i])
        d[cuv]=(set(lsv),set(lsc))
    return d

print(litere("teste","programare"))
"""