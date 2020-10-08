import sys
input = sys.stdin.readline
def dfs(r,c):
    stack=[[r,c]]
    while stack:
        row,col=stack.pop()
        if node[row][col]:
            node[row][col]=False
            if row < n-1 and node[row+1][col]: stack.append([row+1,col])
            if row > 0 and node[row-1][col] : stack.append([row-1,col])
            if col < m-1 and node[row][col+1]: stack.append([row,col+1])
            if col > 0 and node[row][col-1]: stack.append([row,col-1])   
for _ in range(int(input())):
    n,m,k=map(int,input().split())
    c=0
    node=[[False]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        node[x][y]=True
    for i in range(n):
        for j in range(m):
            if node[i][j]:
                dfs(i,j)
                c+=1
    print(c)
