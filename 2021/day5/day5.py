with open("input.txt", "r") as file:
    linhas=file.readlines()

from pprint import pprint
def reads_line(l):
    l = l.replace("\n","").replace(" ","").split("->")
    for i, e in enumerate(l):
        l[i]= e.split(",")
    return l

def percorre(p1,p2,dia=False):
    adicionou = False
    for k in range(2):
        if p1[k]==p2[k]:
            adicionou = True
            z1,z2=int(p1[1-k]),int(p2[1-k])
            sentido = int(z1<z2)*2-1
            z2+=sentido
            for i in range(z1,z2,sentido):
                if k == 0:
                    pn = (p1[k],str(i))
                else:
                    pn = (str(i),p1[k])
                if pn in vistos:
                    vistos[pn] += 1
                else:
                    vistos[pn] = 1
    if dia and not adicionou:
        if p1[0]>p2[0]:
            p1, p2 = p2, p1
        j=0
        for i in range(int(p1[0]),int(p2[0])+1):
            i = str(i)
            if p2[1]>p1[1]:
                pn = (i,str(int(p1[1])+j))
            else:
                pn = (i,str(int(p1[1])-j))
            if pn in vistos:
                vistos[pn] += 1
            else:
                vistos[pn] = 1
            j+=1
    

def conta():
    tot = 0
    for p in vistos:
        if vistos[p] >= 2:
            tot+=1
    print(tot)

# Part 1
vistos = {}
for l in linhas:
    [p1, p2] = reads_line(l)
    percorre(p1, p2)

conta()

#conta()
def print_campo():
    for i in range(10):
        for j in range(10):
            p = (str(j),str(i))
            if p in vistos:
                print(vistos[p],end=" ")
            else:
                print(".",end=" ")
        print("\n")

# Part 2
vistos = {}
for l in linhas:
    [p1, p2] = reads_line(l)
    percorre(p1, p2, True)

conta()

