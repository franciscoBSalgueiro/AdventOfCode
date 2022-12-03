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

function part1()
  rucksacks = []
  for line in eachline("input.txt")
    half = div(length(line), 2)
    half_lines = (line[1:half], line[half+1:end])
    l = common_letters(half_lines)
    push!(rucksacks, l)
  end
  println(sum(letter_value.(rucksacks)))
end

function part2()
  lines = readlines("input.txt")
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
  println(sum(letter_value.(rucksacks)))
end

part1()
part2()
