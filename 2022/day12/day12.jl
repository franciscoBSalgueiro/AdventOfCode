module Day12

function letterToNumber(letter)
    if letter == 'S'
        return 1
    elseif letter == 'E'
        return 26
    end
    return letter - 'a' + 1
end

function canTravel(v1, v2)
    if v2 - v1 > 1
        return false
    end
    return true
end

function parseInput(input)
    lines = readlines(input)
    letters = hcat(collect.(lines)...)
    elevations = letterToNumber.(letters)
    finish = findfirst(letters .== 'E')
    return elevations, letters, finish
end

function calculateDistance(start, finish, elevations)
    queue = [(pos=start, depth=0)]
    visited = Set{CartesianIndex{2}}()
    push!(visited, start)

    while !isempty(queue)
        (pos, depth) = popfirst!(queue)
        if pos == finish
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
    elevations, letters, finish = parseInput(input)
    start = findfirst(letters .== 'S')
    calculateDistance(start, finish, elevations)
end


function part2(input="input.txt")
    elevations, letters, finish = parseInput(input)
    startingPositions = findall(letters .== 'a')

    min([calculateDistance(pos, finish, elevations) for pos in startingPositions]...)
end

end