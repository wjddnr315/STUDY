import sys
i = sys.stdin.readline
s = []
for _ in range(int(i())):
    if (n := int(i())):
        s.append(n)
    else:
        s.pop()
print(sum(s))
