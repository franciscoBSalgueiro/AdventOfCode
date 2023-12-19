file = "input/2023/day19.txt"
# file = "src/examples/day19_example.txt"

with open(file) as f:
    lines = f.read()


[workflows, parts] = lines.split("\n\n")

workflows = workflows.split("\n")
parts = parts.split("\n")

workflows_dict = {}
for workflow in workflows:
    [key, value] = workflow.split("{")
    value = value.replace("}", "").split(",")
    value = [v.split(":") for v in value]
    workflows_dict[key] = value

parts = [part.replace("{", "").replace("}", "").split(",") for part in parts]
parts = [{r.split("=")[0]: int(r.split("=")[1]) for r in part} for part in parts]


def part_value(part):
    return sum(part.values())


def apply_workflow(part, workflow):
    for rule in workflow:
        if len(rule) == 1:
            return rule[0]
        else:
            if rule[0][1] == "<":
                if part[rule[0][0]] < int(rule[0][2:]):
                    return rule[1]
            elif rule[0][1] == ">":
                if part[rule[0][0]] > int(rule[0][2:]):
                    return rule[1]


def apply_full_workflow(part, workflows_dict):
    cur = "in"
    while cur != "A" and cur != "R":
        cur = apply_workflow(part, workflows_dict[cur])
    return cur


# Part 1

total = 0
for part in parts:
    if apply_full_workflow(part, workflows_dict) == "A":
        total += part_value(part)

print(total)

# Part 2


def calculate_possibilities(key, workflows_dict, constrains: dict):
    if key == "R":
        return 0
    if key == "A":
        result = 1
        for k in constrains:
            result *= constrains[k][1] - constrains[k][0] + 1
        return result

    total = 0
    rules = workflows_dict[key]
    for rule in rules:
        if len(rule) == 1:
            total += calculate_possibilities(rule[0], workflows_dict, constrains.copy())
        else:
            k = rule[0][0]
            op = rule[0][1]
            v = int(rule[0][2:])

            accepted_constraints = constrains.copy()
            else_constraints = constrains.copy()
            if op == "<":
                accepted_constraints[k] = (accepted_constraints[k][0], v - 1)
                else_constraints[k] = (v, constrains[k][1])
            elif op == ">":
                accepted_constraints[k] = (v + 1, accepted_constraints[k][1])
                else_constraints[k] = (constrains[k][0], v)
            if accepted_constraints[k][0] <= accepted_constraints[k][1]:
                total += calculate_possibilities(
                    rule[1], workflows_dict, accepted_constraints
                )
            if else_constraints[k][0] > else_constraints[k][1]:
                return total
            constrains = else_constraints
    return total


print(
    calculate_possibilities(
        "in",
        workflows_dict,
        {
            "x": (1, 4000),
            "m": (1, 4000),
            "a": (1, 4000),
            "s": (1, 4000),
        },
    )
)
