function part1()
    max_elfs = 0
    local_max = 0
    for line in eachline("input.txt")
        if line == ""
            if local_max > minimum(max_elfs)
                max_elfs = local_max
            end
            local_max = 0
            continue
        end
           
        v = parse(Int, line)
        local_max += v
    end

    println(max_elfs)
end

function part2()
    max_elfs = zeros(Int, 3)
    local_max = 0
    for line in eachline("input.txt")
        if line == ""
            if local_max > minimum(max_elfs)
                max_elfs[findmin(max_elfs)[2]] = local_max
            end
            local_max = 0
            continue
        end
           
        v = parse(Int, line)
        local_max += v
    end

    println(sum(max_elfs))
end

part1()
part2()
