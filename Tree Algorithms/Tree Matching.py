import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

vis = [False] * (n + 1)
taken = [False] * (n + 1)
parent = [0] * (n + 1)
stack = [1]
vis[1] = True
order= []
ans = 0
while stack:
    u = stack.pop()
    order.append(u)
    for v in g.get(u, []):
        if not vis[v]:
            stack.append(v)
            vis[v] = True
            parent[v] = u
for u in reversed(order):
    p = parent[u]
    if p == 0:
        continue
    if not taken[u] and not taken[p]:
        taken[u] = True
        taken[p] = True
        ans += 1
print(ans)