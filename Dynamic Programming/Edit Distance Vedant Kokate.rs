use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let a = match lines.next() {
        Some(line) => line.to_string(),
        None => return,
    };
    let b = match lines.next() {
        Some(line) => line.to_string(),
        None => return,
    };

    let n = a.len();
    let m = b.len();
    let mut dp = vec![vec![0; m + 1]; n + 1];

    for i in 0..=n {
        dp[i][0] = i;
    }
    for j in 0..=m {
        dp[0][j] = j;
    }

    for i in 1..=n {
        for j in 1..=m {
            if a.as_bytes()[i - 1] != b.as_bytes()[j - 1] {
                dp[i][j] = 1 + dp[i - 1][j].min(dp[i - 1][j - 1]).min(dp[i][j - 1]);
            } else {
                dp[i][j] = dp[i - 1][j - 1];
            }
        }
    }

    println!("{}", dp[n][m]);
}
