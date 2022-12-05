function solver(reversed)
    cargo = []

    for line in eachline("input.txt")
        if startswith(line, "[") || (startswith(line, " ") && !isnumeric(line[2]))
            i = 2
            j = 1
            while i < lastindex(line)
                if lastindex(cargo) < j
                    push!(cargo, [])
                end
                if line[i] != ' '
                    pushfirst!(cargo[j], line[i])
                end
                j += 1
                i += 4
            end
        elseif startswith(line, "move")
            tokens = split(line, " ")
            n = parse(Int, tokens[2])
            from = parse(Int, tokens[4])
            to = parse(Int, tokens[6])
            moving = cargo[from][end-n+1:end]
            if reversed
                moving = reverse(moving)
            end
            deleteat!(cargo[from], lastindex(cargo[from])-n+1:lastindex(cargo[from]))
            cargo[to] = vcat(cargo[to], moving)
        end

    end
    println(join(last.(cargo)))
end

function part1()
    solver(true)
end

function part2()
    solver(false)
end

part1()
part2()