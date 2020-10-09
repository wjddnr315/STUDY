class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data


class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node, end="")
        if node.left is not None:
            self.preorderTraversal(node.left)
        if node.right is not None:
            self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if node.left is not None:
            self.inorderTraversal(node.left)
        print(node, end="")
        if node.right is not None:
            self.inorderTraversal(node.right)

    def postorderTraversal(self, node):
        if node.left is not None:
            self.postorderTraversal(node.left)
        if node.right is not None:
            self.postorderTraversal(node.right)
        print(node, end="")

    def makeroot(self, node, left_node, right_node):
        if self.root is None:
            self.root = node
        if left_node != ".":
            node.left = left_node
        if right_node != ".":
            node.right = right_node


tree = Tree()
nodes = dict()
for i in range(26):
    nodes[chr(65 + i)] = Node(chr(65 + i))
nodes["."] = None
for _ in range(int(input())):
    node, left_child, right_child = input().split()
    tree.makeroot(nodes[node], nodes[left_child], nodes[right_child])
tree.preorderTraversal(tree.root)
print()
tree.inorderTraversal(tree.root)
print()
tree.postorderTraversal(tree.root)
print()
