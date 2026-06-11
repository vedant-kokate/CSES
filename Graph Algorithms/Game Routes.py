import sys
from collections import deque

input = sys.stdin.readline
MOD = 10**9 + 7

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    indeg = [0] * n

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        indeg[b] += 1

    q = deque(i for i in range(n) if indeg[i] == 0)
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    ways = [0] * n
    ways[0] = 1
    for u in topo:
        for v in g[u]:
            ways[v] = (ways[v] + ways[u]) % MOD

    print(ways[n - 1])


if __name__ == '__main__':
    main()