def citire_matrix(fisier):
    f = open(fisier, "r")
    lines = f.read().split("\n")
    matrix = []
    for i in lines:
        ls=[int(x) for x in i.split()]
        matrix.append(ls)
    lenght=len(matrix[0])
    for i in matrix:
        if len(i)!=lenght:
            return None
    return matrix

matrix=citire_matrix("date.in")

def multimi(matrix, *args):
    ls2=set()
    ls1_mare=[]
    c=0
    for arg in args:
        ls1=set()
        for x in matrix[arg]:
            if x<0:
                ls1.add(x)
            if x>0:
                c=str(x)
                c=int(c[0])
                if x%10==c:
                    ls2.add(x)
        for elem in ls1:
            ls1_mare.append(elem)
    multime=set()
    for elem in ls1_mare:
        if ls1_mare.count(elem)==len(args):
            multime.add(elem)
    return multime, ls2

nr=len(matrix)-1
negative, egale = multimi(matrix,nr,nr-1,nr-2)
print(sorted(egale))
negative2, egale2 = multimi(matrix,0,nr)
print(len(negative2))
