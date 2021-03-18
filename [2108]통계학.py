import sys
i = sys.stdin.readline
n = sorted([int(i()) for _ in range(int(i()))])
d = {}
for i in n:
    if i not in d:
        d[i] = 0
    d[i] += 1
print(*[round(sum(n)/len(n)), n[len(n)//2], sorted([i for i in d.keys()
                                                    if d[i] == max(d.values())])[:2][-1], n[-1]-n[0]], sep="\n")
