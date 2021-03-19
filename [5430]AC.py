from collections import deque


def delete(flipped, deq):
    if flipped:
        deq.pop()
    else:
        deq.popleft()


def func(numbers, p):
    deq = deque()
    for i in numbers:
        deq.append(i)
    flipped = False
    for i in list(p):
        if i == "D":
            if deq:
                delete(flipped, deq)
            else:
                return "error"
        elif i == "R":
            flipped = not flipped
        elif i == "F":
            flipped = not flipped
            if deq:
                delete(flipped, deq)
            else:
                return "error"
    return str(list(deq)[::-1] if flipped else list(deq)).replace(" ", "")


for _ in range(int(input())):
    p = input().replace("RR", "").replace("RD", "F")
    n = int(input())
    numbers = list(map(int, input().strip("[]").split(","))) if n else input()
    if not n:
        numbers = []
    print(func(numbers, p))
