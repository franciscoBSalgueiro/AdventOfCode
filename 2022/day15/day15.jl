module Day15

function distance(p1, p2)
    return abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
end

function part1(input="input.txt")
    row = 2000000
    impossible = Set{Tuple{Int,Int}}()
    for line in eachline(input)
        m = [m.match for m in eachmatch(r"(-?\d+)", line)]
        x, y, bx, by = parse.(Int, m)
        if (d = distance((x, y), (bx, by))) >= y - row
            for i in -d:d
                if distance((x, y), (x + i, row)) <= distance((x, y), (bx, by)) && (x + i, row) != (bx, by)
                    push!(impossible, (x + i, row))
                end
            end
        end
    end
    length(impossible)
end

function part2(input="input.txt")
    min_xy = 0
    max_xy = 4000000
    sensor_distances = Tuple{Tuple{Int,Int},Int}[]
    possible = Set{Tuple{Int,Int}}()

    for line in eachline(input)
        m = [m.match for m in eachmatch(r"(-?\d+)", line)]
        x, y, bx, by = parse.(Int, m)
        d = distance((x, y), (bx, by)) + 1

        push!(sensor_distances, ((x, y), d))

        for pos in possible
            if distance(pos, (x, y)) > d
                delete!(possible, pos)
            end
        end

        for xᵢ in -d:d
            pos = (x + xᵢ, y - d + abs(xᵢ))
            if pos[1] >= min_xy && pos[1] <= max_xy && pos[2] >= min_xy && pos[2] <= max_xy
                push!(possible, pos)
            end
        end
        for yᵢ in -d:d
            pos = (x + d - abs(yᵢ), y - yᵢ)
            if pos[1] >= min_xy && pos[1] <= max_xy && pos[2] >= min_xy && pos[2] <= max_xy
                push!(possible, pos)
            end
        end
    end

    for (sensor, d) in sensor_distances
        for pos in possible
            if distance(sensor, pos) < d
                delete!(possible, pos)
                continue
            end
        end
    end

    finalPos = pop!(possible)
    return finalPos[1] * 4000000 + finalPos[2] 
end

end