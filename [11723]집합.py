import sys


i = sys.stdin.readline
s = set()
for _ in range(int(i())):
    payload = i()
    try:
        op, num_str = payload.split()
        num = int(num_str)
    except ValueError:
        op = payload.rstrip()
    if op == "add":
        s.add(num)
    elif op == "remove":
        try:
            s.remove(num)
        except KeyError:
            pass
    elif op == "check":
        print(1 if num in s else 0)
    elif op == "toggle":
        try:
            s.remove(num)
        except KeyError:
            s.add(num)
    elif op == "all":
        s = set(range(1, 21))
    elif op == "empty":
        s.clear()
