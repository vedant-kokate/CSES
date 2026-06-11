import sys
from collections import deque

input = sys.stdin.readline

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

    dist = [-10**18] * n
    parent = [-1] * n
    dist[0] = 1

    for u in topo:
        if dist[u] < 0:
            continue
        for v in g[u]:
            if dist[u] + 1 > dist[v]:
                dist[v] = dist[u] + 1
                parent[v] = u

    if dist[n - 1] < 0:
        print("IMPOSSIBLE")
        return

    path = []
    cur = n - 1
    while cur != -1:
        path.append(cur + 1)
        cur = parent[cur]
    path.reverse()

    print(dist[n - 1])
    print(*path)


if __name__ == '__main__':
    main()