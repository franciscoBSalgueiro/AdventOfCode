from pprint import pprint
from copy import deepcopy

with open("2021/day25/input.txt", "r") as file:
    linhas = file.read().splitlines()

matriz = [[c for c in l] for l in linhas]

dim_x = len(matriz[0])
dim_y = len(matriz)

move = []

contador = 0
while True:
    contador += 1
    inicial = deepcopy(matriz)
    n_matriz = deepcopy(matriz)
    for i, l in enumerate(matriz):
        for j, c in enumerate(l):
            if c == "." or c == "v":
                continue
            elif c == ">":
                n_pos = (i,(j+1)%dim_x)
            if matriz[n_pos[0]][n_pos[1]] == ".":
                n_matriz[i][j] = "."
                n_matriz[n_pos[0]][n_pos[1]] = c
    matriz = n_matriz
    n_matriz = deepcopy(matriz)
    for i, l in enumerate(matriz):
        for j, c in enumerate(l):
            if c == "." or c == ">":
                continue
            elif c == "v":
                n_pos = ((i+1)%dim_y,j)
            if matriz[n_pos[0]][n_pos[1]] == ".":
                n_matriz[i][j] = "."
                n_matriz[n_pos[0]][n_pos[1]] = c
    matriz = n_matriz
    if matriz == inicial:
        print(contador)
        break
