import sys
n,m=map(int,input().split())
a = list(map(int,input().split()))
dp = [(n+1,0)]*(1<<n)
dp[0]=(1,0)
for i in range(1,1<<n):
    for j in range(n):
        if i&(1<<j):
            last_ride, last_weight = dp[i^(1<<j)]
            if last_weight+a[j]<=m:
                dp[i]=min(dp[i],(last_ride,last_weight+a[j]))
            else:
                dp[i]=min(dp[i],(last_ride+1,a[j]))
print(dp[-1][0])