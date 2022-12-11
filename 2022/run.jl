#!/usr/bin/julia

using Pkg

Pkg.activate(@__DIR__)

using aoc
using BenchmarkTools

if length(ARGS) == 0 || ARGS[1] == "a"
    # run all days
    for day in aoc.solvedDays
        local daySymbol = Symbol("day" * lpad(day, 2, "0"))
        printstyled("Day $day:\n", bold=true, underline=true)
        print("P1: ")
        println(@eval $daySymbol(1))
        print("P2: ")
        println(@eval $daySymbol(2))
    end
    exit(0)
end

if ARGS[1] == "t"
    Pkg.test()
    exit(0)
end

# Write the benchmark results into a markdown string:
function _to_markdown_table(bresults)
    header = "| Day | Part | Time | Allocated memory |\n" *
             "|----:|----:|-----:|-----------------:|"
    lines = [header]
    for (d, p, t, m) in bresults
        ds = string(d)
        ps = string(p)
        ts = BenchmarkTools.prettytime(t)
        ms = BenchmarkTools.prettymemory(m)
        push!(lines, "| $ds | $ps | $ts | $ms |")
    end
    return join(lines, "\n")
end

if ARGS[1] == "b"
    if length(ARGS) >= 2
        day = parse(Int, ARGS[2])
        if length(ARGS) == 3
            part = [parse(Int, ARGS[3])]
        else
            part = 1:2
        end
        local daySymbol = Symbol("benchmarkDay" * lpad(day, 2, "0"))
        @eval begin
            for p in part
                println("Day $day - part $p:")
                display($daySymbol(p))
            end
        end
    else
        results = []
        for day in aoc.solvedDays
            local daySymbol = Symbol("benchmarkDay" * lpad(day, 2, "0"))
            printstyled("Day $day - part 1:\n", bold=true, underline=true)
            r = @eval $daySymbol(1)
            display(r)
            push!(results, (day, 1, time(r), memory(r)))
            printstyled("Day $day - part 2:\n", bold=true, underline=true)
            r = @eval $daySymbol(2)
            display(r)
            push!(results, (day, 2, time(r), memory(r)))
        end
        println(_to_markdown_table(results))
    end

    exit()
end

ds = lpad(parse(Int, ARGS[1]), 2, "0")
dayFn = Symbol("day" * ds)

if length(ARGS) == 2
    part = parse(Int, ARGS[2])
    if (part != 1) && (part != 2)
        @error "Invalid part number (must be 1 or 2)"
        exit(1)
    end
    part = [part]
else
    part = 1:2
end

@eval begin
    printstyled("Day $(ARGS[1]):\n", bold=true, underline=true)
    for p in part
        display($dayFn(p))
    end
end
