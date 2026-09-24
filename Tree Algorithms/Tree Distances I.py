from collections import deque
def bfs(node):
    distance = [0] * (n + 1)
    q = deque([(node, 0)])
    vis = {node: True}
    max_d = 0
    furthest = None
    while q:
        u, d = q.popleft()
        if distance[u] < d:
            distance[u] = d
        if d > max_d:
            max_d = d
            furthest = u
        for v in g.get(u, []):
            if v not in vis:
                vis[v] = True
                q.append((v, d + 1))

    return furthest, distance

n = int(input())
if n == 1:
    print(0)
    exit()
g = {}
for _ in range(n-1):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)

point_a, _ = bfs(1)
# print(end_node, _)
point_b, distance_a = bfs(point_a)
_, distance_b = bfs(point_b)

for i in range(1, n + 1):
    print(max(distance_a[i], distance_b[i]), end=' ')





