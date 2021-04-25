from itertools import combinations


def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


n, m = map(int, input().split())
bbq, houses = [], []
city = [list(map(int, input().split())) for _ in range(n)]

for i, r in enumerate(city):
    for j, c in enumerate(r):
        if c == 1:
            houses.append([i, j])
        elif c == 2:
            bbq.append([i, j])
res = 10**10
for case in combinations(bbq, m):
    sum_dist = 0
    for house in houses:
        dist = 101
        for c in case:
            dist = min(get_dist(c, house), dist)
        sum_dist += dist
    res = min(sum_dist, res)
print(res)
