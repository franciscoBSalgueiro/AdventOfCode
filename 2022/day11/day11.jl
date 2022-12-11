module Day11

function fnFromString(s)
    f = eval(Meta.parse("old -> " * s))
    return x -> Base.invokelatest(f, x)
end

function parseInput(input)
    lines = readlines(input)
    monkey = 0
    items = []
    operations = []
    divisions = []
    cases = []
    for line in lines
        if startswith(line, "Monkey")
            monkey += 1
        elseif contains(line, "Starting")
            monkeyItems = parse.(Int,split(match(r"Starting items: (.*)", line).captures[1], ", "))
            push!(items, monkeyItems)
        elseif contains(line, "Operation")
            op = split(line, "new =")[2]
            push!(operations, fnFromString(op))
        elseif contains(line, "Test")
            d = parse(Int, split(line, "divisible by ")[2])
            push!(divisions, d)
        elseif contains(line, "If true")
            newMonkey = parse(Int, split(line, "throw to monkey ")[2])
            push!(cases, [newMonkey])
        elseif contains(line, "If false")
            newMonkey = parse(Int, split(line, "throw to monkey ")[2])
            push!(cases[monkey], newMonkey)
        end
    end
    return items, operations, divisions, cases
end

function getResult(inspections)
    sort!(inspections, rev=true)
    return inspections[1] * inspections[2]
end


function part1(input = "input.txt")
    items, operations, divisions, cases = parseInput(input)
    nInspections = zeros(Int, length(items))

    for _ in 1:20
        for (i, m) in enumerate(items)
            nInspections[i] += length(m)
            for item in m
                worryLevel = item
                worryLevel = operations[i](worryLevel)
                worryLevel = worryLevel ÷ 3
                if (worryLevel % divisions[i]) == 0
                    newMonkey = cases[i][1] + 1
                    push!(items[newMonkey], worryLevel)
                else
                    newMonkey = cases[i][2] + 1
                    push!(items[newMonkey], worryLevel)
                end
            end
            empty!(items[i])
        end
    end
    return getResult(nInspections)
end

function part2(input = "input.txt")
    items, operations, divisions, cases = parseInput(input)

    nInspections = zeros(Int, length(items))
    totalDivider = prod(divisions)

    for _ in 1:10000
        for (i, m) in enumerate(items)
            nInspections[i] += length(m)
            for item in m
                worryLevel = item
                worryLevel = operations[i](worryLevel)
                worryLevel = worryLevel % totalDivider
                if (worryLevel % divisions[i]) == 0
                    newMonkey = cases[i][1] + 1
                    push!(items[newMonkey], worryLevel)
                else
                    newMonkey = cases[i][2] + 1
                    push!(items[newMonkey], worryLevel)
                end
            end
            empty!(items[i])
        end
    end
    return getResult(nInspections)
end

end
