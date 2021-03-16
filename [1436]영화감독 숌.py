n = int(input())
c = 0
res = 0
while res != n:
    c += 1
    if str(c).count("666"):
        res += 1
print(c)
