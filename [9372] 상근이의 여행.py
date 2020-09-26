from collections import deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    nodes=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(int,input().split())
        nodes[a-1].append(b-1)
        nodes[b-1].append(a-1)
    q = deque([0])
    vstd=[False for _ in range(n)]
    c=0
    vstd[0]=True
    while q:
        for _ in range(len(q)):
            curr = q.pop()
            for i in nodes[curr]:
                if not vstd[i]:
                    vstd[i]=True
                    q.append(i)
                    c+=1
    print(c)
