from collections import deque
dx=[1,-1,0,0];dy=[0,0,1,-1]
def bfs(loc,w):
    q=deque(loc)
    w=deque(w)
    for [i,j] in w: vstd[i][j]=True
    cnt=0
    while q:
        for _ in range(len(w)):
            x,y=w.popleft()
            for i in range(4):
                a=x+dx[i];b=y+dy[i]
                if 0<=a<R and 0<=b<C and not vstd[a][b] and (maap[a][b]=='.' or maap[a][b]=='S'):
                    vstd[a][b]=True
                    maap[a][b]='*'
                    w.append([a,b])
        for _ in range(len(q)):
            x,y=q.popleft()
            if [x,y]==[shelter[0],shelter[1]]: return cnt
            for i in range(4):
                a=x+dx[i];b=y+dy[i]
                if 0<=a<R and 0<=b<C and not vstd[a][b] and (maap[a][b]=='.' or maap[a][b]=='D'):
                    vstd[a][b]=True
                    q.append([a,b])
        cnt+=1
    return 'KAKTUS'
R,C= map(int,input().split())
maap=list(list(input().rstrip()) for _ in range(R))
water=[]
hedgehog=[]
shelter=[]
vstd=[[False]*C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if maap[i][j]=='*':water.append([i,j])
        if maap[i][j]=='S':hedgehog.extend([i,j])
        if maap[i][j]=='D':shelter.extend([i,j])
print(bfs([[hedgehog[0],hedgehog[1]]],water))