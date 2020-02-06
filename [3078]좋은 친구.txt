from collections import deque
import sys
input=sys.stdin.readline
l=[0]*25;c=0;d=deque()
n,k=map(int,input().split())
for _ in range(n):
    a=input()
    if len(d)+1>k+1: l[len(d.popleft())]-=1 
    if l[len(a)]>0: c+=l[len(a)]
    l[len(a)]+=1
    d.append(a)
print(c)