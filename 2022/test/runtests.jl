using aoc
using Test

@testset "Day 1" begin
    @test day01(1) == 72718
    @test day01(2) == 213089
end

@testset "Day 2" begin
    @test day02(1) == 11386
    @test day02(2) == 13600
end

@testset "Day 3" begin
    @test day03(1) == 7763
    @test day03(2) == 2569
end

@testset "Day 4" begin
    @test day04(1) == 528
    @test day04(2) == 881
end

@testset "Day 5" begin
    @test day05(1) == "CVCWCRTVQ"
    @test day05(2) == "CNSCZWLVT"

end

@testset "Day 6" begin
    @test day06(1) == 1647
    @test day06(2) == 2447
end

@testset "Day 7" begin
    @test day07(1) == 1297159
    @test day07(2) == 3866390
end

@testset "Day 8" begin
    @test day08(1) == 1785
    @test day08(2) == 345168
end

@testset "Day 9" begin
    @test day09(1) == 6266
    @test day09(2) == 2369
end

@testset "Day 10" begin
    @test day10(1) == 14560
    @test day10(2) == [
        '#' '#' '#' '#' '.' '#' '.' '.' '#' '.' '#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '#' '#' '#' '#'
        '#' '.' '.' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '.' '.' '#' '.'
        '#' '#' '#' '.' '.' '#' '#' '.' '.' '.' '#' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '.' '#' '.' '.'
        '#' '.' '.' '.' '.' '#' '.' '#' '.' '.' '#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '#' '#' '.' '.' '#' '.' '.' '#' '.' '.' '#' '.' '.' '.'
        '#' '.' '.' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '.' '#' '.' '.' '.' '.' '#' '.' '.' '#' '.' '#' '.' '.' '.' '#'
        '#' '#' '#' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '.' '.' '#' '.' '#' '#' '#' '#' '.' '#' '.' '.' '.' '.' '.' '#' '#' '.' '.' '#' '#' '#' '#' '.'
    ]
end

@testset "Day 11" begin
    @test day11(1) == 112221
    @test day11(2) == 25272176808
end

@testset "Day 12" begin
    @test day12(1) == 462
    @test day12(2) == 451
end

@testset "Day 13" begin
    @test day13(1) == 6369
    @test day13(2) == 25800
end

@testset "Day 14" begin
    @test day14(1) == 672
    @test day14(2) == 26831
end

@testset "Day 15" begin
    @test day15(1) == 5403290
    @test day15(2) == 10291582906626
end

@testset "Day 18" begin
    @test day18(1) == 3346
    @test day18(2) == 1980
end