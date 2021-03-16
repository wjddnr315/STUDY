def recur(s, i, op):
    if i == n:
        res.append(s)
        return
    plus, sub, mul, div = op
    num = numbers[i]
    if op[0]:
        recur(s + num, i + 1, [plus - 1, sub, mul, div])
    if op[1]:
        recur(s - num, i + 1, [plus, sub - 1, mul, div])
    if op[2]:
        recur(s * num, i + 1, [plus, sub, mul - 1, div])
    if op[3]:
        recur(s // num if s > 0 else - (-s // num),
              i + 1, [plus, sub, mul, div - 1])


res = []
n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
recur(numbers[0], 1, op)
print(max(res), min(res))
