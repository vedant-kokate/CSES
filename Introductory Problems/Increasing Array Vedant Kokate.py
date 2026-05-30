import sys
from sys import stdin
def get_ints(): return map(int, sys.stdin.readline().strip().split())
n=int(input())
#s=stdin.readline()
a=list(get_ints())
ans=0
for i in range(1,n):
    f,s = a[i-1],a[i]
    if s<f:
        ans+=f-s
        a[i]=f
print(ans)
        
