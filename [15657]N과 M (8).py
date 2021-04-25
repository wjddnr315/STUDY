def backtrack(idx, seq):
    if len(seq) == m:
        res.append(seq)
        return
    for i in range(idx, len(nums)):
        if nums[i] >= seq[-1]:
            seq.append(nums[i])
            backtrack(i, seq[:])
            seq.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
res = []
for i, num in enumerate(nums):
    backtrack(i, [num])
res.sort()
for i in res:
    print(*i, sep=' ')
