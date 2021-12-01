with open("input.txt", "r") as file:
    linhas=file.readlines()


# Part 1

tot = 0
atual = 0
for i, l in enumerate (linhas):
    if int(l)>int(atual):
            tot+=1
    atual = int(l)

print(tot-1)

# Part 2
tot = 0
atual = 0
for i, l in enumerate (linhas):
    if i>2:
        if int(linhas[i-2])+int(linhas[i-1])+int(linhas[i])>int(atual):
            tot+=1
        atual = int(linhas[i-2])+int(linhas[i-1])+int(linhas[i])

print(tot)
    
