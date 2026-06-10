
import sys 
def get_ints(): return map(int, sys.stdin.readline().strip().split())
    
n = int(input())
a = list(get_ints())

last = {}
left = 0
ans = 0
for i, v in enumerate(a):
    if v in last and last[v] >= left:
        left = last[v] + 1
    last[v] = i
    ans += i - left + 1
print(ans)
         
    
    