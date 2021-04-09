class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def __repr__(self):
        return f"{self.value}


class Tree:
    def __init__(self):
        self.root = None
        self.count = 0
        self.nodes = []

    def make_tree(self):
        self.root = Node()
        self.nodes.append([self.root])
        for i in range(k - 1):
            self.nodes.append([])
            for parent in self.nodes[i]:
                left, right = Node(), Node()
                parent.left = left
                parent.right = right
                self.nodes[i + 1].extend([left, right])

    def dfs(self, node):
        if node.left:
            self.dfs(node.left)
        node.value = nums[self.count]
        self.count += 1
        if node.right:
            self.dfs(node.right)


k = int(input())
nums = list(map(int, input().split()))
tree = Tree()
tree.make_tree()
tree.dfs(tree.root)
for nodes in tree.nodes:
    print(*nodes)
