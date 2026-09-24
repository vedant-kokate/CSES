from collections import deque
def bfs(node):
    q = deque([(node, 0)])
    vis = {node: True}
    max_d = 0
    furthest = None
    while q:
        u, d = q.popleft()
        if d > max_d:
            max_d = d
            furthest = u
        for v in g.get(u, []):
            if v not in vis:
                vis[v] = True
                q.append((v, d + 1))

    return furthest, max_d
n = int(input())
g = {}
for _ in range(n-1):
    a, b = map(int, input().split())
    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []
    g[a].append(b)
    g[b].append(a)

end_node, _ = bfs(1)
# print(end_node, _)
_, diameter = bfs(end_node)
print(diameter)

