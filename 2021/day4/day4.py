with open("input.txt", "r") as file:
    linhas=file.readlines()

nums = linhas[0].replace("\n","").split(",")

boards = []

for i, l in enumerate(linhas):
    if l == "\n":
        boards.append([])
    elif i>0:
        boards[-1].append(l.replace("  "," ").replace("\n","").split(" "))

for b in boards:
    for row in b:
        if "" in row:
            row.remove("")

def wins(v, b):
    for row in b:
        if all(e in v for e in row):
            return True
    for j in range(len(b)):
        if all(b[i][j] in v for i in range(len(b))):
            return True
    return False

# Part 1
for i, n in enumerate(nums):
    for b in boards:
        if wins(nums[:i+1],b):
            tot = 0
            for row in b:
                for v in row:
                    if v not in nums[:i+1]:
                        tot += int(v)
            tot*=int(n)
            print(tot)
            break
    else:
        continue
    break

# Part 2
won = 0
n_boards = len(boards)
boards_won = []
while True:
    for i, n in enumerate(nums):
        for b in boards:
            if wins(nums[:i+1],b):
                if b not in boards_won:
                    won+=1
                if won==n_boards and b not in boards_won:
                    tot = 0
                    for row in b:
                        for v in row:
                            if v not in nums[:i+1]:
                                tot += int(v)
                    tot*=int(n)
                    print(tot)
                    break
                if b not in boards_won:
                    boards_won.append(b)
        else:
            continue
        break
    else:
        continue
    break