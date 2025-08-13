class Node:
    def __init__(self, index):
        self.index = index
        self.left = None
        self.right = None

def build_tree(indexes):
    nodes = {}
    root = Node(1)
    nodes[1] = root
    for i, (left, right) in enumerate(indexes, 1):
        current = nodes[i]
        if left != -1:
            current.left = Node(left)
            nodes[left] = current.left
        if right != -1:
            current.right = Node(right)
            nodes[right] = current.right
    return root

def swap_nodes_at_depth(root, key):
    def swap(node, depth):
        if not node:
            return
        if depth % key == 0:
            node.left, node.right = node.right, node.left
        swap(node.left, depth + 1)
        swap(node.right, depth + 1)
    swap(root, 1)

def inorder_traversal(root):
    result = []
    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.index)
            traverse(node.right)
    traverse(root)
    return result

def swap_nodes(indexes, queries):
    root = build_tree(indexes)
    result = []
    for key in queries:
        swap_nodes_at_depth(root, key)
        result.append(inorder_traversal(root))
    return result