from collections import deque
def bfs(l,r,c):
    q=deque()
    q.append([l,r,c])
    vstd=[[[False]*C for _ in range(R)] for _ in range(L)]
    vstd[l][r][c]=True
    cnt=0
    while q:
        for _ in range(len(q)):
            z,x,y=q.popleft()
            if building[z][x][y]=='E':
                return 'Escaped in {} minute(s).'.format(cnt)
            if z<L-1 and building[z+1][x][y]!='#' and not vstd[z+1][x][y]:
                vstd[z+1][x][y]=True
                q.append([z+1,x,y])
            if z>0 and building[z-1][x][y]!='#' and not vstd[z-1][x][y]:
                vstd[z-1][x][y]=True
                q.append([z-1,x,y])
            if x>0 and building[z][x-1][y]!='#' and not vstd[z][x-1][y]:
                vstd[z][x-1][y]=True
                q.append([z,x-1,y])
            if x <R-1 and building[z][x+1][y]!='#' and not vstd[z][x+1][y]:
                vstd[z][x+1][y]=True
                q.append([z,x+1,y])
            if y <C-1 and building[z][x][y+1]!='#' and not vstd[z][x][y+1]:
                vstd[z][x][y+1]=True
                q.append([z,x,y+1])
            if y >0 and building[z][x][y-1]!='#' and not vstd[z][x][y-1]:
                vstd[z][x][y-1]=True
                q.append([z,x,y-1])
        cnt+=1
    return 'Trapped!'
while True:
    a=0;b=0;c=0
    L,R,C=map(int,input().split())
    if [L,R,C]==[0,0,0]:break
    building=[[[] for _ in range(R)] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            building[i][j]=list(input().rstrip())
            if 'S' in building[i][j]:
                a,b,c=i,j,building[i][j].index('S')
        input()
    print(bfs(a,b,c))
