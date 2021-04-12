def rotate(m):
    return [[m[j][i] for j in range(len(m))]
            for i in range(len(m[0])-1, -1, -1)]


def flip(m):
    return [r[::-1] for r in m]


def matching(i, j,  case):
    v = 0
    for x, y in case:
        try:
            v += board[x + i][y + j]
        except IndexError:
            return
    return v


tetrominos = [
    [[1, 1, 1, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[1, 1],
     [1, 1]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[1, 1, 1],
     [0, 1, 0]],
]
cases = []
for t in tetrominos:
    for i in range(2):
        for j in range(4):
            if t not in cases:
                cases.append(t)
            t = rotate(t)
        t = flip(t)

for r, case in enumerate(cases):
    l = []
    for i in range(len(case)):
        for j in range(len(case[0])):
            if case[i][j]:
                l.append([i, j])
    cases[r] = l

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        for case in cases:
            v = matching(i, j, case)
            if v:
                res = max(v, res)

print(res)
