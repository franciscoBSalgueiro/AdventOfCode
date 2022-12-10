module Day10

function cycleLoop(cycle, n, r, total)
    for _ in 1:n
        cycle += 1
        if (cycle + 20) % 40 == 0
            total += (r * cycle)
        end
    end
    return cycle, total
end

function part1(input="input.txt")
    register = 1
    cycle = 0
    total = 0
    for line in eachline(input)
        cmd = split(line, " ")
        if cmd[1] == "noop"
            cycle, total = cycleLoop(cycle, 1, register, total)
        elseif cmd[1] == "addx"
            cycle, total = cycleLoop(cycle, 2, register, total)
            register += parse(Int, cmd[2])
        end
    end
    return total
end

function paintSprite(cycle, n, r, pixels)
    for _ in 1:n
        cycle += 1
        if r <= cycle % 40 <= r + 2
            pixels[cycle] = 1
        end
    end
    return cycle, pixels
end

function part2(input="input.txt")
    register = 1
    cycle = 0
    pixels = zeros(Int, 40, 6)
    for line in eachline(input)
        cmd = split(line, " ")
        if cmd[1] == "noop"
            cycle, pixels = paintSprite(cycle, 1, register, pixels)
        elseif cmd[1] == "addx"
            cycle, pixels = paintSprite(cycle, 2, register, pixels)
            register += parse(Int, cmd[2])
        end
    end
    pixels = transpose(pixels)
    char_pixels = map(pixels) do p
        if p == 1
            return '#'
        else
            return '.'
        end
    end
    return char_pixels
end

end