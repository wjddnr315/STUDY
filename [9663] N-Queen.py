n = int(input())
count = 0
queens = []


def dfs(queens, h, l, r):
    global count
    if h == n:
        count += 1
        return
    for i in range(n):
        if i in queens or i - h in l or i + h in r:
            continue
        l.append(i - h)
        r.append(i + h)
        queens.append(i)
        dfs(queens, h + 1, l, r)
        queens.pop()
        l.pop()
        r.pop()


dfs([], 0, [], [])
print(count)
