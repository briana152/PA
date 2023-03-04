#Merealbe Cris-Briana,143
#s3 a)
def citire_date(fisier):
    f=open(fisier, "r")
    input=f.read()
    info=input.split("\n")
    cheie=info[0]
    mesaj={}
    for k in range(1, len(info)):
        msj = info[k].split(" ")
        mesaj.setdefault(msj[0], {}).setdefault(msj[1], msj[2])
    f.close()
    return cheie,mesaj
#s3 b)
def decodificare(cuvant, cheie):
    valori={}
    contor=0
    for i in range(ord('a'), ord('z') + 1):
        valori.setdefault(i, cheie[contor])
        contor += 1

    decod=""
    for litera in cuvant:
        for key, value in valori.items():
         if litera == value:
             decod+= chr(key)
    return decod
