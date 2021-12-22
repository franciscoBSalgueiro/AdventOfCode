from functools import cache

with open("2021/day21/input.txt", "r") as file:
    linhas = file.read().splitlines()
casa = [int(e[-1]) for e in linhas]
pontos = [0, 0]
jogador1 = False

# Part 1
j = 0
contador_dado = 0
while True:
    for i in range(1, 101):
        contador_dado += 1
        casa[int(jogador1)] = ((casa[int(jogador1)] + i - 1) % 10) + 1

        j += 1
        if j == 3:
            pontos[int(jogador1)] += casa[int(jogador1)]
            if pontos[int(jogador1)] >= 1000:
                print(contador_dado * pontos[int(not jogador1)])
                break
            j = 0
            jogador1 = not jogador1
    else:
        continue
    break

# Part 2
casa = [int(e[-1]) for e in linhas]
poss_dados = []
for a in range(3):
    for b in range(3):
        for c in range(3):
            poss_dados.append(a + b + c + 3)

@cache
def ganha(pos1, pos2, pontos1, pontos2, jogada):
    if pontos1 >= 21:
        return 1
    elif pontos2>=21:
        return 0

    vitorias = 0
    for l in poss_dados:
        n_pos1, n_pos2 = pos1, pos2
        n_pontos1, n_pontos2 = pontos1, pontos2
        if jogada == 0:
            n_pos1 = ((pos1 + l - 1) % 10) + 1
            n_pontos1 += n_pos1
        if jogada == 1:
            n_pos2 = ((pos2 + l - 1) % 10) + 1
            n_pontos2 += n_pos2
        vitorias += ganha(n_pos1, n_pos2, n_pontos1, n_pontos2, int(jogada==0))
    return vitorias

print(ganha(casa[0],casa[1], 0, 0, 0))
