function solver(n)
    data = read("input.txt")
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

function part1()
    solver(4)
end

function part2()
    solver(14)
end

part1()
part2()
