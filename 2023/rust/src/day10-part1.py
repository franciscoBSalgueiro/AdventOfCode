import time
import numpy as np

with open("input/2023/day10.txt") as f:
    lines = np.array([list(line.strip()) for line in f.readlines()])

starting_pos = np.where(lines == "S")
starting_pos = (starting_pos[0][0], starting_pos[1][0])

pipes = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    # "S": [(1, 0), (-1, 0), (0, -1), (0, 1)],
    "S": [(0, 1), (1, 0)]
}

connected_pipes = {
    (starting_pos[0], starting_pos[1]): 0
}
edge_pos = [starting_pos]


def print_pos(pos):
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if (x, y) in pos:
                print(lines[x][y], end="")
            else:
                print(" ", end="")
        print()


distance = 0


while len(edge_pos) > 0:
    new_edge_pos = []
    for pos in edge_pos:
        pipe = lines[pos[0], pos[1]]
        if pipe != ".":
            if connected_pipes.get((pos[0], pos[1])) is None:
                connected_pipes[(pos[0], pos[1])] = distance

            for pipe in pipes[pipe]:
                new_pos = (pos[0] + pipe[0], pos[1] + pipe[1])
                if (
                    connected_pipes.get(new_pos) is None
                    and lines[new_pos[0], new_pos[1]] != "."
                ):
                    new_edge_pos.append(new_pos)

    edge_pos = new_edge_pos
    distance += 1

farthest_pos = max(connected_pipes, key=connected_pipes.get)
farthest_distance = connected_pipes[farthest_pos]

# print_pos(connected_pipes.keys())
print(farthest_distance)
