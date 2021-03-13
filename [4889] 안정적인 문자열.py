loop = 1
while (string := input()):
    if '-' in string:
        break
    stack = []
    count = 0
    while True:
        prev = string[::]
        string = string.replace("{}", '')
        if prev == string:
            break
    for i in string:
        if stack:
            if i != '}':
                count += 1
            stack.pop()
        else:
            if i == '}':
                count += 1
            stack.append('{')
    print(f"{loop}. {count}")
    loop += 1
