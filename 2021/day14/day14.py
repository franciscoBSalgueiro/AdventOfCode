from collections import Counter

with open("input.txt", "r") as file:
    linhas=file.read().split("\n")

regras = {}

for l in linhas[2:]:
    l= l.split(" -> ")
    regras[l[0]] = l[1]

polimero = linhas[0]
pares = Counter()
contas = Counter()

for i in range(len(polimero)-1):
    par = polimero[i:i+2]
    pares[par] += 1
    contas[polimero[i]] += 1
contas[polimero[-1]] += 1

for k in range(40):
    n_pares = pares.copy()
    for par in pares:
        c = regras[par]
        v = pares[par]
        n_pares[par[0]+c] += v
        n_pares[c+par[1]] += v
        n_pares[par] -= v
        contas[c] += v
    pares= n_pares

print(max(contas.values())-min(contas.values()))