use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();

    let m: usize = it.next().unwrap().parse().unwrap();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut c: Vec<usize> = Vec::with_capacity(m);
    for _ in 0..m {
        c.push(it.next().unwrap().parse().unwrap());
    }
    c.sort_unstable();

    const MOD: usize = 1_000_000_007;
    let mut dp = vec![0usize; n + 1];
    dp[0] = 1;
    for i in 1..=n {
        let mut sum = 0;
        for &x in &c {
            if x > i {
                break;
            }
            sum = (sum + dp[i - x]) % MOD;
        }
        dp[i] = sum;
    }

    println!("{}", dp[n] % MOD);
}
