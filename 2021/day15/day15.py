from dijkstar import Graph, find_path
from pprint import pprint

with open("input.txt", "r") as file:
    linhas=file.read().split("\n")

dim = len(linhas)

caves_exp = [[0 for _ in range(5*dim)] for _ in range(5*dim)]

for y in range(5):
    for x in range(5):
        for i, l in enumerate(linhas):
            for j, c in enumerate(l):
                caves_exp[dim*y+i][dim*x+j] = (int(c)+x+y-1)%9+1

linhas = caves_exp

dim = len(linhas)

g = Graph()

for i, l in enumerate(linhas):
    for j, c in enumerate(l):
        if i>0:
            g.add_edge(dim*(i-1)+j,dim*i+j,int(c))
        if j>0:
            g.add_edge(dim*(i)+j-1,dim*i+j,int(c))

print(find_path(g,0,dim**2-1).total_cost)