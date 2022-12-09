module Day03

function common_letters(v)
  for n in v[1]
    all(n ∈ x for x in v[2:end]) && return n
  end
end

function letter_value(letter)
  if letter in 'a':'z'
    return letter - 'a' + 1
  else
    return letter - 'A' + 27
  end
end

function part1(input="input.txt")
  rucksacks = []
  for line in eachline(input)
    half = div(length(line), 2)
    half_lines = (line[1:half], line[half+1:end])
    l = common_letters(half_lines)
    push!(rucksacks, l)
  end
  return sum(letter_value.(rucksacks))
end

function part2(input="input.txt")
  lines = readlines(input)
  rucksacks = []
  group = []
  for (i, line) in enumerate(lines)
    push!(group, line)
    if i % 3 == 0 || line == last(lines)
      l = common_letters(group)
      push!(rucksacks, l)
      group = []
    end
  end
  return sum(letter_value.(rucksacks))
end

end