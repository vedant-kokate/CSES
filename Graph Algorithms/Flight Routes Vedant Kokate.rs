use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let mut k: usize = it.next().unwrap().parse().unwrap();

    let mut g: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
    for _ in 0..m {
        let a: usize = it.next().unwrap().parse().unwrap();
        let b: usize = it.next().unwrap().parse().unwrap();
        let c: i64 = it.next().unwrap().parse().unwrap();
        g[a - 1].push((b - 1, c));
    }

    let mut q: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
    q.push(Reverse((0, 0)));
    let mut count = vec![0usize; n];
    let K = k;
    let mut ans = Vec::new();

    while k > 0 {
        if let Some(Reverse((d, node))) = q.pop() {
            if count[node] <= K {
                count[node] += 1;
                if node == n - 1 {
                    k -= 1;
                    ans.push(d);
                }
                for &(next_node, dist) in &g[node] {
                    q.push(Reverse((d + dist, next_node)));
                }
            }
        } else {
            break;
        }
    }

    let output = ans.iter().map(|v| v.to_string()).collect::<Vec<_>>().join(" ");
    println!("{}", output);
}
