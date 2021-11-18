from random import sample
from functools import reduce

with open("input.txt", "r") as file:
    l = list(map(int,file.readlines()))

def sum_finder(l,x,n):
    soma=0
    while soma!=n:
        lista = sample (l, x)
        soma=sum(lista)
    return lista

def multiply(l):
    return reduce(lambda x,y: x*y, l)

# Part1
print(multiply(sum_finder(l,2,2020)))

# Part2
print(multiply(sum_finder(l,3,2020)))