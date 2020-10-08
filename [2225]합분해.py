d = [[1]*200 for _ in range (200)]
for i in range(1,200):
    for j in range(200):
        d[i][j] = d[i-1][j] + d[i][j-1]
n,k = map(int,input().split())
print(d[k-1][n-1]%1000000000)