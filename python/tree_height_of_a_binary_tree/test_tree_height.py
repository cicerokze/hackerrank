import unittest
from tree_height import Node, height

class TestTreeHeight(unittest.TestCase):
    def test_single_node(self):
        root = Node(1)
        self.assertEqual(height(root), 0)

    def test_balanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(height(root), 2)

    def test_unbalanced_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        root.left.left.left = Node(4)
        self.assertEqual(height(root), 3)

if __name__ == '__main__':
    unittest.main()
    
