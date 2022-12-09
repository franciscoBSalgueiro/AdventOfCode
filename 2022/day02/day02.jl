module Day02

function part1(input="input.txt")
    score = 0
    for line in eachline(input)
        a, b = split(line, ' ')
        if b == "X"
            if a == "C"
                score += 6
            end
            if a == "A"
                score += 3
            end
            score += 1
        end
        if b == "Y"

            if a == "A"
                score += 6
            end
            if a == "B"
                score += 3
            end
            score += 2
        end

        if b == "Z"
            if a == "B"
                score += 6
            end
            if a == "C"
                score += 3
            end
            score += 3
        end
    end
    return score
end

function part2(input="input.txt")
    score = 0
    for line in eachline(input)
        a, b = split(line, ' ')
        if b == "X"
            if a == "C"
                score += 2
            end
            if a == "A"
                score += 3
            end
            if a == "B"
                score += 1
            end
        end
        if b == "Y"
            if a == "A"
                score += 1
            end
            if a == "B"
                score += 2
            end
            if a == "C"

                score += 3
            end
            score += 3
        end

        if b == "Z"
            if a == "B"
                score += 3
            end
            if a == "C"
                score += 1
            end
            if a == "A"
                score += 2
            end
            score += 6
        end
    end
    return score
end

end