import sys
n,m=map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    ai = a[i]
    for j in range(m - 1, -1, -1):
        if ai == b[j]:
            dp[i][j] = 1 + dp[i+1][j + 1]
        else:
            dp[i][j] = dp[i][j + 1] if dp[i][j + 1] >= dp[i+1][j] else dp[i+1][j]

res = []
i = 0
j = 0
while i < n and j < m:
    if a[i] == b[j]:
        res.append(str(a[i]))
        i += 1
        j += 1
    elif dp[i][j + 1] >= dp[i + 1][j]:
        j += 1
    else:
        i += 1
print(dp[0][0])
print(*res)
