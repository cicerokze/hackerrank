from collections import deque

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.info)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result