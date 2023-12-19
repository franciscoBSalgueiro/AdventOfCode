from dijkstar import Graph, find_path

file = "input/2023/day17.txt"
# file = "src/examples/day17_example.txt"

with open(file) as f:
    lines = [[int(x) for x in line.strip()] for line in f.readlines()]

# print(lines)

graph = Graph()
for i in range(len(lines)):
    for j in range(len(lines[i])):
        # right
        if j + 1 < len(lines[i]):
            # turning up
            if i - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j + 1),
                    ("right", "up", lines[i][j + 1] + lines[i - 1][j + 1]),
                )
            # turning down
            if i + 1 < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + 1, j + 1),
                    ("right", "down", lines[i][j + 1] + lines[i + 1][j + 1]),
                )
        if j + 2 < len(lines[i]):
            # turning up
            if i - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j + 2),
                    (
                        "right",
                        "up",
                        lines[i][j + 1] + lines[i][j + 2] + lines[i - 1][j + 2],
                    ),
                )
            # turning down
            if i + 1 < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + 1, j + 2),
                    (
                        "right",
                        "down",
                        lines[i][j + 1] + lines[i][j + 2] + lines[i + 1][j + 2],
                    ),
                )
        if j + 3 < len(lines[i]):
            # turning up
            if i - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j + 3),
                    (
                        "right",
                        "up",
                        lines[i][j + 1]
                        + lines[i][j + 2]
                        + lines[i][j + 3]
                        + lines[i - 1][j + 3],
                    ),
                )
            # turning down
            if i + 1 < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + 1, j + 3),
                    (
                        "right",
                        "down",
                        lines[i][j + 1]
                        + lines[i][j + 2]
                        + lines[i][j + 3]
                        + lines[i + 1][j + 3],
                    ),
                )

        # down
        if i + 1 < len(lines):
            # turning right
            if j + 1 < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i + 1, j + 1),
                    ("down", "right", lines[i + 1][j] + lines[i + 1][j + 1]),
                )
            # turning left
            if j - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i + 1, j - 1),
                    ("down", "left", lines[i + 1][j] + lines[i + 1][j - 1]),
                )
        if i + 2 < len(lines):
            # turning right
            if j + 1 < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i + 2, j + 1),
                    (
                        "down",
                        "right",
                        lines[i + 1][j] + lines[i + 2][j] + lines[i + 2][j + 1],
                    ),
                )
            # turning left
            if j - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i + 2, j - 1),
                    (
                        "down",
                        "left",
                        lines[i + 1][j] + lines[i + 2][j] + lines[i + 2][j - 1],
                    ),
                )
        if i + 3 < len(lines):
            # turning right
            if j + 1 < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i + 3, j + 1),
                    (
                        "down",
                        "right",
                        lines[i + 1][j]
                        + lines[i + 2][j]
                        + lines[i + 3][j]
                        + lines[i + 3][j + 1],
                    ),
                )
            # turning left
            if j - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i + 3, j - 1),
                    (
                        "down",
                        "left",
                        lines[i + 1][j]
                        + lines[i + 2][j]
                        + lines[i + 3][j]
                        + lines[i + 3][j - 1],
                    ),
                )

        # left
        if j - 1 >= 0:
            # turning up
            if i - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j - 1),
                    ("left", "up", lines[i][j - 1] + lines[i - 1][j - 1]),
                )
            # turning down
            if i + 1 < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + 1, j - 1),
                    ("left", "down", lines[i][j - 1] + lines[i + 1][j - 1]),
                )
        if j - 2 >= 0:
            # turning up
            if i - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j - 2),
                    (
                        "left",
                        "up",
                        lines[i][j - 1] + lines[i][j - 2] + lines[i - 1][j - 2],
                    ),
                )
            # turning down
            if i + 1 < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + 1, j - 2),
                    (
                        "left",
                        "down",
                        lines[i][j - 1] + lines[i][j - 2] + lines[i + 1][j - 2],
                    ),
                )
        if j - 3 >= 0:
            # turning up
            if i - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j - 3),
                    (
                        "left",
                        "up",
                        lines[i][j - 1]
                        + lines[i][j - 2]
                        + lines[i][j - 3]
                        + lines[i - 1][j - 3],
                    ),
                )
            # turning down
            if i + 1 < len(lines):
                graph.add_edge(
                    (i, j),
                    (i + 1, j - 3),
                    (
                        "left",
                        "down",
                        lines[i][j - 1]
                        + lines[i][j - 2]
                        + lines[i][j - 3]
                        + lines[i + 1][j - 3],
                    ),
                )

        # up
        if i - 1 >= 0:
            # turning right
            if j + 1 < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i - 1, j + 1),
                    ("up", "right", lines[i - 1][j] + lines[i - 1][j + 1]),
                )
            # turning left
            if j - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 1, j - 1),
                    ("up", "left", lines[i - 1][j] + lines[i - 1][j - 1]),
                )
        if i - 2 >= 0:
            # turning right
            if j + 1 < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i - 2, j + 1),
                    (
                        "up",
                        "right",
                        lines[i - 1][j] + lines[i - 2][j] + lines[i - 2][j + 1],
                    ),
                )
            # turning left
            if j - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 2, j - 1),
                    (
                        "up",
                        "left",
                        lines[i - 1][j] + lines[i - 2][j] + lines[i - 2][j - 1],
                    ),
                )
        if i - 3 >= 0:
            # turning right
            if j + 1 < len(lines[i]):
                graph.add_edge(
                    (i, j),
                    (i - 3, j + 1),
                    (
                        "up",
                        "right",
                        lines[i - 1][j]
                        + lines[i - 2][j]
                        + lines[i - 3][j]
                        + lines[i - 3][j + 1],
                    ),
                )
            # turning left
            if j - 1 >= 0:
                graph.add_edge(
                    (i, j),
                    (i - 3, j - 1),
                    (
                        "up",
                        "left",
                        lines[i - 1][j]
                        + lines[i - 2][j]
                        + lines[i - 3][j]
                        + lines[i - 3][j - 1],
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
visualize_path(path)
print(path.total_cost)
