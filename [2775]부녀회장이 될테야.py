dp = [[0 for _ in range(14)] for _ in range(15)]
dp[0] = [i + 1 for i in range(14)]
for i in range(1, 15):
    for j in range(14):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]
for _ in range(int(input())):
    k, n = int(input()), int(input())
    print(dp[k][n-1])
