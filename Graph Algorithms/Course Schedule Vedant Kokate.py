import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
g=[[]for i in range(n)]

for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

def dfs(v):
    global isCycle
    visited[v] = 1
    for u in g[v]:
        if visited[u] == 0:
            dfs(u)
            if isCycle:
                return
        elif visited[u] == 1:
            isCycle = True
            return
    visited[v] = 2
    ans.append(v + 1)

visited = [0] * n
isCycle = False
ans = []
for i in range(n):
    if visited[i] == 0:
        dfs(i)
        if isCycle:
            break
if isCycle:
    print("IMPOSSIBLE")
    sys.exit()
print(*reversed(ans))