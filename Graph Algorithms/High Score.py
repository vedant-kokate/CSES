import sys
from collections import deque

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    edges = []
    rev = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, x = map(int, input().split())
        edges.append((a, b, x))
        rev[b].append(a)

    can_reach_n = [False] * (n + 1)
    dq = deque([n])
    can_reach_n[n] = True
    while dq:
        u = dq.popleft()
        for v in rev[u]:
            if not can_reach_n[v]:
                can_reach_n[v] = True
                dq.append(v)

    dist = [-10**30] * (n + 1)
    dist[1] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, x in edges:
            if dist[u] != -10**30 and dist[u] + x > dist[v]:
                dist[v] = dist[u] + x
                updated = True
        if not updated:
            break

    for u, v, x in edges:
        if dist[u] != -10**30 and dist[u] + x > dist[v] and can_reach_n[v]:
            print(-1)
            return

    print(dist[n])


if __name__ == '__main__':
    main()
