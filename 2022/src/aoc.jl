module aoc

using BenchmarkTools
using Suppressor

solvedDays = 1:11

for day in solvedDays
    dayString = "day" * lpad(day, 2, '0')

    global daySymbol = Symbol(dayString)
    global benchmarkSymbol = Symbol("benchmark" * titlecase(dayString))
    global modSymbol = Symbol(titlecase(dayString))
    include(joinpath(@__DIR__, "..", dayString, dayString * ".jl"))

    @eval begin
        function $daySymbol(part::Int, inputFile=joinpath(@__DIR__, "..", $dayString, "input.txt"))
            if part == 1
                return $modSymbol.part1(inputFile)
            elseif part == 2
                return $modSymbol.part2(inputFile)
            else
                error("Invalid part number")
            end
        end
        export $daySymbol
    
        function $benchmarkSymbol(part)
            if part == 1
                return @suppress @benchmark $daySymbol(1)
            elseif part == 2
                return @suppress @benchmark $daySymbol(2)
            else
                error("Invalid part number")
            end
        end
        export $benchmarkSymbol
    end
end

end