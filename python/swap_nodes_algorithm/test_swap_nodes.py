import unittest
from swap_nodes import Node, swap_nodes

class TestSwapNodes(unittest.TestCase):
    def test_case_1(self):
        indexes = [[2, 3], [-1, -1], [-1, -1]]
        queries = [1]
        expected = [[3, 1, 2]]
        self.assertEqual(swap_nodes(indexes, queries), expected)

    def test_case_2(self):
        indexes = [[2, 3], [4, 5], [6, -1], [-1, 7], [-1, -1], [-1, -1], [-1, -1]]
        queries = [2]
        expected = [[5, 2, 4, 7, 1, 3, 6]]
        self.assertEqual(swap_nodes(indexes, queries), expected)

if __name__ == '__main__':
    unittest.main()