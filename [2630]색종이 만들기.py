def is_true(n, x, y):
    a = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if a != paper[i][j]:
                return False
    res[a] += 1
    return True


def cut(n, x, y):
    if is_true(n, x, y):
        return
    div = n // 2
    for i in range(2):
        for j in range(2):
            cut(div, x + i * div, y + j * div)


res = {0: 0, 1: 0}
n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

cut(n, 0, 0)

print(*res.values(), sep='\n')
