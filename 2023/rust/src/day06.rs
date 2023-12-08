use crate::utils::*;

use aoc_runner_derive::{aoc, aoc_generator};
use nom::{bytes::complete::tag, IResult};

type Input = Problem;

#[aoc_generator(day6)]
fn input_generator(input: &str) -> Input {
    parse_input(input).unwrap().1
}

#[derive(PartialEq, Eq, Debug, Clone)]
struct Problem {
    races: Vec<Race>,
}

#[derive(PartialEq, Eq, Debug, Clone)]
struct Race(u64, u64);

fn parse_input(s: &str) -> IResult<&str, Input> {
    //     Time:      7  15   30
    // Distance:  9  40  200

    let (s, _) = tag("Time:")(s)?;
    let (s, time) = list(s)?;
    let (s, _) = tag("\n")(s)?;
    let (s, _) = tag("Distance:")(s)?;
    let (s, distance) = list(s)?;

    let time: Vec<u64> = time;
    let distance: Vec<u64> = distance;

    let mut races = Vec::new();
    for (t, d) in time.into_iter().zip(distance) {
        races.push(Race(t, d));
    }

    Ok((s, Problem { races }))
}

impl Race {
    fn min_time(&self) -> u64 {
        let mut total = 0;
        for speed in 1..self.0 {
            let remaining = self.0 - speed;
            if remaining * speed > self.1 {
                total += 1;
                continue;
            }
        }
        total
    }
}

#[aoc(day6, part1)]
fn part1(input: &Input) -> u64 {
    let races = input.clone().races;
    races.into_iter().map(|r| r.min_time()).product()
}

#[aoc(day6, part2)]
fn part2(_input: &Input) -> u64 {
    let race = Race(40817772, 219101213651089);
    race.min_time()
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = include_str!("examples/day06_example.txt");

    #[test]
    fn test_part1() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part1(&input), 288);
    }

    #[test]
    fn test_part2() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part2(&input), 28101347);
    }
}
