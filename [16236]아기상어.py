from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(shark):
    q = deque([shark])
    res = time = 0
    vstd = [[False for _ in range(n)] for _ in range(n)]
    fishes = []
    eat_count = size = 2
    while q:
        for _ in range(len(q)):
            cx, cy = q.popleft()
            for dx, dy in dxy:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < n:
                    if not vstd[nx][ny]:
                        if board[nx][ny] <= size:
                            q.append([nx, ny])
                            vstd[nx][ny] = True
                            if 1 <= board[nx][ny] < size:
                                fishes.append([nx, ny])
        time += 1
        if fishes:
            x, y = sorted(fishes)[0]
            eat_count -= 1
            if not eat_count:
                size += 1
                eat_count = size
            res += time
            time = board[x][y] = 0

            vstd = [[False for _ in range(n)] for _ in range(n)]
            vstd[x][y] = True
            q = deque([[x, y]])
            fishes = []
    return res


for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            print(bfs([i, j]))
