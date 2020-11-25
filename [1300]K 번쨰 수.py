n, k = map(int, input().split())
start = 1
end = k
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(mid // i, n)
    if cnt < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1
print(ans)