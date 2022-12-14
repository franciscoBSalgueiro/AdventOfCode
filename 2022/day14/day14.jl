module Day14

function parseInput(input)
    occupied = Set{Tuple{Int,Int}}()
    for line in eachline(input)
        points = split.(split(line, " -> "), ",")
        points = [parse.(Int, p) for p in points]
        for i in 1:length(points)-1
            lx = minmax(points[i][1], points[i+1][1])
            ly = minmax(points[i][2], points[i+1][2])
            for x in lx[1]:lx[2]
                for y in ly[1]:ly[2]
                    push!(occupied, (x, y))
                end
            end
        end
    end
    return occupied
end

function addSand(occupied, floor, void)
    pos = (500, 0)
    while true
        if pos[2] + 1 == floor
            if void
                push!(occupied, (500, 0))
            else 
                push!(occupied, pos)
            end
            break
        end
        if pos .+ (0, 1) ∉ occupied
            pos = pos .+ (0, 1)
        elseif pos .+ (-1, 1) ∉ occupied
            pos = pos .+ (-1, 1)
        elseif pos .+ (1, 1) ∉ occupied
            pos = pos .+ (1, 1)
        else
            push!(occupied, pos)
            break
        end
    end

    return occupied
end

function solver(input, void)
    occupied = parseInput(input)
    floor = maximum([p[2] for p in occupied]) + (void ? 1 : 2)
    initial_walls = length(occupied)
    while (500, 0) ∉ occupied
        occupied = addSand(occupied, floor, void)
    end
    return length(occupied) - initial_walls - (void ? 1 : 0)
end

function part1(input="input.txt")
    solver(input, true)
end

function part2(input="input.txt")
    solver(input, false)
end

end