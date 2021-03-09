def backtrack(res):
    if len(res) == m:
        print(str(res)[1:-1].replace(",", ""))
        return
    for num in numbers:
        if num not in res:
            res.append(num)
            backtrack(res)
            res.pop()


n, m = map(int, input().split())
numbers = [i + 1 for i in range(n)]
backtrack([])
