#daca nu specificam key -criteriu implicit <=:
ls=[[7,8], [2,3,12], [4,7], [4,5] ]
ls1=sorted(ls)
print(ls) #nu s-a modificat
print (ls1)

ls=sorted("cuvant",reverse=False)
print(ls)

ls=["cuvant","xabc","cabc","altul"]

ls1=sorted(ls,key=lambda x:x[-1])
print(ls1)
def cheie_suma(t):
    return t[0]+t[1]

ls=[(3,21),(5,7),(10,1),(5,8),(6,6)]

ls1=sorted(ls, reverse = True, key = cheie_suma)
print(ls1)

x=int (input("x="))
x1=x.s[::-1]