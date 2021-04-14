import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
stack=[]
ans=[]
for i in range(n):
    #print(stack,"befre poping")
    while len(stack)>0 and a[stack[-1]-1]>=a[i]:
        stack.pop()
   # print(stack,"after poping")
    if len(stack)==0:
        ans.append(0)
    else:
        ans.append(stack[-1])
    stack.append(i+1)
print(*ans)
        
        
    



