"""Unit tests for floyd warshall functions"""

from iterative_floyd_warshall import floyd

import unittest
import sys
NO_PATH = sys.maxsize

class TestFloyd(unittest.TestCase):

    def test_floyd(self):
        graph = [[0, 7, NO_PATH, 8],
                [NO_PATH, 0, 5, NO_PATH],
                [NO_PATH, NO_PATH, 0, 2],
                [NO_PATH, NO_PATH, NO_PATH, 0]]
        result = floyd(graph)
        expected = [[0, 7, 12, 8],
                    [NO_PATH, 0, 5, 7],
                    [sys.maxsize, sys.maxsize, 0, 2],
                    [sys.maxsize, sys.maxsize, sys.maxsize, 0]]
        self.assertEqual(result, expected)

if __name__=='__main__':
    unittest.main()
