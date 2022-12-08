module Day08

function parseInput(input)
    lines = readlines(input)
    ll = collect.(lines)
    m = parse.(Int, hcat(ll...))
    return m
end


function isVisible(m, I)
    R = CartesianIndices(m)
    Ifirst, Ilast = first(R), last(R)
    if I[1] == Ifirst[1] || I[1] == Ilast[1] || I[2] == Ifirst[2] || I[2] == Ilast[2]
        return true
    end

    for i in (I[1]-1):-1:Ifirst[1]
        if m[i, I[2]] >= m[I]
            break
        end
        if i == Ifirst[1]
            return true
        end
    end

    for i in (I[1]+1):1:Ilast[1]
        if m[i, I[2]] >= m[I]
            break
        end
        if i == Ilast[1]
            return true
        end
    end

    for j in (I[2]-1):-1:Ifirst[2]
        if m[I[1], j] >= m[I]
            break
        end
        if j == Ifirst[2]
            return true
        end
    end

    for j in (I[2]+1):1:Ilast[2]
        if m[I[1], j] >= m[I]
            break
        end
        if j == Ilast[2]
            return true
        end
    end

    return false
end

function scenicScore(m, I)
    R = CartesianIndices(m)
    Ifirst, Ilast = first(R), last(R)
    nLeft = 0
    nRight = 0
    nUp = 0
    nDown = 0

    if I[1] == Ifirst[1] || I[1] == Ilast[1] || I[2] == Ifirst[2] || I[2] == Ilast[2]
        return 0
    end

    for i in (I[1]-1):-1:Ifirst[1]
        if m[i, I[2]] >= m[I]
            nUp += 1
            break
        end
        nUp += 1
    end

    for i in (I[1]+1):1:Ilast[1]
        if m[i, I[2]] >= m[I]
            nDown += 1
            break
        end
        nDown += 1
    end

    for j in (I[2]-1):-1:Ifirst[2]
        if m[I[1], j] >= m[I]
            nLeft += 1
            break
        end
        nLeft += 1
    end

    for j in (I[2]+1):1:Ilast[2]
        if m[I[1], j] >= m[I]
            nRight += 1
            break
        end
        nRight += 1
    end

    return nLeft * nRight * nUp * nDown

end

function part1(input = "input.txt")
    m = parseInput(input)
    R = CartesianIndices(m)
    total = 0
    for I in R
        if isVisible(m, I)
            total += 1
        end
    end
    println(total)
end

function part2(input = "input.txt")
    m = parseInput(input)
    R = CartesianIndices(m)
    max = 0
    for I in R
        score = scenicScore(m, I)
        if score > max
            max = score
        end
    end
    println(max)
end

end