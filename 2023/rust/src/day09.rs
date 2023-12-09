use aoc_runner_derive::{aoc, aoc_generator};

type Input = Problem;

#[aoc_generator(day9)]
fn input_generator(input: &str) -> Input {
    let lines = input.lines();
    let mut problem = Problem::default();
    for line in lines {
        problem.history.push(
            line.split_whitespace()
                .map(|s| s.parse().unwrap())
                .collect(),
        );
    }
    problem
}

#[derive(Debug, Clone, Default, PartialEq, Eq)]
struct Problem {
    history: Vec<Vec<i64>>,
}

fn calculate_diffs(positions: Vec<i64>) -> Vec<i64> {
    let mut diffs = Vec::new();
    for i in 1..positions.len() {
        diffs.push(positions[i] - positions[i - 1]);
    }
    diffs
}

fn calculate_diff_layers(positions: Vec<i64>) -> Vec<Vec<i64>> {
    let mut layers = Vec::new();
    let mut new_layer = positions.clone();
    while new_layer.iter().any(|&p| p != 0) {
        layers.push(new_layer.clone());
        new_layer = calculate_diffs(new_layer);
    }
    layers.push(new_layer);
    layers
}

fn predict_next_position(layers: Vec<Vec<i64>>) -> i64 {
    let mut next_position = 0;
    for layer in layers.iter().rev() {
        next_position += layer[layer.len() - 1];
    }
    next_position
}


fn predict_next_position_2(layers: Vec<Vec<i64>>) -> i64 {
    let mut next_position = 0;
    for layer in layers.iter().rev() {
        next_position = layer[0] - next_position;
    }
    next_position
}


#[aoc(day9, part1)]
fn part1(input: &Input) -> i64 {
    let h: Vec<Vec<Vec<i64>>> = input
        .history
        .iter()
        .map(|h| calculate_diff_layers(h.clone()))
        .collect();
    let next_pos = h
        .iter()
        .map(|h| predict_next_position(h.clone()))
        .collect::<Vec<_>>();
    next_pos.iter().sum()
}

#[aoc(day9, part2)]
fn part2(input: &Input) -> i64 {
    let h: Vec<Vec<Vec<i64>>> = input
        .history
        .iter()
        .map(|h| calculate_diff_layers(h.clone()))
        .collect();
    let next_pos = h
        .iter()
        .map(|h| predict_next_position_2(h.clone()))
        .collect::<Vec<_>>();

        next_pos.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = include_str!("examples/day09_example.txt");

    #[test]
    fn test_part1() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part1(&input), 114);
    }

    #[test]
    fn test_part2() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part2(&input), 2);
    }
}
