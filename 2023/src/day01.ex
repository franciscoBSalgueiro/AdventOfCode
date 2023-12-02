defmodule Day01 do
  def part1(input) do
    input
    |> String.split()
    |> Enum.map(fn line ->
      String.split(line, "")
      |> Enum.map(fn char ->
        case Integer.parse(char) do
          :error -> nil
          {n, _} -> n
        end
      end)
      |> Enum.filter(&(&1 != nil))
    end)
    |> Enum.map(fn list ->
      List.first(list) * 10 + List.last(list)
    end)
    |> Enum.sum()
  end

  def part2(input) do
    input
    |> String.split()
    |> Enum.map(fn line ->
      [first_match] = Regex.run(~r{\d|one|two|three|four|five|six|seven|eight|nine}, line)

      [last_match] =
        Regex.run(~r{\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin}, String.reverse(line))

      [first_match, String.reverse(last_match)]
      |> Enum.map(fn match ->
        case Integer.parse(match) do
          :error ->
            case match do
              "one" -> 1
              "two" -> 2
              "three" -> 3
              "four" -> 4
              "five" -> 5
              "six" -> 6
              "seven" -> 7
              "eight" -> 8
              "nine" -> 9
            end

          {n, _} ->
            n
        end
      end)
    end)
    |> Enum.map(fn list ->
      List.first(list) * 10 + List.last(list)
    end)
    |> Enum.sum()
  end
end

input = File.read!("inputs/day01.txt")

Day01.part1(input) |> IO.inspect()
Day01.part2(input) |> IO.inspect()
