import sys
def get_ints(): return map(int, sys.stdin.readline().strip().split())

q = int(input())
for _ in range(q):
    n,a,b = get_ints()
    if a + b > n or (a == 0 and b != 0) or (b == 0 and a != 0):
        print("NO")
        continue    
    print("YES")
    print(*range(1,n+1))
    tie = n-(a+b)
    # print("tie",tie)
    for i in range(1,tie+1):
        print(i,end=" ")
    for i in range(n-b + 1, n+1):
        print(i,end=" ")
    for i in range(tie+1, n-b + 1):
        print(i,end=" ")
    print()
