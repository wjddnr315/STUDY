for _ in range(int(input())):
    items = [input().split() for i in range(int(input()))]
    d = {k: 0 for _, k in items}
    res = 1
    for v, k in items:
        d[k] += 1
    for v in d.values():
        res *= (v + 1)
    print(res - 1)
