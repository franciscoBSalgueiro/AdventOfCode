use std::collections::HashMap;

use aoc_runner_derive::{aoc, aoc_generator};

type Input = Problem;

#[aoc_generator(day8)]
fn input_generator(input: &str) -> Input {
    let mut lines = input.lines();
    let instructions = lines
        .next()
        .unwrap()
        .chars()
        .map(|c| match c {
            'R' => Direction::Right,
            'L' => Direction::Left,
            _ => panic!("Invalid direction"),
        })
        .collect();
    let mut location = HashMap::new();
    lines.next();
    for line in lines {
        let line = line.replace(['(', ')'], "");
        let mut parts = line.split(" = ");
        let name = parts.next().unwrap();
        let mut parts = parts.next().unwrap().split(", ");
        let left = parts.next().unwrap();
        let right = parts.next().unwrap();
        location.insert(name.to_string(), (left.to_string(), right.to_string()));
    }
    Problem {
        instructions,
        location,
    }
}

#[derive(PartialEq, Eq, Debug, Clone)]
struct Problem {
    instructions: Vec<Direction>,
    location: HashMap<String, (String, String)>,
}

#[derive(PartialEq, Eq, Debug, Clone)]
enum Direction {
    Right,
    Left,
}

fn calculate_distance(input: &Input, start: &str, end: &dyn Fn(&str) -> bool) -> usize {
    let mut cur = start.to_string();
    let mut cur_instr = input.instructions[0].clone();
    let mut count = 0;
    while !end(&cur) {
        let (left, right) = input.location.get(&cur).unwrap();
        if cur_instr == Direction::Right {
            cur = right.to_string();
        } else {
            cur = left.to_string();
        }
        count += 1;
        cur_instr = input.instructions[count % input.instructions.len()].clone();
    }
    count
}

#[aoc(day8, part1)]
fn part1(input: &Input) -> u64 {
    calculate_distance(input, "AAA", &|s| s == "ZZZ") as u64
}

#[aoc(day8, part2)]
fn part2(input: &Input) -> usize {
    input
        .location
        .iter()
        .filter(|(k, _)| k.ends_with('A'))
        .map(|(name, _)| name.to_string())
        .map(|name| calculate_distance(input, &name, &|s| s.ends_with('Z')))
        .reduce(lcm)
        .unwrap()
}

fn lcm(a: usize, b: usize) -> usize {
    a * b / gcd(a, b)
}

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = include_str!("examples/day08_example.txt");

    #[test]
    fn test_part1() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part1(&input), 2);
    }

    const TEST_INPUT2: &str = include_str!("examples/day08-2_example.txt");

    #[test]
    fn test_part2() {
        let input = input_generator(TEST_INPUT2);
        assert_eq!(part2(&input), 6);
    }
}
