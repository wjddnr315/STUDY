from copy import deepcopy


def paint(coor, bd, table):
    cx, cy = coor
    l, t, r, b = table

    if l:
        for j in range(cy - 1, -1, -1):
            if bd[cx][j] == 6:
                break
            if bd[cx][j] == 0:
                bd[cx][j] = '#'
    if r:
        for j in range(cy + 1, len(bd[0])):
            if bd[cx][j] == 6:
                break
            if bd[cx][j] == 0:
                bd[cx][j] = '#'
    if b:
        for i in range(cx + 1, len(bd)):
            if bd[i][cy] == 6:
                break
            if bd[i][cy] == 0:
                bd[i][cy] = '#'
    if t:
        for i in range(cx - 1, -1, -1):
            if bd[i][cy] == 6:
                break
            if bd[i][cy] == 0:
                bd[i][cy] = '#'
    return bd


def watch(idx, bd):
    if idx == len(cctvs):
        count = 0
        for row in bd:
            for val in row:
                if val == 0:
                    count += 1
        res.append(count)
        return
    coor, cctv_kind = cctvs[idx]
    for table in CCTV_TABLE[cctv_kind]:
        watch(idx + 1, deepcopy(paint(coor, deepcopy(bd), table)))


CCTV_TABLE = [[],
              [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
              [[1, 0, 1, 0], [0, 1, 0, 1]],
              [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 1]],
              [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]],
              [[1, 1, 1, 1]]]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctvs = []
res = []
for i, row in enumerate(board):
    for j, val in enumerate(row):
        if 0 < val < 6:
            cctvs.append(([i, j], val))

watch(0, board)
print(min(res))
