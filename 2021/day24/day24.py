from collections import Counter

with open("2021/day24/input.txt", "r") as file:
    linhas = file.read().splitlines()

programa = ""
i=0
for l in linhas:
    l = l.split(" ")
    if l[0] == "inp":
        programa += f"{l[1]} = inputs[{i}]"
        i+=1
    if l[0] == "add":
        programa += f"{l[1]} += {l[2]}"
    if l[0] == "mul":
        programa += f"{l[1]} *= {l[2]}"
    if l[0] == "div":
        programa += f"{l[1]} //= {l[2]}"
    if l[0] == "mod":
        programa += f"{l[1]} %= {l[2]}"
    if l[0] == "eql":
        programa += f"int({l[1]} == {l[2]})"
    programa+="\n"

# print(programa)

def executa(inputs):
    x,y,z,w = 0,0,0,0
    w = inputs[0]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 10
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    w = inputs[1]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 9
    y *= x
    z += y
    w = inputs[2]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y
    w = inputs[3]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 4
    y *= x
    z += y
    w = inputs[4]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs[5]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -13
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs[6]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -9
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs[7]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -12
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 12
    y *= x
    z += y
    w = inputs[8]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 14
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs[9]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -9
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 14
    y *= x
    z += y
    w = inputs[10]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 15
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 5
    y *= x
    z += y
    w = inputs[11]
    x *= 0
    x += z
    x %= 26
    z //= 1
    x += 11
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 10
    y *= x
    z += y
    w = inputs[12]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -16
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 8
    y *= x
    z += y
    w = inputs[13]
    x *= 0
    x += z
    x %= 26
    z //= 26
    x += -2
    x = int(x == w)
    x = int(x == 0)
    y *= 0
    y += 25
    y *= x
    y += 1
    z *= y
    y *= 0
    y += w
    y += 15
    y *= x
    z += y
    return z

# Expressão simplificada no Mathematica
# para 3888 possibilidades

print(executa([9,9,9,1,9,6,9,2,4,9,6,9,3,9]))
print(executa([8,1,9,1,4,1,1,1,1,6,1,7,1,4]))