from copy import deepcopy


file = "input/2023/day13.txt"
# file = "src/examples/day13_example.txt"

with open(file) as f:
    input = f.read()

groups = input.split("\n\n")

total = 0

for g in groups:
    old_matrix = [list(r) for r in g.split("\n") if r != ""]
    matrix = old_matrix
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
    original_on_row = on_row
    original_on_col = on_col

    total_matches = 0
    total_on_row = None
    total_on_col = None
    # print(old_matrix)
    for x in range(len(old_matrix)):
        for y in range(len(old_matrix[x])):
            matrix = deepcopy(old_matrix)
            if matrix[x][y] == ".":
                matrix[x][y] = "#"
            else:
                matrix[x][y] = "."

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
                if m > matches and (m == i + 1 or m == len(matrix) - i - 1) and i != original_on_row:
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
                if m > matches and (m == i + 1 or m == len(transposed) - i - 1) and i != original_on_col:
                    matches = m
                    on_col = i
                    on_row = None

            if on_row is not None:
                if total_matches < matches:
                    total_matches = matches
                    total_on_row = on_row
                    total_on_col = None
            elif on_col is not None:
                if total_matches < matches:
                    total_matches = matches
                    total_on_row = None
                    total_on_col = on_col
            # else:
            #     print("ERROR on\n", g)
    if total_on_row is not None:
        print("row", total_on_row + 1)
        total += (total_on_row + 1) * 100
    elif total_on_col is not None:
        print("col", total_on_col + 1)
        total += total_on_col + 1
print(total)
