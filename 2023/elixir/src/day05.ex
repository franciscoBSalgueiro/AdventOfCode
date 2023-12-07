defmodule Day05 do
  def process_1(n, ranges) do
    for {dst, src, len} <- ranges, n in src..(src + len) do
      dst + (n - src)
    end
    |> Enum.min(fn -> n end)
  end

  def get_maps(lines, i) do
    elem(List.to_tuple(lines), i)
    |> String.split("\n")
    |> Enum.drop(1)
    |> Enum.map(fn y -> String.split(y, " ") |> Enum.map(fn z -> String.to_integer(z) end) end)
    |> Enum.map(fn [dst, src, len] -> {dst, src, len} end)
  end

  def part1(input) do
    lines =
      input
      |> String.split("\n\n")

    seeds =
      elem(List.to_tuple(lines), 0)
      |> String.split(" ")
      |> Enum.drop(1)
      |> Enum.map(&String.to_integer/1)

    seed_soil = get_maps(lines, 1)
    soil_fertilizer = get_maps(lines, 2)
    fertilizer_water = get_maps(lines, 3)
    water_light = get_maps(lines, 4)
    light_temperature = get_maps(lines, 5)
    temperature_humidity = get_maps(lines, 6)
    humidity_location = get_maps(lines, 7)

    for seed <- seeds do
      process_1(seed, seed_soil)
      |> process_1(soil_fertilizer)
      |> process_1(fertilizer_water)
      |> process_1(water_light)
      |> process_1(light_temperature)
      |> process_1(temperature_humidity)
      |> process_1(humidity_location)
    end
    |> Enum.min()
  end

  def process_2({start, last}, maps) do
    if length(maps) == 0 do
      [{start, last}]
    else
      [{src_start, src_stop, diff} | rest] = maps

      cond do
        start >= src_start and last <= src_stop ->
          [{start - diff, last - diff}]

        start < src_start and last in src_start..src_stop ->
          [
            {start, src_start - 1},
            {src_start - diff, last - diff}
          ]

        start in src_start..src_stop ->
          [
            {start - diff, src_stop - diff}
            | process_2({src_stop + 1, last}, rest)
          ]

        true ->
          process_2({start, last}, rest)
      end
    end
  end

  def get_maps2(lines, i) do
    get_maps(lines, i)
    |> Enum.map(fn {dst, src, len} -> {src, src + len - 1, src - dst} end)
    |> Enum.sort_by(&elem(&1, 0))
  end

  def part2(input) do
    lines =
      input
      |> String.split("\n\n")

    seeds =
      elem(List.to_tuple(lines), 0)
      |> String.split(" ")
      |> Enum.drop(1)
      |> Enum.chunk_every(2)
      |> Enum.map(fn [start, len] ->
        start = String.to_integer(start)
        len = String.to_integer(len)
        {start, start + len}
      end)

    # IO.inspect(seeds)

    seed_soil = get_maps2(lines, 1)
    soil_fertilizer = get_maps2(lines, 2)
    fertilizer_water = get_maps2(lines, 3)
    water_light = get_maps2(lines, 4)
    light_temperature = get_maps2(lines, 5)
    temperature_humidity = get_maps2(lines, 6)
    humidity_location = get_maps2(lines, 7)

    seeds
    |> Enum.map(fn seed ->
      Task.async(fn ->
        process_2(seed, seed_soil)
        |> Enum.flat_map(fn x -> process_2(x, soil_fertilizer) end)
        |> Enum.flat_map(fn x -> process_2(x, fertilizer_water) end)
        |> Enum.flat_map(fn x -> process_2(x, water_light) end)
        |> Enum.flat_map(fn x -> process_2(x, light_temperature) end)
        |> Enum.flat_map(fn x -> process_2(x, temperature_humidity) end)
        |> Enum.flat_map(fn x -> process_2(x, humidity_location) end)
      end)
    end)
    |> Enum.flat_map(fn x -> Task.await(x) end)
    |> Enum.min()
    |> elem(0)
  end
end

input = File.read!("inputs/day05.txt")

Day05.part1(input) |> IO.inspect()
Day05.part2(input) |> IO.inspect()
