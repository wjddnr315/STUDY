from collections import deque
import sys
input=sys.stdin.readline
def dfs(s):
    vstd2[s]=True
    print(s,end=' ')
    for i in l[s]:
        if not vstd2[i]:dfs(i)
def bfs(s):
    q=deque()
    vstd=[False]*n
    vstd[s]=True
    print(s,end=' ')
    q.append(s)
    while q:  
        c=q.popleft()
        for i in l[c]:
            if not vstd[i]:
                print(i,end=' ')
                vstd[i]=True
                q.append(i)
n,m,v=map(int,input().split())
n+=1
l=[[] for _ in range(n)]
vstd2=[False]*n  
for _ in range(m):
    a,b=map(int,input().split())
    l[a].append(b)
    l[b].append(a)
for i in range(n):
    l[i].sort()
dfs(v)
print()
bfs(v)