from collections import defaultdict, deque


file = "input/2023/day20.txt"
# file = "src/examples/day20_example.txt"

with open(file) as f:
    lines = f.readlines()

total_low = 0
total_high = 0


class Module:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def pulse(self, value, input):
        pass


class FlipFlop(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.value = False

    def pulse(self, value, input):
        if value is False:
            self.value = not self.value
            if self.value is True:
                return True
            return False

    def __repr__(self):
        return f"{self.name}: {self.value}"


class Conjunction(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)
        self.inputs = {}

    def pulse(self, value, input):
        self.inputs[input] = value
        if all(self.inputs.values()):
            return False
        return True

    def __repr__(self):
        return f"{self.name}: {self.inputs}"


class Broadcaster(Module):
    def __init__(self, name, outputs):
        super().__init__(name, outputs)

    def pulse(self, value, input):
        return value

    def __repr__(self):
        return f"{self.name}"


modules = defaultdict(lambda: Module("default", []))


for line in lines:
    [name, outputs] = line.strip().split(" -> ")
    outputs = outputs.split(", ")
    if name[0] == "%":
        modules[name[1:]] = FlipFlop(name[1:], outputs)
    elif name[0] == "&":
        modules[name[1:]] = Conjunction(name[1:], outputs)
    elif name == "broadcaster":
        modules[name] = Broadcaster(name, outputs)


for module in modules:
    for output in modules[module].outputs:
        if output in modules and isinstance(modules[output], Conjunction):
            modules[output].inputs[module] = False

cycles = defaultdict(list)

for i in range(1000):
    queue = deque()
    queue.append((False, "broadcaster"))
    total_low += 1
    while queue:
        value, name = queue.popleft()
        for output in modules[name].outputs:
            if value is True:
                total_high += 1
            elif value is False:
                total_low += 1
            v = modules[output].pulse(value, name)
            ######
            # part 2
            if output in ["st", "tn", "hh", "dt"] and v is True:
                # print(f"{output}: {i}")
                cycles[output].append(i)
            #####
            if v is not None:
                queue.append((v, output))
    # total_low += 1
    # print(total_low)
    # print(total_high)
    # print()

print(total_low * total_high)


# Part 2 was done manually by looking at the cycles of each input of the conjunction that leads to rx

for k, v in cycles.items():
    # print(k, v)
    # print differences for cycle detection
    print(k, [v[i + 1] - v[i] for i in range(len(v) - 1)])

# hh 3769
# tn 3863
# st 3929
# dt 4079

# lcm = 233338595643977