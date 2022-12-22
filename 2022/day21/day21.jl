module Day21

function calculateOperation(op, monkeys)
    v = tryparse(Int,op)
    if v !== nothing
        return v
    end
    arg1, operator, arg2 = split(op)
    v1 = calculateOperation(monkeys[arg1], monkeys)
    v2 = calculateOperation(monkeys[arg2], monkeys)
    if operator == "+"
        return v1 + v2
    elseif operator == "-"
            return v1 - v2
    elseif operator == "*"
        return v1 * v2
    elseif operator == "/"
        return v1 ÷ v2
    end
end

function part1(input = "input.txt")
    monkeys = Dict()
    for line in eachline(input)
        🐒, op = split(line, ": ")
        monkeys[🐒] = op
    end
    @show calculateOperation(monkeys["root"], monkeys)
end

function calculateHuman(op, monkeys, isHuman, isRoot)
    v = tryparse(Int,op)
    if v !== nothing
        if isHuman
            return complex(0, 1)
        else
            return complex(v, 0)
        end
    end
    arg1, operator, arg2 = split(op)

    v1 = calculateHuman(monkeys[arg1], monkeys, arg1 == "humn", false)
    v2 = calculateHuman(monkeys[arg2], monkeys, arg2 == "humn", false)
    if isRoot
        if abs(imag(v1)) > abs(imag(v2))
            return trunc(Int, real(v2 - v1) / imag(v1))
        else
            return trunc(Int, real(v1 - v2) / imag(v2))
        end
    end

    if operator == "+"
        return v1 + v2
    elseif operator == "-"
        return v1 - v2
    elseif operator == "*"
        return v1 * v2
    elseif operator == "/"
        return v1 / v2
    end
end

function part2(input = "input.txt")
    monkeys = Dict()
    for line in eachline(input)
        🐒, op = split(line, ": ")
        monkeys[🐒] = op
    end
    calculateHuman(monkeys["root"], monkeys, false, true)
end

end