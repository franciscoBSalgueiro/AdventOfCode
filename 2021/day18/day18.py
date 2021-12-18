from math import ceil

with open("input.txt", "r") as file:
    linhas = file.read().split("\n")

nums = list(eval(l) for l in linhas)


def split_fish(n):
    return [n // 2, ceil(n / 2)]

def deep_flatten(x):
    if isinstance(x, list):
        return [a for i in x for a in deep_flatten(i)]
    else:
        return [x]


def explode_flat(l, n):
    if n > 0:
        l[n - 1] += l[n]
    if n + 2 < len(l):
        l[n + 2] += l[n + 1]
    l[n] = 0
    del l[n + 1]


def explode(l, n):
    flat_nums = deep_flatten(l)
    explode_flat(flat_nums, n)
    out_str = ""
    i = -1
    l = str(l)
    num = ""
    for j, c in enumerate(l):
        if c.isnumeric():
            if num == "":
                i += 1
            num += c
        if c == " " or c ==",":
            if i == n:
                l = l[: j - 1- len(num)] + "0" + l[j+2+l[j+1:].index("]"):]
                break
            num = ""
    i = -1
    num = ""
    for j, c in enumerate(l):
        if c == " " or c==",":
            num = ""
        if c.isnumeric():
            if num=="":
                i+=1
            num += c
            if not l[j+1].isnumeric():
                out_str += str(flat_nums[i])
        else:
            out_str += c
    return out_str


def percorre(l):
    l = str(l)
    modo = 0
    out = ""
    while True:
        nested = 0
        i = -1
        num = ""
        for j, c in enumerate(l):
            if c == "[":
                nested += 1
            elif c == "]":
                nested -= 1
            elif c == " ":
                num = ""
            elif c.isnumeric():
                if num== "":
                    i += 1
                num += c
                if int(num) >= 10 and modo == 1:
                    l = l[:j-1] + str(split_fish(int(num))) + l[j + 1 :]
                    modo=0
                    break
            elif c == "," and nested >= 5 and l[j - 1].isnumeric() and l[j + 2].isnumeric() and modo == 0:
                l = explode(eval(l), i )
                break
        else:
            modo = 1
            if out == l:
                break
            else:
                out = l
    return eval(out)

novo = nums[0]
for i in range(1,len(nums)):
    novo = percorre([novo,nums[i]])

total = 0
def calcula(l):
    if isinstance(l, int):
        return l
    return 3*calcula(l[0]) + 2*calcula(l[1])
print(calcula(novo))

maximo = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i!=j:
            valor = calcula(percorre([nums[i],nums[j]]))
            maximo = max(maximo,valor)

print(maximo)