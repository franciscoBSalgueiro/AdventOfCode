defmodule Day02 do
  def parse_color(color, line) do
    Regex.scan(~r{(\d+) #{color}}, line)
    |> Enum.map(fn [_, n] -> String.to_integer(n) end)
  end

  def part1(input) do
    input
    |> String.split("\n")
    |> Enum.with_index(1)
    |> Enum.map(fn {line, i} ->
      blue = parse_color("blue", line)
      red = parse_color("red", line)
      green = parse_color("green", line)

      if Enum.find(blue, fn n -> n > 14 end) != nil or
           Enum.find(red, fn n -> n > 12 end) != nil or
           Enum.find(green, fn n -> n > 13 end) != nil do
        0
      else
        i
      end
    end)
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> String.split("\n")
    |> Enum.map(fn line ->
      blue = parse_color("blue", line)
      red = parse_color("red", line)
      green = parse_color("green", line)

      Enum.max(blue) * Enum.max(red) * Enum.max(green)
    end)
    |> Enum.sum()
  end
end

input = File.read!("inputs/day02.txt")

Day02.part1(input) |> IO.inspect()
Day02.part2(input) |> IO.inspect()
