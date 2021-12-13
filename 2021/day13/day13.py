with open("input.txt", "r") as file:
    linhas=file.readlines()

pontos = set()
folds = []

for l in linhas:
    if l != "\n":
        if "fold" in l:
            folds.append(l.replace("fold along ","").split("="))
        else:
            pontos.add(tuple(map(int,l.split(","))))

dim = ( max([p[0] for p in pontos]), max([p[1] for p in pontos]) )

def dobra(axis,n):
    global pontos, dim
    n_pontos = pontos.copy()
    for i, p in enumerate(pontos):
        if axis=="y":
            if p[1]>n:
                n_pontos.add((p[0],dim[1]-p[1]))
                n_pontos.remove(p)
            n_dim = (dim[0], (dim[1]+1)//2-1)
        if axis=="x":
            if p[0]>n:
                n_pontos.add((dim[0]-p[0],p[1]))
                n_pontos.remove(p)
            n_dim = ((dim[0]+1)//2-1, dim[1])
    pontos = n_pontos
    dim = n_dim

# Part 1
# dobra(folds[0][0],int(folds[0][1]))
# print(len(pontos))

# Part 2
for f in folds:
    dobra(f[0],int(f[1]))
for j in range(6):
    for i in range(40):
        if (i,j) in pontos:
            print("#",end="")
        else:
            print(".",end="")
    print()
