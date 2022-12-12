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
        neighbors = [
            CartesianIndex(pos[1] - 1, pos[2]),
            CartesianIndex(pos[1] + 1, pos[2]),
            CartesianIndex(pos[1], pos[2] - 1),
            CartesianIndex(pos[1], pos[2] + 1)
        ]
        for n in neighbors
            if (n[1] < 1 || n[1] > size(elevations)[1]) || (n[2] < 1 || n[2] > size(elevations)[2] || n in visited)
                continue
            end
            if canTravel(elevations[pos], elevations[n])
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