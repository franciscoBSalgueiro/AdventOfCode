with open("input.txt", "r") as file:
    linhas=file.readlines()

epsilon = ""
gamma = ""
for j in range(len(linhas[0])-1):
    valores = []
    for i, l in enumerate (linhas):
        valores.append(l[j])
    epsilon += str(int(valores.count("1")>valores.count("0")))
    gamma += str(int(not valores.count("1")>valores.count("0")))

print(int(epsilon, 2) * int(gamma, 2))

epsilon = ""
gamma = ""
terminou_c = False
terminou_o = False
for j in range(len(linhas[0])-1):
    valores = []
    valores_e = []
    for i, l in enumerate (linhas):
        if l.startswith(epsilon):
            valores_e.append(l[j])
        if l.startswith(gamma):
            valores.append(l[j])
    if not terminou_o:
        epsilon += str(int(valores_e.count("1")>=valores_e.count("0")))
    if not terminou_c:
        gamma += str(int(not valores.count("1")>=valores.count("0")))

    
    n=0
    m=0
    oxigen = 0
    c02 = 0
    
    for l in linhas:
        if l.startswith(epsilon):
            oxigen = l
            n+=1
        if l.startswith(gamma):
            c02 = l
            m+=1
    if n==1 and not terminou_o:
        final_oxigenio = int(oxigen,2)
        terminou_o = True
    if m==1 and not terminou_c:
        final_c02 = int(c02,2)
        terminou_c = True
print(final_c02*final_oxigenio)
