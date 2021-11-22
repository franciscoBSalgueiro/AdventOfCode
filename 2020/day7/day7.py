with open("input.txt", "r") as file:
    lines = file.readlines()

def read_line(line):
    line = line.replace("bags","").replace("\n","").replace("bag","").replace(".","").replace(" ","")
    line = ''.join([i for i in line])
    line = line.split("contain")
    line[1] = line[1].split(",")
    for i, e in enumerate(line[1]):
        if e == "noother":
            line[1][i] = (0, e)
        else:
            line[1][i] = (int(e[0]), e[1:])
    return line[0], line[1]


# Part 1

goodies = ['shinygold']

for i in range(30):
    for l in reversed(lines):
        container, cargo = read_line(l)
        for c in cargo:
            for g in goodies:
                if c[1] == g:
                    if container not in goodies:
                        goodies.append(container)

goodies.remove("shinygold")
print(len(goodies))

# Part 2

total = 0

a_ver = [('shinygold',1)]

while a_ver != []:
    for l in lines:
        container, cargo = read_line(l)
        if container == a_ver[0][0]:
            for c in cargo:
                total += c[0]*a_ver[0][1]
                if c[0] != 0:
                    a_ver.append((c[1],a_ver[0][1]*c[0]))
            a_ver.remove(a_ver[0])
            break

print(total)