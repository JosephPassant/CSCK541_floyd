"""Unit tests for Floyd Warshall functions."""
# Requires the unittest and sys modules to be installed
import unittest
import sys

#import the function to be tested from the src folder
sys.path.append('../src/')
from recursive_floyd_warshall import floyd_warshall_recursive

# Define a constant to represent no path between two nodes
# equal to the maximum integer value of the system
NO_PATH = sys.maxsize

class TestFloyd(unittest.TestCase):
    """Test case for floyd function."""

    def test_case_1(self):
        """
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

    def test_case_2(self):
        """
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

    def test_case_3(self):
        """
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

    def test_case_4(self):
        """
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

    def test_case_5(self):
        '''
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
