with open("input.txt", "r") as file:
    nums=file.read().replace('\n','').split(",")

nums = list(map(int, nums))

def proximo_n(idades):
    n_idades = idades.copy()
    n_idades[8] = idades[0]
    n_idades[6] = idades[7] + idades[0]
    for i in range(8):
        if i == 6:
            continue
        n_idades[i] = idades[i+1]
    return n_idades

def n_apos_xgeracoes(geracoes):
    idades = [ nums.count(i) for i in range(9) ]
    for _ in range(geracoes):
        idades = proximo_n(idades)
    print(sum(idades))

# Part 1
n_apos_xgeracoes(80)

# Part 2
n_apos_xgeracoes(256)