import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

col = [-1] * (n + 1)
queue = deque()
for start in range(1, n + 1):
    if col[start] != -1:
        continue
    col[start] = 0
    queue.append(start)
    while queue:
        node = queue.popleft()
        for neigh in graph[node]:
            if col[neigh] == -1:
                col[neigh] = 1 - col[node]
                queue.append(neigh)
            elif col[neigh] == col[node]:
                print("IMPOSSIBLE")
                sys.exit()

print(" ".join(str(col[i] + 1) for i in range(1, n + 1)))
