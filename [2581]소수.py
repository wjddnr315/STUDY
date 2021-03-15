numbers = [True for _ in range(10001)]
numbers[1] = False
for i in range(2, 5001):
    c = 2
    while i * c < 10001:
        numbers[i * c] = False
        c += 1
res = []
for i in range(int(input()), int(input())+1):
    if numbers[i]:
        res.append(i)
print(f"{sum(res)}\n{res[0]}") if res else print(-1)
