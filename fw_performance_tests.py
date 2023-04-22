"""Performace tests for recursive and iterative Floyd Warshall functions"""
import sys
import timeit
import pandas as pd
from recursive_floyd_warshall import floyd_warshall_recursive
from iterative_floyd_warshall import floyd_warshall_iterative

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

def performance_test_recursive():
    """Performance test for recursive Floyd Warshall function"""
    start_time = timeit.default_timer()
    floyd_warshall_recursive(graph)
    return timeit.default_timer() - start_time

df_recursive_results = pd.DataFrame(columns=['Recursive Execution Time (s)'])

for i in range (1,1000):
    execution_time = performance_test_recursive()
    #add execution time to dataframe
    df_recursive_results.loc[i] = [execution_time]


#mean execution time for execution time recursive
mean_execution_time = df_recursive_results['Recursive Execution Time (s)'].mean()
print("Mean recursive function execution time: ", mean_execution_time, "(s)")

def performance_test_iterative():
    """Performance test for iterative Floyd Warshall function"""
    start_time = timeit.default_timer()
    floyd_warshall_iterative(graph)
    return timeit.default_timer() - start_time

df_iterative_results = pd.DataFrame(columns=['Iterative Execution Time (s)'])

for i in range (1,1000):
    execution_time = performance_test_iterative()
    #add execution time to dataframe
    df_iterative_results.loc[i] = [execution_time]

#mean execution time for execution time iterative
mean_execution_time = df_iterative_results['Iterative Execution Time (s)'].mean()
print("Mean iterative function execution time: ", mean_execution_time, "(s)")
