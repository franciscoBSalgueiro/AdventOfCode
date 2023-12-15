from collections import defaultdict


file = "input/2023/day15.txt"
# file = "src/examples/day15_example.txt"

with open(file) as f:
    input = f.read().strip()


def hash(string):
    current_value = 0
    for ch in string:
        current_value += ord(ch)
        current_value *= 17
        current_value %= 256
    return current_value


codes = [hash(code) for code in input.split(",")]
print(sum(codes))

# part 2

slots = defaultdict(list)

for i, code in enumerate(input.split(",")):
    label = code[:2]
    op = code[2:]
    h = hash(label)
    if op[0] == "=":
        for i, (l, _) in enumerate(slots[h]):
            if l == label:
                slots[h][i] = (label, int(op[1]))
                break
        else:
            slots[h].append((label, int(op[1])))
    else:
        slots[h] = list(filter(lambda x: x[0] != label, slots[h]))

total = 0
for k, v in slots.items():
    for i, code in enumerate(v):
        total += (k + 1) * (i + 1) * code[1]

print(total)
