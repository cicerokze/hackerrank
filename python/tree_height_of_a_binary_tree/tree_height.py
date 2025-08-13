class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return -1
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return 1 + max(left_height, right_height)