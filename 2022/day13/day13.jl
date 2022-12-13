module Day13

using JSON3

function parseInput(input)
    packets = []
    for line in eachline(input)
        if line != ""
            push!(packets, JSON3.read(line))
        end
    end
    return packets
end

function compare(a::AbstractArray, b::AbstractArray)
    for (x₁, x₂) in zip(a, b)
        c = compare(x₁, x₂)
        if c != 0
            return c
        end
    end
    return sign(length(a) - length(b))
end

compare(a::Int, b::Int) = sign(a - b)
compare(a::AbstractArray, b::Int) = compare(a, [b])
compare(a::Int, b::AbstractArray) = compare([a], b)

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
    aᵢ, bᵢ = 1, 2
    for p in packets
        if compare(p, [[2]]) <= 0
            aᵢ += 1
            bᵢ += 1
        elseif compare(p, [[6]]) <= 0
            bᵢ += 1
        end
    end

    return aᵢ * bᵢ
end

end