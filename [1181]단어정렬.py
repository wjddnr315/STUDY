import sys
i = sys.stdin.readline
words = set([i() for _ in range(int(i()))])
print(''.join(sorted(words, key=lambda x: (len(x), x))))
