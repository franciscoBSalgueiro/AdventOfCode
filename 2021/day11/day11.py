from pprint import  pprint
with open("input.txt", "r") as file:
    linhas=file.read().split("\n")

matriz = [[int(c) for c in l] for l in linhas]

explosao = 0

g=0
while True:
    g+=1
    l_explosao = 0
    for i, l in enumerate(matriz):
        for j, energia in enumerate(l):
            l[j] += 1
    for x in range(100):
        for i, l in enumerate(matriz):
            for j, energia in enumerate(l):
                if l[j] > 9:
                    l[j] = -100
                    explosao += 1
                    l_explosao +=1
                    if i>0:
                        matriz[i-1][j] += 1
                        if j>0:
                            matriz[i-1][j-1] += 1
                        if j<len(l)-1:
                            matriz[i-1][j+1] += 1
                    if j>0:
                            matriz[i][j-1] += 1
                    if j<len(l)-1:
                            matriz[i][j+1] += 1
                    if i<len(matriz)-1:
                        matriz[i+1][j] += 1
                        if j>0:
                            matriz[i+1][j-1] += 1
                        if j<len(l)-1:
                            matriz[i+1][j+1] += 1
    for i, l in enumerate(matriz):
        for j, energia in enumerate(l):
            if energia<0:
                l[j] = 0
    if g == 100:
        print(explosao)
    if sum((sum(l) for l in matriz))==0:
        print(g)
        break