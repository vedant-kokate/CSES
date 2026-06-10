import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
a = list(map(int, input().split()))


ans = [0] * (n + 1)

def dfs(u):
    for v in g.get(u, []):
        dfs(v)
        ans[u] += 1 + ans[v]

g = {}
for i in range(n-1):
    parent = a[i]
    child = i + 2
    if parent not in g:
        g[parent] = []
    g[parent].append(child)

dfs(1)
print(*ans[1:])