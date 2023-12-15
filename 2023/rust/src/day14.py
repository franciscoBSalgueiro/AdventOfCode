from copy import deepcopy
import numpy as np

file = "input/2023/day14.txt"
# file = "src/examples/day14_example.txt"

with open(file) as f:
    lines = np.array([list(line.strip()) for line in f.readlines()])


def pull_water(lines, direction):
    if direction == "up" or direction == "left":
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == "O":
                    tmpi = i
                    tmpj = j
                    if direction == "left":
                        while tmpj > 0 and lines[tmpi][tmpj - 1] == ".":
                            lines[tmpi][tmpj - 1] = "O"
                            lines[tmpi][tmpj] = "."
                            tmpj -= 1
                    elif direction == "up":
                        while tmpi > 0 and lines[tmpi - 1][tmpj] == ".":
                            lines[tmpi - 1][tmpj] = "O"
                            lines[tmpi][tmpj] = "."
                            tmpi -= 1
    elif direction == "down" or direction == "right":
        for i in range(len(lines) - 1, -1, -1):
            for j in range(len(lines[i]) - 1, -1, -1):
                if lines[i][j] == "O":
                    tmpi = i
                    tmpj = j
                    if direction == "right":
                        while tmpj < len(lines[i]) - 1 and lines[tmpi][tmpj + 1] == ".":
                            lines[tmpi][tmpj + 1] = "O"
                            lines[tmpi][tmpj] = "."
                            tmpj += 1
                    elif direction == "down":
                        while tmpi < len(lines) - 1 and lines[tmpi + 1][tmpj] == ".":
                            lines[tmpi + 1][tmpj] = "O"
                            lines[tmpi][tmpj] = "."
                            tmpi += 1
    return lines


def count_points(lines):
    total = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                total += len(lines) - i
    return total


# part 1
lines_part1 = deepcopy(lines)
pull_water(lines_part1, "up")

# print(count_points(lines_part1))

# part 2
lines_part2 = deepcopy(lines)


def cycle(lines):
    pull_water(lines, "up")
    pull_water(lines, "left")
    pull_water(lines, "down")
    pull_water(lines, "right")


for i in range(100000000):
    print(i, count_points(lines_part2))
    cycle(lines_part2)

    # answer determined by looking at the pattern
