from recursive_floyd_warshall import floyd_warshall_recursive

import timeit

from fw_unit_tests import TestFloyd 

import sys
NO_PATH = sys.maxsize

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


def performance_test():
    floyd_warshall_recursive(graph)


execution_time = timeit.timeit(performance_test, number=1000)

print("Execution time: ", execution_time, "(s)")

