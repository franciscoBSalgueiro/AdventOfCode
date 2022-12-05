function contained(a, b)
    return (a[1] <= b[1] && a[2] >= b[2]) || (a[1] >= b[1] && a[2] <= b[2])
end

function overlaps(a, b)
    (a[2] >= b[1] && b[2] >= a[1]) || (b[2] >= a[1] && a[2] >= b[1])
end

function solver(check)
    total = 0
    for line in eachline("input.txt")
        pair1, pair2 = split.(split(line, ","), "-")
        if check((parse(Int, pair1[1]), parse(Int, pair1[2])), (parse(Int, pair2[1]), parse(Int, pair2[2])))
            total += 1
        end
    end
    println(total)
end

function part1()
    solver(contained)
end

function part2()
    solver(overlaps)
end

part1()
part2()