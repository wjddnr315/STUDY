import re
d = {"[": "]", "(": ")"}
while (n := input()) != ".":
    s = []
    for i in list(re.sub(r"[^\[\]\(\)]", "", n)):
        s.append(i)

        while len(s) > 1 and s[-2] in d and d[s[-2]] == s[-1]:
            s.pop()
            s.pop()
    print("no" if s else "yes")
