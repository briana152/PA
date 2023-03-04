#Merealbe Cris-Briana,143
#s2 a)
def citire_matrice(nume_fisier):
    inp = open(nume_fisier,"r")
    input = inp.read()
    lista = input.split('\n')

    m_n = lista[0].split(' ')
    m = m_n[0]
    n = m_n[1]

    elemente = lista[1].split(' ')


    if len(elemente) != int(m) * int(n):
        matrice = None
        return matrice
    else:
        index = 0
        index_f = int(n)
        matrice = []
        for i in range(0,int(m)):
            new_line = []
            for j in range(index,index_f):
                new_line.append(elemente[j])
            matrice.append(new_line)
            index = index + int(n)
            index_f = index_f + 2
    inp.close()
    return matrice
#s2 b)
def total(matrice,indici,tip):
    n = len(matrice[0])
    new_line = []
    for i in range(0,n):
        suma = 0
        for j in indici:
            suma += int(matrice[j][i])
        new_line.append(str(suma))

    if tip == 0:
        matrice.append(new_line)
    else:
        matrice[:0] = new_line

    return matrice
#s2 c)
def ultimul_spct():
    matrice = citire_matrice("matricemn.in")
    lg = len(matrice)
    matrice = total(matrice,[0,1],1)

    matrice = total(matrice, [lg-2,lg-1],0)
    return matrice

