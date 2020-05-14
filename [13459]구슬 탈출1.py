d=[[0,1],[0,-1],[1,0],[-1,0]]
n,m=list(map(int,input().split()))
board=list(list(input()) for _ in range(n))
vstd=[[[[False] *m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def bfs():
    r_x,r_y,b_x,b_y=[0]*4
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                r_x=i;r_y=j
            if board[i][j]=='B':
                b_x=i;b_y=j
    vstd[r_x][r_y][b_x][b_y]=True
    q=[[r_x,r_y,b_x,b_y]]
    cnt=1
    while q:
        for _ in range(len(q)):
            rx,ry,bx,by=q.pop(0)
            rc,bc=[0]*2
            if cnt>10:
                return 0
            for dx,dy in d:
                tmp_rx,tmp_ry,rc=move(rx,ry,dx,dy)
                tmp_bx,tmp_by,bc=move(bx,by,dx,dy)
                if board[tmp_bx][tmp_by]!='O':
                    if board[tmp_rx][tmp_ry]=='O':
                        return cnt
                    if [tmp_bx,tmp_by]==[tmp_rx,tmp_ry]:
                            if rc>bc:
                                tmp_rx-=dx
                                tmp_ry-=dy
                            else:
                                tmp_bx-=dx
                                tmp_by-=dy
                    if not vstd[tmp_rx][tmp_ry][tmp_bx][tmp_by]:
                        vstd[tmp_rx][tmp_ry][tmp_bx][tmp_by] = True
                        q.append([tmp_rx,tmp_ry,tmp_bx,tmp_by])
        cnt+=1 
    return 0
def move(x,y,dx,dy):
    c=0
    while board[x+dx][y+dy]!='#' and board[x][y]!='O':
        x+=dx
        y+=dy
        c+=1
    return x,y,c

print(bfs())
