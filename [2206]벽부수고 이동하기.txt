from collections import deque
dx=[1,-1,0,0];dy=[0,0,1,-1]
def bfs():
    q=deque([[0,0,False]])
    cnt=0
    vstd[0][0][0]=True
    while q:
        for _ in range(len(q)):
            r,c,b=q.popleft()
            if [r,c]==[n-1,m-1]:return cnt+1
            for i in range(4):
                x=r+dx[i];y=c+dy[i]
                if 0<=x<n and 0<=y<m:
                    if not b and not vstd[0][x][y]:
                        if matrix[x][y]=='1':
                            q.append([x,y,True])
                            vstd[1][x][y]=True
                        else:
                            q.append([x,y,False])
                            vstd[0][x][y]=True
                    else:
                        if matrix[x][y]=='0' and not vstd[1][x][y]:
                            q.append([x,y,True])
                            vstd[1][x][y]=True
        cnt+=1
    return -1
n,m=map(int,input().split())
matrix=list(list(input().rstrip()) for _ in range(n))
vstd=[[[False]*m for _ in range(n)] for _ in range(2)]
print(bfs())