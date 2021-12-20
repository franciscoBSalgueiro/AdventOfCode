with open("input.txt", "r") as file:
    linhas = file.read().splitlines()


transformador = linhas[0]

def add_estofo(t, c):
    novo_t = [c*(len(t[0])+4)]
    novo_t.append(c*(len(t[0])+4))
    for l in t:
        novo_t.append(2*c + l + 2*c)
    novo_t.append(c*(len(t[0])+4))
    novo_t.append(c*(len(t[0])+4))
    return novo_t

def cod_to_bin(cod):
    cod = cod.replace(".","0").replace("#","1")
    return int(cod,2)

mat = linhas[2:]

def enchance_image(img, c):
    estofo = add_estofo(img, c)
    novo_estofo = []
    for i in range(1,len(estofo)-1):
        nova_linha = ""
        for j in range(1,len(estofo[0])-1):
            codigo = estofo[i-1][j-1:j+2] + estofo[i][j-1:j+2] + estofo[i+1][j-1:j+2]
            codigo = cod_to_bin(codigo)
            nova_linha += transformador[codigo]
        novo_estofo.append(nova_linha)
    return novo_estofo

def count_pixels(img):
    tot = 0
    for l in img:
        tot += l.count("#")
    return tot

for i in range(50):
    if i%2 == 0:
        c="."
    else:
        c="#"
    mat = enchance_image(mat, c)
print(count_pixels(mat))