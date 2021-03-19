def build(board, b):
    time = 0
    for row in board:
        for i in row:
            if f < i:
                time += (i - f) * 2
                b += (i - f)
            elif f > i:
                time += (f - i)
                b -= (f - i)
                if b < 0:
                    return False, time
    return True, time


n, m, blocks = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
f = 0
ans = []

while f <= 256:
    builded, t = build(board, blocks)
    if builded:
        ans.append([t, f])
    f += 1

ans.sort(key=lambda x: (x[0], -x[0]))
print(*ans[0], sep=' ')
