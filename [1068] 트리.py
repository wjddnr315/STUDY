class Node:
    def __init__(self, data):
        self.data = data
        self.childs = list()


class Tree:
    def __init__(self, n):
        self.root = None
        self.nodes = list(Node(i) for i in range(n))

    def make_tree(self, parent, child):
        parent.childs.append(child)

    def cut(self, cut_node):
        stack = [tree.root]
        if tree.root == cut_node:
            tree.root = None
            return
        while stack:
            for _ in range(len(stack)):
                node = stack.pop()
                for child in node.childs:
                    if child == cut_node:
                        node.childs.remove(cut_node)
                        return
                    stack.append(child)

    def find_leaves(self):
        leaves = 0
        stack = [tree.root]
        while stack:
            for _ in range(len(stack)):
                node = stack.pop()
                if node.childs == []:
                    leaves += 1
                    continue
                for child in node.childs:
                    stack.append(child)
        return leaves


n = int(input())
tree = Tree(n)
for child, parent in enumerate(list(map(int, input().split()))):
    if parent == -1:
        tree.root = tree.nodes[child]
    else:
        tree.make_tree(tree.nodes[parent], tree.nodes[child])
cut_node = tree.nodes[int(input())]
tree.cut(cut_node)
if tree.root is None:
    print(0)
else:
    print(tree.find_leaves())
