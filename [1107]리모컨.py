def can(n, r):
    for i in list(str(n)):
        if i in r:
            return False
    return True


n = int(input())
r = input().split() if int(input()) else []
c = 0
res = abs(100 - n)
while c <= 500000:
    if can(n - c, r):
        res = min(res, c + len(str(n - c)))
    if can(n + c, r):
        res = min(res, c + len(str(n + c)))
    c += 1
print(res)
