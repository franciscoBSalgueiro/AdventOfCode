module Day13

function parseInput(input)
    packets = []
    for line in eachline(input)
        if line != ""
            push!(packets, eval(Meta.parse(line)))
        end
    end
    return packets
end

function compare(a::Vector, b::Vector)
    for (x₁, x₂) in zip(a, b)
        c = compare(x₁, x₂)
        if c != 0
            return c
        end
    end
    return sign(length(a) - length(b))
end

compare(a::Int, b::Int) = sign(a - b)
compare(a::Vector, b::Int) = compare(a, [b])
compare(a::Int, b::Vector) = compare([a], b)

function part1(input="input.txt")
    packets = parseInput(input)
    total = 0
    for i in 1:2:lastindex(packets)
        if compare(packets[i], packets[i + 1]) <= 0
            total += (i + 1) ÷ 2
        end
    end
    return total
end

function part2(input="input.txt")
    packets = parseInput(input)
    push!(packets, [[2]], [[6]])
    sort!(packets, lt=(a, b) -> compare(a, b) < 0)

    aᵢ = findfirst(isequal([[2]]), packets)
    bᵢ = findfirst(isequal([[6]]), packets)

    return aᵢ * bᵢ
end

end