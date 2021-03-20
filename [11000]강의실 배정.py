import sys
from heapq import heappush, heappushpop
input = sys.stdin.readline
classes = [list(map(int, input().split())) for _ in range(int(input()))]
classes.sort()
hq = []
res = 0
for s, e in classes:
    if hq:
        if hq[0] > s:
            heappush(hq, e)
        else:
            heappushpop(hq, e)
    else:
        heappush(hq, e)
    res = max(len(hq), res)
print(res)
