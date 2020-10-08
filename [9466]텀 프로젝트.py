import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
cnt=0
def dfs(v):
    global cnt
    vstd[v]=True
    nxt=l[v]
    if vstd[nxt]:
        if not cycle[nxt]:
            tmp=nxt
            while tmp != v:
                tmp = l[tmp]
                cnt+=1
            cnt+=1
    else:
        dfs(nxt)
    cycle[v]=True
for _ in range(int(input())):
    n=int(input())
    n+=1
    cnt=0
    l=[0]
    l.extend(list(map(int,input().split())))
    vstd=[False]*n
    cycle=[False]*n
    for i in range(n):
        if not vstd[i]:dfs(i)
    print(n-cnt)
