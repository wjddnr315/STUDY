numbers = [True] * 1000001
numbers[0] = numbers[1] = False
for i in range(1000001):
    if numbers[i]:
        for j in range(i*2, 1000001, i):
            numbers[j] = False
s, e = map(int, input().split())

for i in range(s, e + 1):
    if numbers[i]:
        print(i)
