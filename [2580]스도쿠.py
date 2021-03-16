import sys


def backtrack(idx):
    if len(zeros) == idx:
        for i in board:
            print(str(i).replace(",", "")[1:-1])
        sys.exit(0)
    i, j = zeros[idx]
    bin_nums = bin(box[(i // 3 * 3) + j // 3] | rows[i] | cols[j])
    bin_nums_str = bin_nums[2:][::-1]
    bin_num_list = list(bin_nums_str + "0" * (9-len(bin_nums_str)))
    nums = [idx + 1 for idx, v in enumerate(bin_num_list) if v == "0"]
    if not nums:
        return
    for num in nums:
        bitmask = 2 ** (num - 1)

        board[i][j] = num
        rows[i] += bitmask
        cols[j] += bitmask
        box[(i // 3 * 3) + j // 3] += bitmask

        backtrack(idx + 1)
        board[i][j] = 0
        rows[i] -= bitmask
        cols[j] -= bitmask
        box[(i // 3 * 3) + j // 3] -= bitmask


board = [list(map(int, input().split())) for _ in range(9)]

zeros = []
box = [0 for _ in range(9)]
rows = [0 for _ in range(9)]
cols = [0 for _ in range(9)]

for i, row in enumerate(board):
    for j, num in enumerate(row):
        if num:
            num -= 1
            box[(i // 3 * 3) + j // 3] |= 2**(num)
            rows[i] |= 2**(num)
            cols[j] |= 2**(num)
        else:
            zeros.append([i, j])
backtrack(0)
