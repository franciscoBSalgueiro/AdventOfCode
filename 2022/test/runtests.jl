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