with open("input/2023/day10-preprocessed.txt") as f:
    lines = [line.replace("\n", "") for line in f.readlines()]

total = sum([line.count(".") for line in lines])
starting_pos = (0, 0)


neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()
visited.add(starting_pos)
visited_dot = set()
q = [starting_pos]

while len(q) > 0:
    pos = q.pop(0)
    for neighbour in neighbours:
        new_pos = (pos[0] + neighbour[0], pos[1] + neighbour[1])
        if (
            new_pos[0] >= 0
            and new_pos[0] < len(lines)
            and new_pos[1] >= 0
            and new_pos[1] < len(lines[0])
            and (lines[new_pos[0]][new_pos[1]] == "." or lines[new_pos[0]][new_pos[1]] == " ")
            and new_pos not in visited
        ):
            if lines[new_pos[0]][new_pos[1]] == ".":
                visited_dot.add(new_pos)
            visited.add(new_pos)
            q.append(new_pos)

print(total - len(visited_dot))
