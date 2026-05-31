use std::collections::HashMap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();
    if nums.is_empty() {
        return;
    }
    let n = nums[0] as usize;
    let x = nums[1];
    let mut count: i64 = 0;
    let mut sum: i64 = 0;
    let mut dp: HashMap<i64, i64> = HashMap::new();
    dp.insert(0, 1);
    let values = &nums[2..];
    for &value in values.iter().take(n) {
        sum += value;
        let need = sum - x;
        count += *dp.get(&need).unwrap_or(&0);
        *dp.entry(sum).or_insert(0) += 1;
    }
    println!("{}", count);
}
