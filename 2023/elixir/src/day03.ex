defmodule Day03 do
  def isSymbol(char) do
    char != "." && Integer.parse(char) == :error
  end

  def adjacentSquares(lines, x, y) do
    possible = [
      {x - 1, y - 1},
      {x, y - 1},
      {x + 1, y - 1},
      {x - 1, y},
      {x + 1, y},
      {x - 1, y + 1},
      {x, y + 1},
      {x + 1, y + 1}
    ]

    Enum.filter(possible, fn {x, y} ->
      x >= 0 && y >= 0 && y < Enum.count(lines) && x < String.length(Enum.at(lines, y))
    end)
  end

  def part1(input) do
    lines = String.split(input, "\n")

    lines
    |> Enum.with_index()
    |> Enum.map(fn {line, i} ->
      Regex.scan(~r/\d+/, line, return: :index)
      |> Enum.map(fn [{b, l}] ->
        hasSymbol =
          b..(b + l - 1)
          |> Enum.map(fn j -> {j, i} end)
          |> Enum.map(fn {x, y} -> adjacentSquares(lines, x, y) end)
          |> List.flatten()
          |> Enum.any?(fn {x, y} -> isSymbol(Enum.at(lines, y) |> String.at(x)) end)

        if hasSymbol do
          String.to_integer(String.slice(line, b..(b + l - 1)))
        else
          0
        end
      end)
      |> Enum.sum()
    end)
    |> Enum.sum()
  end

  def part2(input) do
    lines = String.split(input, "\n")

    lines
    |> Enum.with_index()
    |> Enum.reduce(Map.new(), fn {line, i}, acc ->
      Regex.scan(~r/\d+/, line, return: :index)
      |> Enum.reduce(acc, fn [{b, l}], acc ->
        hasSymbol =
          b..(b + l - 1)
          |> Enum.map(fn j -> {j, i} end)
          |> Enum.map(fn {x, y} -> adjacentSquares(lines, x, y) end)
          |> List.flatten()
          |> Enum.find(fn {x, y} -> isSymbol(Enum.at(lines, y) |> String.at(x)) end)

        newAcc =
          if hasSymbol != nil do
            char = Enum.at(lines, hasSymbol |> elem(1)) |> String.at(hasSymbol |> elem(0))

            if char == "*" do
              adj =
                adjacentSquares(lines, hasSymbol |> elem(0), hasSymbol |> elem(1))
                |> Enum.map(fn {x, y} -> Enum.at(lines, y) |> String.at(x) end)

              chunks =
                [
                  Enum.slice(adj, 0, 3),
                  Enum.slice(adj, 3, 1),
                  Enum.slice(adj, 4, 1),
                  Enum.slice(adj, 5, 3)
                ]
                |> Enum.map(fn x ->
                  joined = Enum.join(x)
                  Regex.scan(~r/\d+/, joined)
                end)
                |> List.flatten()

              if Enum.count(chunks) == 2 do
                n = String.slice(line, b..(b + l - 1)) |> String.to_integer()
                prev = Map.get(acc, hasSymbol)

                if prev != nil do
                  Map.put(Map.new(), hasSymbol, prev * n)
                else
                  Map.put(Map.new(), hasSymbol, n)
                end
              end
            end
          end

        if newAcc == nil do
          acc
        else
          Map.merge(acc, newAcc)
        end
      end)
    end)
    |> Map.values()
    |> Enum.sum()
  end
end

input = File.read!("inputs/day03.txt")

Day03.part1(input) |> IO.inspect()
Day03.part2(input) |> IO.inspect()
