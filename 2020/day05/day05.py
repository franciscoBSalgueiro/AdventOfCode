with open("input.txt", "r") as file:
    linhas = file.readlines()

from functools import reduce

def binario(n):
    return reduce(lambda x,y: 2*x + y, n)

def encontra_lugar(s):
    lr = [1 if c=="B" else 0 for c in s[:7]]
    r = binario(lr)
    lc = [1 if c=="R" else 0 for c in s[7:]]
    c = binario(lc)
    return 8*r+c

# Part1
lista_ids = [encontra_lugar(l.replace("\n","")) for l in linhas]
print(max(lista_ids))

# Part2
for r in range(1,127):
    for c in range(0,8):
        lugar = 8*r+c
        if lugar not in lista_ids and lugar+1 in lista_ids and lugar-1 in lista_ids:
            print(lugar)
