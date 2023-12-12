from functools import lru_cache

file = "input/2023/day12.txt"
# file = "src/examples/day12_example.txt"

with open(file) as f:
    lines = f.readlines()

rows = []

for l in lines:
    [values, counts] = l.split(" ")
    counts = tuple(int(x) for x in counts.strip().split(","))
    rows.append([values, counts])


@lru_cache()
def count_poss(values, counts):
    if len(values) == 0 and len(counts) == 0:
        return 1

    if len(values) == 0 and len(counts) > 0:
        return 0

    if len(counts) == 0:
        if any([x == "#" for x in values]):
            return 0
        return 1

    if len(values) < sum(counts):
        return 0

    if values[0] == ".":
        return count_poss(values[1:], counts)

    if values[0] == "?":
        return count_poss("#" + values[1:], counts) + count_poss(
            "." + values[1:], counts
        )

    if values[0] == "#":
        v = counts[0]
        if any([x == "." for x in values[:v]]):
            return 0
        if len(values) > v and values[v] == "#":
            return 0
        return count_poss(values[v + 1 :], counts[1:])


total_possibilities = [count_poss(values, counts) for [values, counts] in rows]

print("part 1 -", sum(total_possibilities))


total_possibilities = [
    count_poss(((values + "?") * 5)[:-1], counts * 5) for [values, counts] in rows
]

print("part 2 -", sum(total_possibilities))
