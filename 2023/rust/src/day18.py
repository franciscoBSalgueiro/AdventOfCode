file = "input/2023/day18.txt"
# file = "src/examples/day18_example.txt"

with open(file) as f:
    lines = f.readlines()

dig_plan = []
for line in lines:
    [dir, n, color] = line.split()
    n = int(n)
    color = color.replace("(#", "").replace(")", "")
    dig_plan.append((dir, n, color))


def polygon_area(poly):
    area = 0
    for i in range(len(poly)):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % len(poly)]
        area += x1 * y2 - x2 * y1

    return abs(area) / 2


def calculate_area(vertices, contourn):
    # A = i + b/2 - 1
    A = polygon_area(vertices)
    b = contourn

    i = A - b / 2 + 1

    return int(i + b)


# part 1

contourn = 0
vertices = []
start_pos = (0, 0)

for dir, n, color in dig_plan:
    if dir == "D":
        start_pos = (start_pos[0] + n, start_pos[1])
    elif dir == "R":
        start_pos = (start_pos[0], start_pos[1] + n)
    elif dir == "U":
        start_pos = (start_pos[0] - n, start_pos[1])
    elif dir == "L":
        start_pos = (start_pos[0], start_pos[1] - n)
    contourn += n
    vertices.append(start_pos)

print(calculate_area(vertices, contourn))

# Part 2

contourn = 0
vertices = []
start_pos = (0, 0)

for dir, n, color in dig_plan:
    if color[-1] == "0":
        dir = "R"
    elif color[-1] == "1":
        dir = "D"
    elif color[-1] == "2":
        dir = "L"
    elif color[-1] == "3":
        dir = "U"
    n = int(color[:-1], base=16)
    if dir == "D":
        start_pos = (start_pos[0] + n, start_pos[1])
    elif dir == "R":
        start_pos = (start_pos[0], start_pos[1] + n)
    elif dir == "U":
        start_pos = (start_pos[0] - n, start_pos[1])
    elif dir == "L":
        start_pos = (start_pos[0], start_pos[1] - n)

    contourn += n
    vertices.append(start_pos)

print(calculate_area(vertices, contourn))
