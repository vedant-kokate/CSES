import sys

MOD = 10**9 + 7
input = sys.stdin.readline

def build_transitions(n):
    max_mask = 1 << n
    transitions = [[] for _ in range(max_mask)]

    def dfs(row, mask, next_mask):
        if row == n:
            transitions[mask].append(next_mask)
            return
        if mask >> row & 1:
            dfs(row + 1, mask, next_mask)
            return

        # place vertical tile in this column
        if row + 1 < n and not (mask >> (row + 1) & 1):
            dfs(row + 2, mask, next_mask)

        # place horizontal tile to the next column
        dfs(row + 1, mask, next_mask | (1 << row))

    for mask in range(max_mask):
        dfs(0, mask, 0)

    return transitions


def main():
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])

    transitions = build_transitions(n)
    max_mask = 1 << n
    dp = [0] * max_mask
    dp[0] = 1

    for _ in range(m):
        next_dp = [0] * max_mask
        for mask in range(max_mask):
            if dp[mask] == 0:
                continue
            ways = dp[mask]
            for next_mask in transitions[mask]:
                next_dp[next_mask] = (next_dp[next_mask] + ways) % MOD
        dp = next_dp

    print(dp[0])


if __name__ == '__main__':
    main()
