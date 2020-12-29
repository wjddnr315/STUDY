from copy import deepcopy
from collections import deque
from itertools import combinations

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(board, viruses):
    global n, m

    vstd = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    q = deque(viruses)

    while q:
        for _ in range(len(q)):
            virus = q.popleft()
            vstd[virus[0]][virus[1]] = True
            for i in dxy:
                new_virus = [sum(j) for j in zip(virus, i)]
                if (
                    0 <= new_virus[0] < n
                    and 0 <= new_virus[1] < m
                    and board[new_virus[0]][new_virus[1]] == 0
                    and not vstd[new_virus[0]][new_virus[1]]
                ):
                    q.append(new_virus)
                    board[new_virus[0]][new_virus[1]] = 2
    return sum(list(i.count(0) for i in board))


ret = 0
n, m = map(int, input().split())
board = []
empty = []
viruses = []

for _ in range(n):
    board.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))
        if board[i][j] == 2:
            viruses.append((i, j))

case_wall = list(combinations(empty, 3))

for walls in case_wall:
    new_board = deepcopy(board)
    for wall_x, wall_y in walls:
        new_board[wall_x][wall_y] = 1
    ret = max(ret, bfs(new_board, viruses))

print(ret)
