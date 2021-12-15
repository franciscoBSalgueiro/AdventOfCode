with open("input.txt", "r") as file:
    linhas=file.readlines()

for i, l in enumerate(linhas):
    linhas[i] = l.replace("\n","")


# PART 1
lowpoints = []
for i, l in enumerate(linhas):
    linhas[i] = l.replace("\n","")
    for j, c in enumerate(l):
        adiciona = True
        if i>0 and c>=linhas[i-1][j]:
            adiciona=False
        if j>0 and c>=linhas[i][j-1]:
            adiciona=False
        if i<(len(linhas)-1) and c>=linhas[i+1][j]:
            adiciona = False
        if j<(len(l)-1) and c>=linhas[i][j+1]:
            adiciona = False
        if adiciona:
            lowpoints.append(int(c))

tot=0
for p in lowpoints:
    tot+=(1+p)
print(tot)

# PART 2

def encontra_basin(i,j):
    if linhas[i][j] == "9" or (i,j) in vistos:
        return []
    vistos.append((i,j))
    final = [linhas[i][j]]
    if i>0 and (i-1,j) not in vistos and c<linhas[i-1][j] and linhas[i-1][j]!="9":
        final += encontra_basin(i-1,j)
    if j>0 and (i,j-1) not in vistos and c<linhas[i][j-1] and linhas[i][j-1]!="9":
        final += encontra_basin(i,j-1)
    if i<(len(linhas)-1) and(i+1,j) not in vistos  and c<linhas[i+1][j] and linhas[i+1][j]!="9":
        final += encontra_basin(i+1,j)
    if j<(len(l)-1) and (i,j+1) not in vistos and  c<linhas[i][j+1] and linhas[i][j+1]!="9":
        final += encontra_basin(i,j+1)
    return final

basins = []
vistos = []
for i, l in enumerate(linhas):
    linhas[i] = l.replace("\n","")
    for j, c in enumerate(l):
        adiciona = True
        if i>0 and c>=linhas[i-1][j]:
            adiciona=False
        if j>0 and c>=linhas[i][j-1]:
            adiciona=False
        if i<(len(linhas)-1) and c>=linhas[i+1][j]:
            adiciona = False
        if j<(len(l)-1) and c>=linhas[i][j+1]:
            adiciona = False
        if adiciona:
            basins.append(encontra_basin(i,j))

for i, b in enumerate(basins):
    basins[i] = len(b)
basins = sorted(basins)
print(basins[-1]*basins[-2]*basins[-3])