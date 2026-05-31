import sys
from collections import deque

n = int(sys.stdin.readline())
grid = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]

dq = deque([(0, 0)])
visited[0][0] = True

while dq:
    i, j = dq.popleft()
    for di, dj in moves:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
            visited[ni][nj] = True
            grid[ni][nj] = grid[i][j] + 1
            dq.append((ni, nj))

out = []
for row in grid:
    out.append(" ".join(map(str, row)))
sys.stdout.write("\n".join(out))