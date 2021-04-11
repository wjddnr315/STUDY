def f(n):
    if n <= 1:
        return 1
    return f(n-1) * n


res = str(f(int(input())))
print(len(res) - len(res.rstrip("0")))
