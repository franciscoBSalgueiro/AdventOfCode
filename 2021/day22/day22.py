import re
from collections import Counter

with open("2021/day22/input.txt", "r") as file:
    linhas = file.read().splitlines()

def part1():
    cubos = Counter()
    for l in linhas:
        m = re.search("(.*) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", l)
        x = (int(m.group(2)), int(m.group(3)))
        y = (int(m.group(4)), int(m.group(5)))
        z = (int(m.group(6)), int(m.group(7)))
        if x[0]>50 or x[1]<-50 or y[0]>50 or y[1]<-50 or z[0]>50 or z[1]<-50:
            break
        for a in range(x[0],x[1]+1):
            for b in range(y[0],y[1]+1):
                for c in range(z[0],z[1]+1):
                    if m.group(1) == "on":
                        cubos[(a,b,c)] = 1
                    else:
                        cubos[(a,b,c)] = 0
    print(sum(x for x in cubos.values()))

def part2():
    def volume(cubo):
        x,y,z = cubo
        return (1+x[1]-x[0])*(1+y[1]-y[0])*(1+z[1]-z[0])

    def intersetam(cubo1,cubo2):
        x1, y1, z1 = cubo1
        x2, y2, z2 = cubo2
        return x2[0]<=x1[1] and x2[1]>=x1[0] and y2[0]<=y1[1] and y2[1]>=y1[0] and z2[0]<=z1[1] and z2[1]>=z1[0]

    def intersecao(cubo1, cubo2):
        x1, y1, z1 = cubo1
        x2, y2, z2 = cubo2
        return ((max(x1[0],x2[0]),min(x1[1],x2[1])),(max(y1[0],y2[0]),min(y1[1],y2[1])),(max(z1[0],z2[0]),min(z1[1],z2[1])))


    cubos = []
    for l in linhas:
        m = re.search("(.*) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", l)
        x = (int(m.group(2)), int(m.group(3)))
        y = (int(m.group(4)), int(m.group(5)))
        z = (int(m.group(6)), int(m.group(7)))
        
        cubo = (x,y,z)
        for c, v in cubos.copy():
            if intersetam(cubo,c):
                inter = intersecao(cubo,c)
                if v<0:
                    cubos.append((inter,1))
                else:
                    cubos.append((inter,-1))
        if m.group(1) == "on":
            cubos.append((cubo,1))

    print(sum(volume(x)*y for (x, y) in cubos))

part1()
part2()