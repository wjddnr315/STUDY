MAX = 123456 * 2 + 1
numbers = [True] * MAX
numbers[0] = numbers[1] = False
for i in range(123457):
    if numbers[i]:
        for j in range(i*2, MAX, i):
            numbers[j] = False

while (n := int(input())):
    print(len([i for i in range(n+1, n * 2 + 1) if numbers[i]]))
