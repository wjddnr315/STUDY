x, c, s = int(input()), 1, 1
while x > s:
    c += 1
    s += c
d = x - (s - c)
print(f"{c - d + 1 if c % 2 else d}/{d if c % 2 else c - d + 1}")
