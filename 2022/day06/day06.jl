module Day06

function solver(n, input)
    data = read(input)
    start = 1
    ending = n
    while ending <= lastindex(data)
        if length(Set(data[start:ending])) == n
            println(ending)
            break
        end
        start += 1
        ending += 1
    end
end

function part1(input = "input.txt")
    solver(4, input)
end

function part2(input = "input.txt")
    solver(14, input)
end

end