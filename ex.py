def build(board, blocks):
    time = 0
    for row in board:
        for i in row:
            if floor < i:
                time += (i - floor) * 2
                blocks += (i - floor)
    for row in board:
        for i in row:
            if floor > i:
                if blocks < floor - i:
                    return False, time
                time += (floor - i)
                blocks -= (floor - i)
    return True, time


n, m, b = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
floor = 0
results = []

while floor <= 256:
    res, time = build(board, b)
    if res:
        results.append([time, floor])
    floor += 1

results.sort(key=lambda x: (x[0], -x[1]))
print(*results[0], sep=' ')
