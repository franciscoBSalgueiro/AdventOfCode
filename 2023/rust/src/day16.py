file = "input/2023/day16.txt"
# file = "src/examples/day16_example.txt"

with open(file) as f:
    lines = [list(line.strip()) for line in f.readlines()]

X_SIZE = len(lines[0])
Y_SIZE = len(lines)


def move_beams(lines, beams: set):
    while beams:
        beam = beams.pop()
        if beam in completed:
            continue
        point, velocity = beam
        i, j = point
        vi, vj = velocity
        if i < 0 or j < 0 or j >= X_SIZE or i >= Y_SIZE:
            continue
        completed.add(beam)
        obj = lines[j][i]
        if obj == ".":
            beams.add(((i + vi, j + vj), velocity))
        elif obj == "/":
            if vi == 0 and vj == 1:
                beams.add(((i - 1, j), (-1, 0)))
            elif vi == 0 and vj == -1:
                beams.add(((i + 1, j), (1, 0)))
            elif vi == 1 and vj == 0:
                beams.add(((i, j - 1), (0, -1)))
            elif vi == -1 and vj == 0:
                beams.add(((i, j + 1), (0, 1)))
        elif obj == "\\":
            if vi == 0 and vj == 1:
                beams.add(((i + 1, j), (1, 0)))
            elif vi == 0 and vj == -1:
                beams.add(((i - 1, j), (-1, 0)))
            elif vi == 1 and vj == 0:
                beams.add(((i, j + 1), (0, 1)))
            elif vi == -1 and vj == 0:
                beams.add(((i, j - 1), (0, -1)))
        elif obj == "|":
            if vi == 0:
                beams.add(((i, j + vj), velocity))
            else:
                beams.add(((i, j - 1), (0, -1)))
                beams.add(((i, j + 1), (0, 1)))
        elif obj == "-":
            if vi == 0:
                beams.add(((i - 1, j), (-1, 0)))
                beams.add(((i + 1, j), (1, 0)))
            else:
                beams.add(((i + vi, j), velocity))


def print_beams(beams):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if (x, y) in [b[0] for b in beams]:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def count_beams(beams):
    return len(set([b[0] for b in beams]))


beams = set([((0, 0), (1, 0))])
completed = set()
move_beams(lines, beams)
print("part1:", count_beams(completed))

max_energy = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        print(x, y)
        possible_velocities = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if y == 0:
            possible_velocities.remove((0, -1))
        if y == Y_SIZE - 1:
            possible_velocities.remove((0, 1))
        if x == 0:
            possible_velocities.remove((-1, 0))
        if x == X_SIZE - 1:
            possible_velocities.remove((1, 0))

        for velocity in possible_velocities:
            beams = set([((x, y), velocity)])
            completed = set()
            move_beams(lines, beams)
            energy = count_beams(completed)
            if energy > max_energy:
                max_energy = energy

print("part2:", max_energy)
