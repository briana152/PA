print("mesaj")
x = 1
print("x=",x, type(x), id(x)) #pe acelasirandcu spatiu, apoi linie noua
print("x=" + str(x))
x = "Sir"
print("x=", x, type(x), id(x)) #nu are acelasi id
y = 2
print(x, end=' ') #pentru a nu trece la linie noua modific parametrul end
print(y)
print(x, y, sep='*')
