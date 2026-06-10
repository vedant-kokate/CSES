use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut stdin_lock = stdin.lock();

    let mut buf = String::new();
    stdin_lock.read_line(&mut buf).unwrap();
    let n: usize = buf.trim().parse().unwrap();
    let mut grid: Vec<Vec<char>> = Vec::with_capacity(n);

    for _ in 0..n {
        buf.clear();
        stdin_lock.read_line(&mut buf).unwrap();
        let row: Vec<char> = buf.trim_end().chars().collect();
        grid.push(row);
    }

    let mut dist: Vec<Vec<Option<String>>> = vec![vec![None; n]; n];
    let start = grid[0][0].to_string();
    dist[0][0] = Some(start.clone());

    let mut heap: BinaryHeap<Reverse<(String, usize, usize)>> = BinaryHeap::new();
    heap.push(Reverse((start, 0, 0)));

    while let Some(Reverse((path, i, j))) = heap.pop() {
        if let Some(current) = &dist[i][j] {
            if *current != path {
                continue;
            }
        }

        if i == n - 1 && j == n - 1 {
            println!("{}", path);
            break;
        }

        for &(di, dj) in &[(1, 0), (0, 1)] {
            let ni = i.wrapping_add(di);
            let nj = j.wrapping_add(dj);
            if ni < n && nj < n {
                let mut next_path = path.clone();
                next_path.push(grid[ni][nj]);
                let update = match &dist[ni][nj] {
                    Some(existing) => next_path < *existing,
                    None => true,
                };
                if update {
                    dist[ni][nj] = Some(next_path.clone());
                    heap.push(Reverse((next_path, ni, nj)));
                }
            }
        }
    }
}
