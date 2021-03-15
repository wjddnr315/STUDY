n = int(input())
loads = list(map(int, input().split()))
costs = list(map(int, input().split()))

curr = costs[0]
res = 0
for i in range(len(costs)-1):
    if curr > costs[i]:
        curr = costs[i]
    res += curr * loads[i]
print(res)
