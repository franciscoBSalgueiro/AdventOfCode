module Day01

function part1(input = "input.txt")
    max_elfs = 0
    local_max = 0
    for line in eachline(input)
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

function part2(input = "input.txt")
    max_elfs = zeros(Int, 3)
    local_max = 0
    for line in eachline(input)
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

end