import sys
from functools import lru_cache

data=sys.stdin.read().split()
if not data: sys.exit()
a,b=map(int,data)

def f(x):
    s=str(x)
    @lru_cache(None)
    def g(i,p,t):
        if i==len(s): return 1
        L=int(s[i]) if t else 9
        r=0
        for d in range(L+1):
            if d==p: continue
            r+=g(i+1,-1 if p<0 and d==0 else d,t and d==L)
        return r
    return g(0,-1,1)

print(f(b) if a==0 else f(b)-f(a-1))
