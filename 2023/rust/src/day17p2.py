from dijkstar import Graph, find_path

file = "input/2023/day17.txt"
# file = "src/examples/day17_example.txt"

with open(file) as f:
    lines = [[int(x) for x in line.strip()] for line in f.readlines()]

# print(lines)

path_min = 4
path_max = 10 + path_min - 1

graph = Graph()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        # right
        for x in range(path_min, path_max + 1):
            if j + x >= len(lines[i]):
                break
            # turning up
            if i - path_min >= 0:
                graph.add_edge(
                    (i, j),
                    (i - path_min, j + x),
                    (
                        "right",
                        "up",
                        sum([lines[i][j + ii] for ii in range(1, x + 1)])
                        + sum([lines[i - ii][j + x] for ii in range(1, path_min + 1)]),
                    ),
                )
            # turning down
            if i + path_min < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + path_min, j + x),
                    (
                        "right",
                        "down",
                        sum([lines[i][j + ii] for ii in range(1, x + 1)])
                        + sum([lines[i + ii][j + x] for ii in range(1, path_min + 1)]),
                    ),
                )
        # down
        for x in range(path_min, path_max + 1):
            if i + x >= len(lines):
                break
            # turning left
            if j - path_min >= 0:
                graph.add_edge(
                    (i, j),
                    (i + x, j - path_min),
                    (
                        "down",
                        "left",
                        sum([lines[i + ii][j] for ii in range(1, x + 1)])
                        + sum([lines[i + x][j - ii] for ii in range(1, path_min + 1)]),
                    ),
                )
            # turning right
            if j + path_min < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i + x, j + path_min),
                    (
                        "down",
                        "right",
                        sum([lines[i + ii][j] for ii in range(1, x + 1)])
                        + sum([lines[i + x][j + ii] for ii in range(1, path_min + 1)]),
                    ),
                )
        # left
        for x in range(path_min, path_max + 1):
            if j - x < 0:
                break
            # turning up
            if i - path_min >= 0:
                graph.add_edge(
                    (i, j),
                    (i - path_min, j - x),
                    (
                        "left",
                        "up",
                        sum([lines[i][j - ii] for ii in range(1, x + 1)])
                        + sum([lines[i - ii][j - x] for ii in range(1, path_min + 1)]),
                    ),
                )
            # turning down
            if i + path_min < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + path_min, j - x),
                    (
                        "left",
                        "down",
                        sum([lines[i][j - ii] for ii in range(1, x + 1)])
                        + sum([lines[i + ii][j - x] for ii in range(1, path_min + 1)]),
                    ),
                )
        # up
        for x in range(path_min, path_max + 1):
            if i - x < 0:
                break
            # turning left
            if j - path_min >= 0:
                graph.add_edge(
                    (i, j),
                    (i - x, j - path_min),
                    (
                        "up",
                        "left",
                        sum([lines[i - ii][j] for ii in range(1, x + 1)])
                        + sum([lines[i - x][j - ii] for ii in range(1, path_min + 1)]),
                    ),
                )
            # turning right
            if j + path_min < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i - x, j + path_min),
                    (
                        "up",
                        "right",
                        sum([lines[i - ii][j] for ii in range(1, x + 1)])
                        + sum([lines[i - x][j + ii] for ii in range(1, path_min + 1)]),
                    ),
                )


def cost_func(u, v, edge, prev_edge):
    if prev_edge is None:
        return edge[2]

    if (
        prev_edge[1] == "up"
        and edge[0] == "down"
        or prev_edge[1] == "down"
        and edge[0] == "up"
        or prev_edge[1] == "left"
        and edge[0] == "right"
        or prev_edge[1] == "right"
        and edge[0] == "left"
    ):
        return 1000

    return edge[2]


start = (0, 0)
end = (len(lines) - 1, len(lines[0]) - 1)

path = find_path(graph, start, end, cost_func=cost_func)


def visualize_path(path):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i, j) in path.nodes:
                print("X", end="")
            else:
                print(".", end="")
        print()


print(path.edges)
print(path.nodes)
print(path.costs)
# visualize_path(path)
print(path.total_cost + 1)
