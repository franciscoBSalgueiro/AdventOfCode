module Day12

function letterToNumber(letter)
    if letter == 'S'
        return 1
    elseif letter == 'E'
        return 26
    end
    return letter - 'a' + 1
end

function parseInput(input)
    lines = readlines(input)
    letters = hcat(collect.(lines)...)
    elevations = letterToNumber.(letters)
    return elevations, letters
end

function calculateDistance(start, elevations, finishTest, canTravel)
    queue = [(pos=start, depth=0)]
    visited = Set{CartesianIndex{2}}()
    push!(visited, start)

    while !isempty(queue)
        (pos, depth) = popfirst!(queue)
        if finishTest(pos)
            return depth
        end
        for δ in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            n = pos + CartesianIndex(δ)
            if checkbounds(Bool, elevations, n) && canTravel(elevations[pos], elevations[n]) && n ∉ visited
                push!(queue, (pos=n, depth=depth + 1))
                push!(visited, n)
            end
        end
    end
    return typemax(Int)
end

function part1(input="input.txt")
    elevations, letters = parseInput(input)
    start = findfirst(letters .== 'S')
    finish = findfirst(letters .== 'E')
    canTravel = (a, b) -> b - a <= 1
    calculateDistance(start, elevations, x -> x == finish, canTravel)
end

function part2(input="input.txt")
    elevations, letters = parseInput(input)
    start = findfirst(letters .== 'E')
    canTravel = (a, b) -> a - b <= 1
    calculateDistance(start, elevations, x -> elevations[x] == 1, canTravel)
end

end