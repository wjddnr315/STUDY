from heapq import heappush, heappop
import sys
i = sys.stdin.readline
hq = []
for _ in range(int(i())):
    if (n := int(i())) > 0:
        heappush(hq, -n)
    else:
        try:
            print(-heappop(hq))
        except IndexError:
            print(0)
