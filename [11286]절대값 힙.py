from heapq import heappush, heappop
import sys
i = sys.stdin.readline
hq = []
for _ in range(int(i())):
    if abs(n := int(i())) > 0:
        heappush(hq, (abs(n), n))
    else:
        try:
            print(heappop(hq)[1])
        except IndexError:
            print(0)
