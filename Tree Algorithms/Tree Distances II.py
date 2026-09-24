import sys
from collections import deque
# sys.setrecursionlimit(10**6)

# def dfs(cur, parent, depth):
#     global subtree_size, subree_dist
#     subree_dist[1] += depth
#     size = 1
#     for v in g[cur]:
#         if v != parent:
#             size += dfs(v, cur, depth + 1)
#     subtree_size[cur] = size
#     return size

# def dfs2(cur, parent):
#     global subree_dist
#     for v in g[cur]:
#         if v != parent:
#             subree_dist[v] = subree_dist[cur] + (n - 2 * subtree_size[v])
#             dfs2(v, cur)


n = int(sys.stdin.readline())
g = [[] for _ in range(n + 1)]

subtree_size = [1] * (n + 1)
subree_dist = [0] * (n + 1)
parent = [0] * (n + 1)
depths = [0] * (n + 1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

order = []
q = deque([1])
while q:
    u = q.popleft()
    order.append(u)
    for v in g[u]:
        if v != u and v != parent[u]:
            parent[v] = u
            depths[v] = depths[u] + 1
            q.append(v)

for u in reversed(order):
    parent_u = parent[u]
    subtree_size[parent_u] += subtree_size[u]
subree_dist[1] = sum(depths)
# print(order)
for u in order[1:]:
   p = parent[u]
   subree_dist[u] = subree_dist[p] + (n - 2 * subtree_size[u])
sys.stdout.write(" ".join(map(str, subree_dist[1:])))
# dfs(1, -1, 0)
# # subree_dist[1] = sum(subtree_size) - 1
# dfs2(1, -1)

# print(*subree_dist[1:])
