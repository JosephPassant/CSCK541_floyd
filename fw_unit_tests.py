"""Unit tests for Floyd Warshall functions"""

import unittest
import sys

from recursive_floyd_warshall import floyd_warshall_recursive

NO_PATH = sys.maxsize

class TestFloyd(unittest.TestCase):
    """Test case for floyd function"""

    def test_floyd_warshall_recursive_1(self):
        """
        Test case 1
        4 x 4 matrix defined in given pdf and known output
        """
        graph = [[0, 7, NO_PATH, 8],
                [NO_PATH, 0, 5, NO_PATH],
                [NO_PATH, NO_PATH, 0, 2],
                [NO_PATH, NO_PATH, NO_PATH, 0]]
        result = floyd_warshall_recursive(graph)
        expected = [[0, 7, 12, 8],
                    [NO_PATH, 0, 5, 7],
                    [sys.maxsize, sys.maxsize, 0, 2],
                    [sys.maxsize, sys.maxsize, sys.maxsize, 0]]
        self.assertEqual(result, expected)

    def test_floyd_warshall_recursive_2(self):
        """
        Test case 2
        3x3 matrix
        """
        graph = [[0, 5, NO_PATH],
                 [5, 0, 5],
                 [NO_PATH, 5, 0]]
        result = floyd_warshall_recursive(graph)
        expected_2 = [[0, 5, 10],
                 [5, 0, 5],
                 [10, 5, 0]]
        self.assertEqual(result, expected_2)

if __name__=='__main__':
    unittest.main()
