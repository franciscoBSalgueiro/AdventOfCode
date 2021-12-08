with open("input.txt", "r") as file:
    linhas=file.readlines()

# Part 1
numsfaceis = [0,0,0,0]
for l in linhas:
    l = l.split(" | ")
    nums4digits = l[1].replace("\n","").split(" ")
    for n in nums4digits:
        if len(n) == 2:
            numsfaceis[0]+=1
        elif len(n) == 4:
            numsfaceis[1]+=1
        elif len(n) == 3:
            numsfaceis[2]+=1
        elif len(n) == 7:
            numsfaceis[3]+=1
print(sum(numsfaceis))

# Part 2

def converte(digits4):
    convertor = {"abcefg":0,"cf":1,"acdeg":2,"acdfg":3,"bcdf":4,"abdfg":5,"abdefg":6,"acf":7,"abcdefg":8,"abcdfg":9}
    numero = ""
    for n in digits4:
        numero+=str(convertor[n])
    return int(numero)

def naocontem(x,y):
    """letras de x que não estão em y"""
    return "".join(list(filter(lambda x: x not in signaldigits[y],signaldigits[x])))

def comuns(x,y):
    return "".join(list(filter(lambda x: x in signaldigits[y],signaldigits[x])))

total=0
for l in linhas:
    signal_mapping = {}
    l = l.split(" | ")
    signaldigits = l[0].split(" ")
    nums4digits = l[1].replace("\n","").split(" ")
    signaldigits = sorted(list((map(lambda x: "".join(sorted(x)),signaldigits))), key = len)
    # A
    signal_mapping[naocontem(1,0)] = "a"
    # B e D
    possiveis = naocontem(2,0)
    for p in possiveis:
        
        com = [comuns(2,i) for i in [3,4,5]]
        if all(p in x for x in com):
            signal_mapping[p] = "d"
        else:
            signal_mapping[p] = "b"
    # C, F e G
    for i in range(3,6):
        if all(x in signaldigits[i] for x in signal_mapping.keys()):
            signal_mapping[naocontem(2,i)] = "c"
            signal_mapping[comuns(0,i)] = "f"
            for c in naocontem(i,1):
                if c not in signal_mapping.keys():
                    signal_mapping[c] = "g"
    # E
    for letra in ["a","b","c","d","e","f","g"]:
        if letra not in signal_mapping.keys():
            signal_mapping[letra] = "e"

    ######
    for i in range(4):
        nums4digits[i] = "".join(sorted(signal_mapping[nums4digits[i][j]] for j in range(len(nums4digits[i]))))
    total+=converte(nums4digits)
print(total)