from itertools import combinations
import numpy as np

file = "input/2023/day11.txt"
# file = "src/examples/day11_example.txt"

with open(file) as f:
    lines = np.array([list(line.strip()) for line in f.readlines()])

empty_rows = []
for i in range(len(lines)):
    if np.all(lines[i] == "."):
        empty_rows.append(i)
empty_cols = []
for i in range(len(lines[0])):
    if np.all(lines[:, i] == "."):
        empty_cols.append(i)

galaxies = list(zip(*np.where(lines == "#")))


def between(x, y):
    if x < y:
        return range(x + 1, y)
    else:
        return range(y + 1, x)


def distance(x, y, empty_rows, empty_cols, n):
    y_dist = abs(x[0] - y[0])
    x_dist = abs(x[1] - y[1])

    y_dist += sum([1 for r in empty_rows if r in between(x[0], y[0])]) * (n - 1)
    x_dist += sum([1 for c in empty_cols if c in between(x[1], y[1])]) * (n - 1)

    return y_dist + x_dist


combs = list(combinations(galaxies, 2))

print(sum([distance(c[0], c[1], empty_rows, empty_cols, 1) for c in combs]))
print(sum([distance(c[0], c[1], empty_rows, empty_cols, 1000000) for c in combs]))
