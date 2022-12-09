module Day09

function move(pos, d)
    if d == 'U'
        return pos + 1im
    elseif d == 'D'
        return pos - 1im
    elseif d == 'L'
        return pos - 1
    elseif d == 'R'
        return pos + 1
    end
end

function moveTail(head_pos, tail_pos)
    distance = head_pos - tail_pos
    if abs(distance) >= 2
        tail_pos += complex(sign(real(distance)), sign(imag(distance)))
    end
    return tail_pos
end

function solver(input, ropeLenght)
    lines = readlines(input)
    tail_positions = [complex(0, 0) for _ in 1:ropeLenght]
    visited_pos = Set{Complex{Int}}()
    for l in lines
        d, n = l[1], parse(Int, l[3:end])
        for _ in 1:n
            for (i, pos) in enumerate(tail_positions)
                if i == 1
                    tail_positions[i] = move(pos, d)
                else
                    tail_positions[i] = moveTail(tail_positions[i-1], pos)
                end
            end
            push!(visited_pos, last(tail_positions))
        end
    end
    return length(visited_pos)
end

function part1(input="input.txt")
    return solver(input, 2)
end

function part2(input="input.txt")
    return solver(input, 10)
end

end