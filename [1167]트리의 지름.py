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
        self.diameter = 0
        self.farthestNode = None

    def make_tree(self, node1, node2, distance):
        node1.childNode[node2] = distance

    def dfs(self, startNode):
        vstd = [False] * (n + 1)
        stack = [[startNode, 0]]
        diameter = 0
        while stack:
            for _ in range(len(stack)):
                currNode, distance = stack[-1]
                if vstd[currNode.data]:
                    stack.pop()
                    diameter -= distance
                    continue
                vstd[currNode.data] = True
                diameter += distance
                if self.diameter < diameter:
                    self.diameter = diameter
                    self.farthestNode = currNode
                for childNode in currNode.childNode:
                    if not vstd[childNode.data]:
                        stack.append([childNode, currNode.childNode[childNode]])


tree = Tree()
n = int(input())
nodes = [Node(i) for i in range(n + 1)]
for _ in range(n):
    inputs = list(map(int, input().split()))
    inputs.pop()
    node = inputs.pop(0)
    for i in range(0, len(inputs), 2):
        tree.make_tree(nodes[node], nodes[inputs[i]], inputs[i + 1])
tree.dfs(nodes[1])
tree.dfs(tree.farthestNode)
print(tree.diameter)
