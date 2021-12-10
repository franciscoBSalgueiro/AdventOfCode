with open("input.txt", "r") as file:
    linhas=file.readlines()


erros = {")": 3, "]":57,"}":1197,">":25137}
erro = 0
completar = {"(":1,"[":2,"{":3,"<":4}

inicios =  ["(","[","{","<"]
finais = [")","]","}",">"]

score = []
for l in linhas:
    comecaram = []
    pontos = 0
    # Part 1
    for i, c in enumerate(l):
        if c in inicios:
            comecaram.append(c)
        elif c in finais:
            if inicios.index(comecaram[-1]) == finais.index(c):
                comecaram.pop()
            else:
                erro += erros[c]
                break
    # Part 2
    else:
        if len(comecaram)!=0:
            for e in comecaram[::-1]:
                pontos = pontos * 5 + completar[e]
        score.append(pontos)

print(erro)

score = sorted(score)
print(score[len(score)//2])