from copy import deepcopy

n = int(input())
res = 0


def pass_zero(board):
    global n

    i = 0
    while i < n:
        if 0 in board[i]:
            board[i].remove(0)
        else:
            i += 1

    for i in range(n):
        for _ in range(n - len(board[i])):
            board[i].append(0)
    return board


def squeeze(board):
    global n
    i = 0

    board = pass_zero(deepcopy(board))

    for i in range(n):
        for j in range(n - 1):
            if board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0

    board = pass_zero(deepcopy(board))

    return board


def rotate(cnt, board):
    global n
    for _ in range(cnt):
        new_board = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[i][j] = board[j][n - i - 1]
        board = new_board
    return board


def move(board, cnt, direction):
    global res
    global n
    if cnt == 5:
        res = max(res, max([max(i) for i in board]))
        return
    board = squeeze(rotate(direction, deepcopy(board)))

    for i in range(4):
        move(deepcopy(board), cnt + 1, i)


board = []

for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(4):
    move(deepcopy(board), 0, i)

print(res)
