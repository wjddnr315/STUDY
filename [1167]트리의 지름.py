import sys

input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.childNode = dict()

    def __str__(self):
        return self.data


class Tree:
    def __init__(self):
        self.root = None


tree = Tree()

for _ in range(int(input())):
    inputs = list(map(int, input().split()))
    print(inputs)
