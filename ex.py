p = [list(map(int, input().split())) for _ in range(int(input()))]
for i in p:
    c = 1
    for j in p:
        if i[0] < j[0] and i[1] < j[1]:
            c += 1
    print(c)
