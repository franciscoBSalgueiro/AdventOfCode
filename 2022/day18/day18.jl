module Day18

const neighbors::Vector{Tuple{Int,Int,Int}} = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

function parseInput(input="input.txt")
    cubes = []
    for line in eachline(input)
        cube = Tuple(parse.(Int, split(line, ",")))
        push!(cubes, cube)
    end
    return cubes
end

function part1(input="input.txt")
    cubes = parseInput(input)
    sum([n .+ cube ∉ cubes for n in neighbors for cube in cubes])
end

function part2(input="input.txt")
    cubes = parseInput(input)
    sides = 0
    seen = Set{Tuple{Int,Int,Int}}()
    start = (0, 0, 0)
    queue = [start]
    bounds = range(-1, 20)
    while length(queue) > 0
        cube = pop!(queue)
        for n in neighbors
            v = n .+ cube
            if v ∈ cubes
                sides += 1
            elseif v ∉ seen && v[1] ∈ bounds && v[2] ∈ bounds && v[3] ∈ bounds
                push!(queue, v)
                push!(seen, v)
            end
        end
    end
    return sides
end

end
