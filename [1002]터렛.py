def solution(p1, p2):
    if p1 == p2:
        return -1
    r_sub_r = (p1[-1]-p2[-1]) ** 2
    r_plus_r = (p1[-1]+p2[-1]) ** 2
    d_square = (p1[1]-p2[1]) ** 2 + (p1[0]-p2[0]) ** 2

    if r_sub_r < d_square < r_plus_r:
        return 2
    elif d_square == r_plus_r or d_square == r_sub_r:
        return 1
    elif r_plus_r < d_square or d_square < r_sub_r:
        return 0


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solution([x1, y1, r1], [x2, y2, r2]))
