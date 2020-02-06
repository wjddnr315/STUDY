import sys
sys.setrecursionlimit(10**9)
dx=[1,-1,0,0];dy=[0,0,1,-1]
mx=1
def dfs(vstd,r,c,t):
    global mx   
    for i in range(4):
        x=dx[i]+r;y=dy[i]+c
        if 0<=x<R and 0<=y<C and not vstd[ord(alpha[x][y])-ord('A')]:
            vstd[ord(alpha[x][y])-ord('A')]=True
            dfs(vstd,x,y,t+1)
            vstd[ord(alpha[x][y])-ord('A')]=False  
    mx=max(t,mx)
R,C=map(int,input().split())
alpha=list(list(input().rstrip()) for _ in range(R)) 
vs=[False]*26
vs[ord(alpha[0][0])-ord('A')]=True
dfs(vs,0,0,1)
print(mx)
