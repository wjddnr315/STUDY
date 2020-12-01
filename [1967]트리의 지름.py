class Node:
    def __init__(self, data):
        self.data = data
        self.child = dict()


class Tree:
    def __init__(self):
        self.diaNode = None
        self.diameter = 0

    def make_tree(self, node1, node2, dist):
        node1.child[node2] = dist
        node2.child[node1] = dist

    def dfs(self, start):
        vstd = [False] * (n + 1)
        stack = []
        stack.append([start, 0])
        dm = 0
        while stack:
            for _ in range(len(stack)):
                node, dist = stack[-1]
                if vstd[node.data]:
                    stack.pop()
                    dm -= dist
                    continue
                vstd[node.data] = True
                dm += dist
                c = 0
                for childNode in node.child:
                    if not vstd[childNode.data]:
                        c += 1
                        stack.append([childNode, node.child[childNode]])
                if not c:
                    if self.diameter < dm:
                        self.diameter = dm
                        self.diaNode = node


n = int(input())
if n != 1:
    nodes = [Node(i) for i in range(1, n + 1)]

    tree = Tree()
    for _ in range(n - 1):
        node1, node2, dist = map(int, input().split())
        tree.make_tree(nodes[node1 - 1], nodes[node2 - 1], dist)
    tree.dfs(nodes[0])
    tree.dfs(tree.diaNode)
    print(tree.diameter)
else:
    print(0)