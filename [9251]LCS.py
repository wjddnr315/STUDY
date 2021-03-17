a = input()
b = input()
dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
for i, iv in enumerate(a):
    for j, jv in enumerate(b):
        if iv == jv:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

print(dp[-1][-1])
