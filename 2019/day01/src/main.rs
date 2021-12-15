fn parse_input(input: &str) -> Vec<i64> {
    input.lines().filter_map(|line| line.parse().ok()).collect()
}

fn fuel_calculator(n: i64) -> i64 {
    let fuel = n / 3 - 2;
    if fuel>0 {
        fuel
    } else { 0 }
}


fn main() {
    let modules = parse_input(&std::fs::read_to_string("input.txt").unwrap());
    // Part 1
    let mut total_fuel = 0;
    for m in &modules {
        total_fuel += fuel_calculator(*m);
    }
    println!("{}",total_fuel);

    // Part 2
    let mut total_fuel = 0;
    for m in &modules {
        let mut restante = *m;
        loop {
            let fuel = fuel_calculator(restante);
            total_fuel += fuel;
            restante = fuel;
            if restante == 0 {
                break
            }
        }
    }
    println!("{}",total_fuel)
}
