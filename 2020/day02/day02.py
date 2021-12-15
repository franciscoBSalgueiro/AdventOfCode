with open("input.txt", "r") as file:
    linhas=file.readlines()

for i, l in enumerate (linhas):
    linhas[i] = l.replace(":","").split()

# Part1
tot=0
for l in linhas:
    (x,y) = tuple(map(int, l [0].split("-")))
    if x<=l[2].count(l[1])<=y:
        tot+=1
print(tot)

# Part2
tot=0
for l in linhas:
    (x,y) = tuple(map(int, l [0].split("-")))
    if (l[2][x-1]==l[1]) != (l[2][y-1] == l[1]):
        tot+=1
print(tot)