use std::collections::HashMap;

use aoc_runner_derive::aoc;

fn parse_hand1(s: &str) -> Hand1 {
    let x = s.split_whitespace().collect::<Vec<_>>();
    let cards = x[0].chars().map(Card1::from_char).collect();
    let bid = x[1].parse::<u64>().unwrap();
    Hand1 { cards, bid }
}

fn parse_hand2(s: &str) -> Hand2 {
    let x = s.split_whitespace().collect::<Vec<_>>();
    let cards = x[0].chars().map(Card2::from_char).collect();
    let bid = x[1].parse::<u64>().unwrap();
    Hand2 { cards, bid }
}

#[derive(PartialEq, Eq, Debug, Clone, PartialOrd, Ord)]
enum Kind {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

impl Kind {
    fn from_counts(counts: &[u64]) -> Kind {
        match counts {
            [1, 1, 1, 1, 1] => Kind::HighCard,
            [1, 1, 1, 2] => Kind::OnePair,
            [1, 2, 2] => Kind::TwoPair,
            [1, 1, 3] => Kind::ThreeOfAKind,
            [2, 3] => Kind::FullHouse,
            [1, 4] => Kind::FourOfAKind,
            [5] => Kind::FiveOfAKind,
            _ => panic!("Invalid hand"),
        }
    }
}

#[derive(PartialEq, Eq, Debug, Clone, PartialOrd, Ord, Hash)]
enum Card1 {
    N(u64),
    T,
    J,
    Q,
    K,
    A,
}

#[derive(PartialEq, Eq, Debug, Clone, PartialOrd, Ord, Hash)]
enum Card2 {
    J,
    N(u64),
    T,
    Q,
    K,
    A,
}

impl Card1 {
    fn from_char(c: char) -> Card1 {
        match c {
            'A' => Card1::A,
            'K' => Card1::K,
            'Q' => Card1::Q,
            'J' => Card1::J,
            'T' => Card1::T,
            _ => Card1::N(c.to_digit(10).unwrap() as u64),
        }
    }
}

impl Card2 {
    fn from_char(c: char) -> Card2 {
        match c {
            'A' => Card2::A,
            'K' => Card2::K,
            'Q' => Card2::Q,
            'J' => Card2::J,
            'T' => Card2::T,
            _ => Card2::N(c.to_digit(10).unwrap() as u64),
        }
    }
}

#[derive(PartialEq, Eq, Debug, Clone)]
struct Hand1 {
    cards: Vec<Card1>,
    bid: u64,
}

#[derive(PartialEq, Eq, Debug, Clone)]
struct Hand2 {
    cards: Vec<Card2>,
    bid: u64,
}

impl Hand1 {
    fn get_kind(&self) -> Kind {
        let mut counts = HashMap::new();
        for c in self.cards.iter() {
            let count = counts.entry(c).or_insert(0);
            *count += 1;
        }
        let mut counts = counts.into_iter().collect::<Vec<_>>();
        counts.sort_by(|a, b| b.1.cmp(&a.1));
        let mut counts = counts.into_iter().map(|(_, v)| v).collect::<Vec<_>>();
        counts.sort();
        Kind::from_counts(&counts)
    }
}
impl Hand2 {
    fn get_kind(&self) -> Kind {
        let mut counts = HashMap::new();
        for c in self.cards.iter() {
            let count = counts.entry(c).or_insert(0);
            *count += 1;
        }
        if counts.len() == 1 {
            return Kind::FiveOfAKind;
        }

        let mut best_kind = Kind::HighCard;

        for k in [
            Card2::A,
            Card2::K,
            Card2::Q,
            Card2::T,
            Card2::N(9),
            Card2::N(8),
            Card2::N(7),
            Card2::N(6),
            Card2::N(5),
            Card2::N(4),
            Card2::N(3),
            Card2::N(2),
        ] {
            let mut counts = counts.clone();
            if !self.cards.contains(&k) {
                continue;
            }
            if self.cards.contains(&Card2::J) {
                let j_count = *counts.entry(&Card2::J).or_insert(0);
                counts.remove(&Card2::J);
                let count = counts.entry(&k).or_insert(0);
                *count += j_count;
            }

            let mut counts = counts.into_iter().collect::<Vec<_>>();
            counts.sort_by(|a, b| b.1.cmp(&a.1));
            let mut counts = counts.into_iter().map(|(_, v)| v).collect::<Vec<_>>();
            counts.sort();
            let kind = Kind::from_counts(&counts);
            if kind > best_kind {
                best_kind = kind;
            }
        }
        best_kind
    }
}

#[aoc(day7, part1)]
fn part1(input: &str) -> u64 {
    let lines = input.lines().collect::<Vec<_>>();
    let mut hands: Vec<Hand1> = lines.iter().map(|l| parse_hand1(l)).collect();

    hands.sort_by(|a, b| {
        let kind_a = a.get_kind();
        let kind_b = b.get_kind();
        if kind_a == kind_b {
            for (i, card) in a.cards.iter().enumerate() {
                let cmp = card.cmp(&b.cards[i]);
                if cmp != std::cmp::Ordering::Equal {
                    return cmp;
                }
            }
            std::cmp::Ordering::Equal
        } else {
            kind_a.cmp(&kind_b)
        }
    });

    let mut total = 0;
    for (i, hand) in hands.iter().enumerate() {
        total += hand.bid * (i as u64 + 1);
    }

    total
}

#[aoc(day7, part2)]
fn part2(input: &str) -> u64 {
    let lines = input.lines().collect::<Vec<_>>();
    let mut hands: Vec<Hand2> = lines.iter().map(|l| parse_hand2(l)).collect();

    hands.sort_by(|a, b| {
        let kind_a = a.get_kind();
        let kind_b = b.get_kind();
        if kind_a == kind_b {
            for (i, card) in a.cards.iter().enumerate() {
                let cmp = card.cmp(&b.cards[i]);
                if cmp != std::cmp::Ordering::Equal {
                    return cmp;
                }
            }
            std::cmp::Ordering::Equal
        } else {
            kind_a.cmp(&kind_b)
        }
    });

    let mut total = 0;
    for (i, hand) in hands.iter().enumerate() {
        total += hand.bid * (i as u64 + 1);
    }

    total
}

#[cfg(test)]
mod tests {
    use super::*;

    const TEST_INPUT: &str = include_str!("examples/day07_example.txt");

    #[test]
    fn test_part1() {
        assert_eq!(part1(TEST_INPUT), 6440);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(TEST_INPUT), 5905);
    }
}
