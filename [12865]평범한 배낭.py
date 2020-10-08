n,k = map(int,input().split())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
    
d = [[0]*(k+1) for _ in range(n)]
for i in range(n):
    for j in range(k+1):
        if l[i][0] > j:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(l[i][1]+d[i-1][j-l[i][0]],d[i-1][j])
print(d[-1][-1])
