n = int(input())
res = 0


def squeeze(board):
    _len = len(board)
    i = j = 0
    while True:
        if board[i][j] == 0:
            del board[i][j]
            _len -= 1
        else:
            j += 1
            if j == _len:
                j = 0
                i += 1
        if i == j == n:
            break
    print(board)


def rotate(cnt, board):
    _len = len(board)
    for _ in range(cnt):
        new_board = [[0 for _ in range(_len)] for _ in range(_len)]
        for i in range(_len):
            for j in range(_len):
                new_board[i][j] = board[j][n - i - 1]
        board = new_board
        for i in board:
            print(i)
        print()
    return board


def move(board, cnt, direction):
    global res
    global n
    if cnt == 5:
        res = max(res, max([max(i) for i in board]))
    board = rotate(direction)
    board = squeeze(board)

    for i in range(4):
        move(board, cnt + 1, i)


board = []

for i in range(n):
    board.append(list(map(int, input().split())))

squeeze(board)