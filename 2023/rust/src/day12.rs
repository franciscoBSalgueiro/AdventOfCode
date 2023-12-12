use aoc_runner_derive::{aoc, aoc_generator};
use std::hash::{Hash, Hasher};
use rustc_hash::{FxHashMap, FxHasher};
type Input = Vec<(String, Vec<usize>)>;

#[aoc_generator(day12)]
fn input_generator(input: &str) -> Input {
    let lines = input.lines();
    let mut rows: Vec<(String, Vec<usize>)> = Vec::new();

    for l in lines {
        let mut parts = l.split_whitespace();
        let values = parts.next().unwrap().to_string();
        let counts: Vec<usize> = parts
            .next()
            .unwrap()
            .split(',')
            .map(|x| x.parse().unwrap())
            .collect();
        rows.push((values, counts));
    }
    rows
}

fn count_poss(values: &str, counts: &[usize], memo: &mut FxHashMap<u64, usize>) -> usize {
    let mut hasher = FxHasher::default();
    values.hash(&mut hasher);
    counts.hash(&mut hasher);
    let key = hasher.finish();

    if let Some(&result) = memo.get(&key) {
        return result;
    }

    let result = if values.is_empty() && counts.is_empty() {
        1
    } else if values.is_empty() && !counts.is_empty() {
        0
    } else if counts.is_empty() {
        if values.chars().any(|x| x == '#') {
            0
        } else {
            1
        }
    } else if values.len() < counts.iter().sum() {
        0
    } else if values.starts_with('.') {
        // strip all leading dots
        count_poss(values.trim_start_matches('.'), counts, memo)

        // strip one leading dot
        // count_poss(values.strip_prefix('.').unwrap(), counts, memo)
    
    } else if values.starts_with('?') {
        let stripped = values.strip_prefix('?').unwrap();
        count_poss(&format!("#{stripped}"), counts, memo)
            + count_poss(&format!(".{stripped}"), counts, memo)
    } else if values.starts_with('#') {
        let v = counts[0];
        if (values.chars().take(v).any(|x| x == '.'))
            || (values.len() > v && values.chars().nth(v).unwrap() == '#')
        {
            0
        } else if values.len() > v {
            count_poss(&values[v + 1..], &counts[1..], memo)
        } else {
            count_poss("", &counts[1..], memo)
        }
    } else {
        unreachable!();
    };

    memo.insert(key, result);
    result
}

#[aoc(day12, part1)]
fn part1(input: &Input) -> usize {
    let mut memo: FxHashMap<u64, usize> = FxHashMap::default();

    let total_possibilities: Vec<usize> = input
        .iter()
        .map(|(values, counts)| count_poss(values, counts, &mut memo))
        .collect();

    return total_possibilities.iter().sum::<usize>();
}

#[aoc(day12, part2)]
fn part2(input: &Input) -> usize {
    let mut memo: FxHashMap<u64, usize> = FxHashMap::default();

    let rows: Vec<_> = input
        .iter()
        .map(|(values, counts)| {
            return (
                format! {"{values}?"}
                    .repeat(5)
                    .strip_suffix('?')
                    .unwrap()
                    .to_string(),
                counts.repeat(5),
            );
        })
        .collect();

    let total_possibilities: Vec<usize> = rows
        .iter()
        .map(|(values, counts)| count_poss(values, counts, &mut memo))
        .collect();
    return total_possibilities.iter().sum::<usize>();
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = include_str!("examples/day12_example.txt");

    #[test]
    fn test_part1() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part1(&input), 21);
    }

    #[test]
    fn test_part2() {
        let input = input_generator(TEST_INPUT);
        assert_eq!(part2(&input), 525152);
    }
}
