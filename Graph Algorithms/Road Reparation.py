import sys

n,m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    edges.append((c, a - 1, b - 1))
edges.sort()

p = list(range(n))
r = [0] * n

def find(a):
    while p[a] != a:
        p[a] = p[p[a]]
        a = p[a]
    return a

ans = 0
cnt = 0
for c, a, b in edges:
    ra = find(a)
    rb = find(b)
    if ra != rb:
        if r[ra] < r[rb]:
            ra, rb = rb, ra
        p[rb] = ra
        if r[ra] == r[rb]:
            r[ra] += 1
        ans += c
        cnt += 1
        if cnt == n - 1:
            break

if cnt != n - 1:
    print("IMPOSSIBLE")
else:
    print(ans)
