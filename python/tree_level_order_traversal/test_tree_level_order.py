import unittest
from tree_level_order import Node, level_order

class TestLevelOrder(unittest.TestCase):
    def test_single_node(self):
        root = Node(1)
        self.assertEqual(level_order(root), [1])

    def test_complete_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(level_order(root), [1, 2, 3, 4, 5])

    def test_left_skewed(self):
        root = Node(1)
        root.left = Node(2)
        root.left.left = Node(3)
        self.assertEqual(level_order(root), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()    
