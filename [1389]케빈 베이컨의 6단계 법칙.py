from collections import deque
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.friends = list()

    def __repr__(self):
        return str(self.value + 1)


class Tree:
    def __init__(self):
        self.nodes = list()
        self.n = None
        self.m = None
        self.min_kevin_bacon = sys.maxsize
        self.res = None

    def make_tree(self):
        self.n, self.m = map(int, input().split())

        for i in range(self.n):
            self.nodes.append(Node(i))

        for i in range(self.m):
            a, b = map(int, input().split())
            a -= 1
            b -= 1
            self.nodes[a].friends.append(self.nodes[b])
            self.nodes[b].friends.append(self.nodes[a])

    def solution(self):
        for node in self.nodes:
            vstd = [False for _ in range(self.n)]
            q = deque([node])
            kevin_bacon = 0
            depth = 1
            while q:
                for _ in range(len(q)):
                    curr = q.popleft()
                    for f in curr.friends:
                        if not vstd[f.value]:
                            vstd[f.value] = True
                            kevin_bacon += depth
                            q.append(f)
                depth += 1
            if kevin_bacon < self.min_kevin_bacon:
                self.min_kevin_bacon = kevin_bacon
                self.res = node


tree = Tree()
tree.make_tree()
tree.solution()
print(tree.res)
