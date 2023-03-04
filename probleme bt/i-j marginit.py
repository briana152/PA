def valid(k):
    return v[k] not in v[:k]

def solutie(k):
    return k <= j-i+1
def back(k):
    for x in range(i,j+1):
        v[k] = x
        if valid(k):
            if solutie(k):
                print(*v[:k+1])
                back(k+1)
            else:
                back(k+1)

i = int(input("i="))
j = int(input("j="))
v = [0 for i in range(j-i+2)]
print(v)
back(0)