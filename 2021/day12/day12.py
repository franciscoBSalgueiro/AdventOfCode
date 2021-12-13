with open("input.txt", "r") as file:
    linhas=file.read().split("\n")

caves = {}
for l in linhas:
    l = l.split("-")
    if l[1] != "start":
        if l[0] in caves.keys():
            caves[l[0]].append(l[1])
        else:
            caves[l[0]] = [l[1]]
    if l[0] != "start":
        if l[1] in caves.keys():
            caves[l[1]].append(l[0])
        else:
            caves[l[1]] = [l[0]]

def caminha(cave, part2=False):
    global total, caminho_str
    for saida in caves[cave]:
        if (not part2 and saida not in vistos) or (part2 and vistos.count(saida)<2 and (len(list(filter(lambda e: e.lower()==e and vistos.count(e)>=2, vistos)))/2)<2):
            caminho_str += cave +","
            if saida.lower() == saida and saida!="end":
                vistos.append(saida)
            if saida == "end":
                total+=1
            else:
                caminha(saida,part2)
                if saida.lower() == saida:
                    vistos.remove(saida)
                caminho_str=caminho_str[:-2]
    caminho_str=caminho_str[:-2]
vistos = []
caminho_str = ""
total=0
caminha("start")
print(total)
total=0
caminha("start",True)
print(total)