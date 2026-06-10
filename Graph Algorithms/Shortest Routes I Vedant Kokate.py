import sys
import heapq

data = sys.stdin.buffer.read().split()
it = iter(data)
n = int(next(it))
m = int(next(it))

graph = [[] for _ in range(n)]
for _ in range(m):
    a = int(next(it)) - 1
    b = int(next(it)) - 1
    c = int(next(it))
    graph[a].append((b, c))

INF = 10**15
dist = [INF] * n
dist[0] = 0
pq = [(0, 0)]

while pq:
    d, node = heapq.heappop(pq)
    if d > dist[node]:
        continue
    for neigh, w in graph[node]:
        nd = d + w
        if nd < dist[neigh]:
            dist[neigh] = nd
            heapq.heappush(pq, (nd, neigh))

print(*dist)

