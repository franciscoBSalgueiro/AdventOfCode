fn solve(part: i32) {
    let mut passwords = 0;
    for n in 356261..846304 {
        let n_str = n.to_string();
        let mut repetido = false;
        let mut decresce = false;
        let mut anterior = 0;
        for c in n_str.chars() {
            let atual = c.to_digit(10).unwrap();
            if atual<anterior {
                decresce = true;
                break;
            }
            if !repetido && anterior == atual {
                if part==1 || (part==2 && !n_str.contains(&c.to_string().repeat(3))) {
                    repetido = true;
                }
            }
            anterior = atual;
        }
        if repetido && !decresce{
            passwords += 1;
        }
    }
    println!("{}",passwords)
}

fn main() {
    solve(1);
    solve(2);
}
