res = 0
n = int(input())
m = int(input())
string = input()
p = 0
i = 1
while i < m - 1:
    if [string[i-1], string[i], string[i+1]] == ["I", "O", "I"]:
        p += 1
        i += 1
        if p == n:
            res += 1
            p -= 1
    else:
        p = 0
    i += 1

print(res)
