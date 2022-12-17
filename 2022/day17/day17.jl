module Day17

function move(pos, m, l, occupied, rock)
    if m == '<'
        if pos[1] == 0
            return pos
        else
            newPos = pos - CartesianIndex(1, 0)
            if any(newPos + p in occupied for p in rock)
                return pos
            else
                return newPos
            end
        end
    else
        if pos[1] + l == 7
            return pos
        else
            newPos = pos + CartesianIndex(1, 0)
            if any(newPos + p in occupied for p in rock)
                return pos
            else
                return newPos
            end
        end
    end
end
fall(pos) = pos - CartesianIndex(0, 1)

function print_tetris(occupied, h)
    for y in h:-1:0
        for x in 0:7
            if CartesianIndex(x, y) in occupied
                print("#")
            else
                print(".")
            end
        end
        println()
    end
end

function topView(occupied)
    tv = []
    for x in 1:7
        max_y = maximum([p[2] for p in filter(p -> p[1] == x, occupied)])
        push!(tv, CartesianIndex(x, max_y))
    end
    return tv
end

function part1(input="input_final.txt")
    movements = collect(readline(input))
    rocktypes = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 1), (1, 0), (2, 1), (1, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (0, 1), (1, 0), (1, 1)]
    ]
    occupied = Set()
    curMove = 1
    # previous_tv = Set()
    for i in 1:2022
        rock = CartesianIndex.(rocktypes[mod1(i, 5)])
        l = maximum([p[1] for p in rock]) + 1
        if length(occupied) == 0
            h = 0
        else
            h = maximum([p[2] for p in occupied]) + 1
        end
        pos = CartesianIndex(2, h + 4)
        while pos[2] > 0 && (!any(fall(p + pos) in occupied for p in rock))
            m = movements[mod1(curMove, length(movements))]
            curMove += 1
            pos = fall(pos)
            pos = move(pos, m, l, occupied, rock)
            # @show pos
            # @show [fall(p + pos) for p in rock]
        end
        # tv = topView(occupied)
        for p in rock
            push!(occupied, p + pos)
        end
        # @show h
        # @show pos
        # @show occupied
        # print_tetris(occupied, h + l)
        # println()
    end
    h = maximum([p[2] for p in occupied]) + 1
    # print_tetris(occupied, h)
    return h
end

println(part1())
end
