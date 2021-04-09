dxy = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def dfs(start):
    stack = [start]
    while stack:
        for _ in range(len(stack)):
            cx, cy = stack.pop()
            for dx, dy in dxy:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < h and 0 <= ny < w:
                    if not vstd[nx][ny] and board[nx][ny]:
                        vstd[nx][ny] = True
                        stack.append([nx, ny])


while True:
    w, h = map(int, input().split())
    island = 0
    if w == h == 0:
        break
    board = [list(map(int, input().split())) for _ in range(h)]
    vstd = [[False for _ in range(w)] for _ in range(h)]
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if not vstd[i][j] and c == 1:
                vstd[i][j] = True
                dfs([i, j])
                island += 1
    print(island)
