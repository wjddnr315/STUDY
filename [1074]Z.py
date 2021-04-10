def z(w, x, y, count):
    if w == 1:
        if r == x and c == y:
            print(count)
        return
    div = w // 2
    for i in range(2):
        for j in range(2):
            dx, dy = x + div * i, y + div * j
            if dx <= r <= dx + w and dy <= c <= dy + w:
                z(div, dx, dy, count + (i * 2 + j) * div ** 2)


n, r, c = map(int, input().split())
z(2 ** n, 0, 0, 0)
