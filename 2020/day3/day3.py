with open("input.txt", "r") as file:
    linhas = file.readlines()

comp = len(linhas[0])-1

def slope_test(x,y):
    arvores=0
    px=0
    py=0
    while py<len(linhas)-1:
        px+=x
        py+=y
        value = linhas[py][px%comp]
        if value == "#":
            arvores+=1
    return arvores

# # Part1
print(slope_test(3,1))

# # Part2
print(slope_test(1,1)*slope_test(3,1)*slope_test(5,1)*slope_test(7,1)*slope_test(1,2))
