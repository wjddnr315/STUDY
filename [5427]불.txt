import sys
from collections import deque
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(x,y,fire):
    q=deque()
    q.append([x,y])
    vstd[x][y]=True
    f=deque(fire)
    for i,j in f:f_vstd[i][j]=True
    cnt=0
    while q:
        for _ in range(len(f)):
            a,b=f.popleft()
            for i in range(4):
                r=a+dx[i];c=b+dy[i]
                if 0<=r<h and 0<=c<w and building[r][c]!='#' and not f_vstd[r][c]:
                    building[r][c]='*'
                    f_vstd[r][c]=True;f.append([r,c])
        for _ in range(len(q)):
            a,b=q.popleft()
            if (a==h-1 or a==0 or b==w-1 or b==0) and building[a][b]!='#': return cnt+1
            for i in range(4):
                r=a+dx[i];c=b+dy[i]
                if 0<=r<h and 0<=c<w and building[r][c]=='.' and not vstd[r][c]: 
                    vstd[r][c]=True;q.append([r,c])
        cnt+=1
    return 'IMPOSSIBLE'
for _ in range((int(input()))):
    w,h=map(int,input().split())
    row=0
    col=0
    fire=[]
    building=list(list(input().rstrip()) for _ in range(h))
    vstd=[[False]*w for _ in range(h)]
    f_vstd=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if building[i][j]=='@':row=i;col=j
            if building[i][j]=='*':fire.append([i,j])
    print(bfs(row,col,fire))
    