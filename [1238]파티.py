import sys
import heapq

i = sys.stdin.readline

n, m, x = map(int, i().split())
board = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, v = map(int, i().split())
    board[a][b] = v
