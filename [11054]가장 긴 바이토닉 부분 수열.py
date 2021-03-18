n = int(input())
a = list(map(int, input().split()))
r_a = a[::-1]
x = [1 for _ in range(len(a))]
y = x[::]
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            x[i] = max(x[i], x[j] + 1)
        if r_a[i] > r_a[j]:
            y[i] = max(y[i], y[j] + 1)
        print(i, x)

y.reverse()
print(x)
print(max(list(x[i] + y[i] for i in range(n))) - 1)
