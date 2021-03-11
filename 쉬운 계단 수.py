n = int(input())
dp = [1 for _ in range(10)]
dp[0] = 0
for _ in range(n - 1):
    nums = []
    for i in range(10):
        nums.append((dp[i - 1] if i - 1 >= 0 else 0) +
                    (dp[i + 1] if i + 1 < 10 else 0))
    dp = nums
print(sum(dp) % (10 ** 9))
