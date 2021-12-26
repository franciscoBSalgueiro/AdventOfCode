import random

with open("2021/day19/input.txt", "r") as file:
    linhas = file.read().splitlines()

scanners = []
i = 0
for l in linhas:
    if l == "":
        continue
    elif "scanner" in l:
        scanners.append([])
        i += 1
    else:
        l = list(map(int,l.split(",")))
        scanners[i-1].append(l)

def roda(scanner,n):
    scanner_rodado=[]
    for v in scanner:
        if n==0:
            w=[v[0],v[1],v[2]]
        elif n==1:
            w=[v[0],-v[1],-v[2]]
        elif n==2:
            w=[-v[0],v[1],-v[2]]
        elif n==3:
            w=[-v[0],-v[1],v[2]]
        elif n==4:
            w=[v[1],v[2],v[0]]
        elif n==5:
            w=[v[1],-v[2],-v[0]]
        elif n==6:
            w=[-v[1],v[2],-v[0]]
        elif n==7:
            w=[-v[1],-v[2],v[0]]
        elif n==8:
            w=[v[2],v[0],v[1]]
        elif n==9:
            w=[v[2],-v[0],-v[1]]
        elif n==10:
            w=[-v[2],v[0],-v[1]]
        elif n==11:
            w=[-v[2],-v[0],v[1]]
        elif n==12:
            w=[v[0],v[2],-v[1]]
        elif n==13:
            w=[v[0],-v[2],v[1]]
        elif n==14:
            w=[-v[0],v[2],v[1]]
        elif n==15:
            w=[-v[0],-v[2],-v[1]]
        elif n==16:
            w=[v[2],v[1],-v[0]]
        elif n==17:
            w=[v[2],-v[1],v[0]]
        elif n==18:
            w=[-v[2],v[1],v[0]]
        elif n==19:
            w=[-v[2],-v[1],-v[0]]
        elif n==20:
            w=[v[1],v[0],-v[2]]
        elif n==21:
            w=[v[1],-v[0],v[2]]
        elif n==22:
            w=[-v[1],v[0],v[2]]
        elif n==23:
            w=[-v[1],-v[0],-v[2]]
        scanner_rodado.append(w)
    return(scanner_rodado)

def ajusta(scanner,i,j):
    difx=mapa[i][0]-scanner[j][0]
    dify=mapa[i][1]-scanner[j][1]
    difz=mapa[i][2]-scanner[j][2]
    novo=[]
    for v in scanner:
        novo.append([v[0]+difx,v[1]+dify,v[2]+difz])
    return [difx,dify,difz,novo]

def compativel(s1,s2):
    comp=True
    comuns=0
    minx=max(s1[0],s2[0])-1000
    maxx=min(s1[0],s2[0])+1000
    miny=max(s1[1],s2[1])-1000
    maxy=min(s1[1],s2[1])+1000
    minz=max(s1[2],s2[2])-1000
    maxz=min(s1[2],s2[2])+1000
    if (minx<=maxx) and (miny<=maxy) and (minz<=maxz):
        dentro1=[]
        for v in s1[3]:
            if (minx<=v[0]<=maxx) and (miny<=v[1]<=maxy) and (minz<=v[2]<=maxz):
                dentro1.append(v)
        dentro2=[]
        for v in s2[3]:
            if (minx<=v[0]<=maxx) and (miny<=v[1]<=maxy) and (minz<=v[2]<=maxz):
                dentro2.append(v)
        comuns=len(dentro1)
        comp=(len(dentro1)==len(dentro2))
        for v in dentro1:
            comp=comp and (v in dentro2)
    return comp,comuns

def aumenta_mapa(novo):
    for v in novo[3]:
        if not(v in mapa):
            mapa.append(v)

n_scanners=len(scanners)

orientados=[]
orientados.append([0,0,0,scanners.pop(0)])
mapa=orientados[0][3]
faltam=n_scanners-1
for faltam in range(n_scanners-1,0,-1):
    print("Mapa com",len(mapa),"beacons")
    print("Falta orientar",faltam,"scanners")
    orientado=False
    while not orientado:
        n=random.randint(0,faltam-1)
        scanner=roda(scanners[n],random.randint(0,23))
        i=random.randint(0,len(mapa)-1)
        j=random.randint(0,len(scanner)-1)
        novo=ajusta(scanner,i,j)
        possivel=True
        comuns12=False
        for s in orientados:
            possivel,comuns=compativel(novo,s)
            if comuns>=12:
                comuns12=True
            if not possivel:
                break
        if possivel and comuns12:
            orientados.append(novo)
            aumenta_mapa(novo)
            del scanners[n]
            orientado=True

print("Mapa com",len(mapa),"beacons")
dist=[]
for s1 in orientados:
    for s2 in orientados:
        dist.append(abs(s1[0]-s2[0])+abs(s1[1]-s2[1])+abs(s1[2]-s2[2]))
print(max(dist))