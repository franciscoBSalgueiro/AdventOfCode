fn parse_input(input: &str) -> Vec<usize> {
    input.split(",").filter_map(|line| line.parse().ok()).collect()
}

fn opcode(input: &mut Vec<usize>) -> usize {
    let mut i = 0;
    loop {
        if input[i] == 99 {
            break
        } else if input[i] == 1 || input[i] == 2 {
            let ind3 = input[i+3];
            let ind2 = input[i+2];
            let ind1 = input[i+1];
            if input[i] == 1 {
                input[ind3] = input[ind2] + input[ind1];
            } else if input[i] == 2 {
                input[ind3] = input[ind2] * input[ind1];   
            }
            i+=4;
            continue;
        }
        i += 1;
    }
    input[0]
}

fn main() {
    let mut input = parse_input(&std::fs::read_to_string("input.txt").unwrap());

    // Part 1
    input[1]=12;
    input[2]=2;
    println!("{}",opcode(&mut input));


    // Part 2

    for n in 0..99 {
        for v in 0..99 {
            let mut input = parse_input(&std::fs::read_to_string("input.txt").unwrap());
            input[1]=n;
            input[2]= v;
            if opcode(&mut input) == 19690720 {
                println!("{}", 100*n+v);
                break
            }
        }
    }
}