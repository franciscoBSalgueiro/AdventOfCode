file = "input/2023/day13.txt"
# file = "src/examples/day13_example.txt"

with open(file) as f:
    input = f.read()

groups = input.split("\n\n")

total = 0

for x, g in enumerate(groups):
    matrix = [list(r) for r in g.split("\n") if r != ""]
    transposed = list(zip(*matrix))

    matches = 0
    on_row = None
    on_col = None

    for i in range(0, len(matrix) - 1):
        m = 0
        for j in range(i + 1):
            if i + 1 + j >= len(matrix):
                break
            if matrix[i - j] == matrix[i + 1 + j]:
                m += 1
            else:
                break
        if m > matches and (m == i + 1 or m == len(matrix) - i - 1):
            matches = m
            on_row = i

    for i in range(0, len(transposed) - 1):
        m = 0
        for j in range(i + 1):
            if i + 1 + j >= len(transposed):
                break
            if transposed[i - j] == transposed[i + 1 + j]:
                m += 1
            else:
                break
        if m > matches and (m == i + 1 or m == len(transposed) - i - 1):
            matches = m
            on_col = i
            on_row = None

    if on_row is not None:
        total += (on_row + 1) * 100
    elif on_col is not None:
        total += on_col + 1
    else:
        print("ERROR on\n", g)

print(total)
