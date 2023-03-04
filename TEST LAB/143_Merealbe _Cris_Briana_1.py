#Merealbe Cris-Briana,143
#s1
dictionar={}
fin=open("text.in","r")
fout=open("text.out","w")
nr=0
ls=[]
lista=[]
multime=[]
lines=fin.readlines()
for line in lines:
    line_splited = line.strip(".,:;\n").split()
    ls+=line_splited
    line=fin.readline()
for i in range(len(ls)):
    nr=ls.count(ls[i])
    dictionar.setdefault(nr, []).append(ls[i])
print(dictionar)
fin.close()
fout.close()
