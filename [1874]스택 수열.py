import sys
i = sys.stdin.readline
c = 1
s = [0]
res = ""
for _ in range((int(i()))):
    n = int(i())
    while c <= n:
        res += "+"
        s.append(c)
        c += 1
    if s.pop() == n:
        res += "-"
    else:
        print("NO")
        sys.exit(0)
print(*res, sep='\n')
