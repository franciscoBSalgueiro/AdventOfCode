defmodule Day04 do
  def get_intersecting(line) do
    [first, last] =
      String.replace(line, ~r/Card\s+\d+: /, "")
      |> String.split("|")
      |> Enum.map(fn group ->
        String.split(group)
        |> Enum.map(fn match -> String.to_integer(match) end)
        |> MapSet.new()
      end)

    MapSet.intersection(first, last) |> MapSet.size()
  end

  def part1(input) do
    input
    |> String.split("\n")
    |> Enum.map(fn line ->
      n = get_intersecting(line)
      if n == 0, do: 0, else: 2 ** (n - 1)
    end)
    |> Enum.sum()
  end

  def part2(input) do
    lines = String.split(input, "\n")

    lines
    |> Enum.with_index()
    |> Enum.reduce(List.duplicate(1, length(lines)), fn {line, i}, acc ->
      n = get_intersecting(line)

      n_cards = elem(List.to_tuple(acc), i)

      if n == 0 do
        acc
      else
        acc
        |> Enum.with_index()
        |> Enum.map(fn {el, j} ->
          if i < j && j <= i + n do
            el + n_cards
          else
            el
          end
        end)
      end
    end)
    |> Enum.sum()
  end
end

input = File.read!("inputs/day04.txt")

Day04.part1(input) |> IO.inspect()
Day04.part2(input) |> IO.inspect()
