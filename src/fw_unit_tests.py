"""Unit tests for Floyd Warshall functions."""
# Requires the unittest and sys modules to be installed
import unittest
import sys

# Requires the following files to be in the same directory:
from recursive_floyd_warshall import floyd_warshall_recursive

# Define a constant to represent no path between two nodes
# equal to the maximum integer value of the system
NO_PATH = sys.maxsize

class TestFloyd(unittest.TestCase):
    """Test case for floyd function."""

    def test_floyd_warshall_recursive_1(self):
        """
        Test case 1.
        Defines a 4 x 4 matrix and calls floyd_warshall_recursive function
        passing the matrix as an argument.
        It then compares the output of the function with the known expected output.
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
        Test case 2.
        Defines a 3x3 matrix and calls floyd_warshall_recursive function
        passing the matrix as an argument.
        It then compares the output of the function with the known expected output.
        """
        graph = [[0, 5, NO_PATH],
                 [5, 0, 5],
                 [NO_PATH, 5, 0]]
        result = floyd_warshall_recursive(graph)
        expected_2 = [[0, 5, 10],
                 [5, 0, 5],
                 [10, 5, 0]]
        self.assertEqual(result, expected_2)

    def test_floyd_warshall_recursive_3(self):
        """
        Test case 3.
        Defines a 5 x 5 matrix and calls floyd_warshall_recursive function
        passing the matrix as an argument.
        It then compares the output of the function with the known expected output.
        """
        graph = [[0 , 3, 5, NO_PATH, NO_PATH],
                 [NO_PATH, 0, 3, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 3, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, 0, 4],
                 [6, NO_PATH, NO_PATH, 4, 0]]
        result = floyd_warshall_recursive(graph)
        expected = [[0, 3, 5, 8, 12],
                    [16, 0, 3, 6, 10],
                    [13, 16, 0, 3, 7],
                    [10, 13, 15, 0, 4],
                    [6, 9, 11, 4, 0]]
        self.assertEqual(result, expected)

    def test_floyd_warshall_recursive_4(self):
        """
        Test case 4.
        Defines a 10 x 10 matrix and calls floyd_warshall_recursive function
        passing the matrix as an argument.
        It then compares the output of the function with the known expected output.
        """
        graph = [[0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 3],
                 [NO_PATH, 0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, 0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, 3, 0, 3, NO_PATH, NO_PATH, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 3, NO_PATH, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 3, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 3, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0, 3],
                 [3, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, NO_PATH, 0]]
        result = floyd_warshall_recursive(graph)
        expected = [[0, 3, 6, 9, 12, 15, 18, 21, 24, 3],
                    [27, 0, 3, 6, 9, 12, 15, 18, 21, 24],
                    [24, 27, 0, 3, 6, 9, 12, 15, 18, 21],
                    [21, 24, 27, 0, 3, 6, 9, 12, 15, 18],
                    [18, 21, 24, 3, 0, 3, 6, 9, 12, 15],
                    [15, 18, 21, 24, 27, 0, 3, 6, 9, 12],
                    [12, 15, 18, 21, 24, 27, 0, 3, 6, 9],
                    [9, 12, 15, 18, 21, 24, 27, 0, 3, 6],
                    [6, 9, 12, 15, 18, 21, 24, 27, 0, 3],
                    [3, 6, 9, 12, 15, 18, 21, 24, 27, 0]]
        self.assertEqual(result, expected)

    def test_floyd_warshall_recursive_5(self):
        """
        Test case 5.
        Defines a 5 x 5 matrix and calls floyd_warshall_recursive function
        passing the matrix as an argument.
        It then compares the output of the function with the known expected output.
        """
        graph = [[0, 3, 3, 3, 3],
                 [NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
                 [3, NO_PATH, 0, NO_PATH, NO_PATH],
                 [NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH],
                 [3, NO_PATH, NO_PATH, NO_PATH, 0]]
        result = floyd_warshall_recursive(graph)
        expected = [[0, 3, 3, 3, 3],
                    [NO_PATH, 0, NO_PATH, NO_PATH, NO_PATH],
                    [3, 6, 0, 6, 6],
                    [NO_PATH, NO_PATH, NO_PATH, 0, NO_PATH],
                    [3, 6, 6, 6, 0]]
        self.assertEqual(result, expected)

    def test_floyd_warshall_recursive_6(self):
        '''
        Test case 6.
        Defines a 4 x 4 matrix and calls floyd_warshall_recursive function
        passing the matrix as an argument.
        It then compares the output of the function with the known expected output.
        '''
        graph = [[0, 3, NO_PATH, 6],
                 [NO_PATH, 0, 6, 7],
                 [7, 6, 0, NO_PATH],
                 [6, NO_PATH, 3, 0]]
        result = floyd_warshall_recursive(graph)
        expected = [[0, 3, 9, 6],
                    [13, 0, 6, 7],
                    [7, 6, 0, 13],
                    [6, 9, 3, 0]]
        self.assertEqual(result, expected)

if __name__=='__main__':
    unittest.main()

print("test")
