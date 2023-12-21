file = "input/2023/day21.txt"
# file = "src/examples/day21_example.txt"

with open(file) as f:
    lines = f.readlines()

lines = [list(line.strip()) for line in lines]

x_size = len(lines)
y_size = len(lines[0])


def adjacent_cells(x, y):
    adj = []
    if lines[(x - 1) % x_size][y % y_size] != "#":
        adj.append((x - 1, y))
    if lines[x % x_size][(y - 1) % y_size] != "#":
        adj.append((x, y - 1))
    if lines[(x + 1) % x_size][y % y_size] != "#":
        adj.append((x + 1, y))
    if lines[x % x_size][(y + 1) % y_size] != "#":
        adj.append((x, y + 1))
    return adj


for i in range(len(lines)):
    for j in range(len(lines)):
        if lines[i][j] == "S":
            start = (i, j)
            break

positions = set([start])
prev = 0

for i in range(64):
    new_positions = set()
    for pos in positions:
        adj = adjacent_cells(*pos)
        new_positions.update(adj)
    positions = new_positions
    # For part 2
    if i % x_size == 65:
        print(i, len(positions) - prev, len(positions))
        prev = len(positions)

print(len(positions))

# https://www.wolframalpha.com/widgets/view.jsp?id=d9976f1c2c0c972d1cee0c3647cbd194

# 65 3742
# 196 33564
# 327 93148
# 458 182494

# 3682 - 14821 n + 14881 n^2


def pattern(n):
    return 3682 - 14821 * n + 14881 * n**2


print(pattern((26501365 // 131) + 1))
