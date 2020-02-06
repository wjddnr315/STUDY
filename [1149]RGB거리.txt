N = int(input())
l = []
for _ in range(N):
    l.append(list(map(int,input().split(' '))))
dp = []
for _ in range(N):
    dp.append([0,0,0])
dp[0][0] = l[0][0]
dp[0][1] = l[0][1]
dp[0][2] = l[0][2]
for i in range(1,N):
    dp[i][0] = min(dp[i-1][1],dp[i-1][2])+l[i][0]
    dp[i][1] = min(dp[i-1][0],dp[i-1][2])+l[i][1]
    dp[i][2] = min(dp[i-1][1],dp[i-1][0])+l[i][2]
print(min(dp[N-1][0],dp[N-1][1],dp[N-1][2]))
