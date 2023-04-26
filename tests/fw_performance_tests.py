"""Performace tests for recursive and iterative Floyd Warshall functions"""

#requires the following modules to be installed:
import sys
import timeit
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
from scipy.stats import shapiro

#import the functions to be tested from the src folder
sys.path.append('../src/')
from recursive_floyd_warshall import floyd_warshall_recursive
from iterative_floyd_warshall import floyd_warshall_iterative

# Define a constant to represent no path between two nodes
# equal to the maximum integer value of the system
NO_PATH = sys.maxsize

# Add your own n x n graph to test performance of graphs with different characteristics
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

def performance_test(function_name):
    """
    Performance test for Floyd Warshall functions
    starts timer, calls function, stops timer and returns execution time
    """
    start_time = timeit.default_timer()
    function_name(graph)
    return timeit.default_timer() - start_time

#Creates a dataframe to store execution times from recursive function
df_results = pd.DataFrame(columns=['floyd_warshall_recursive execution time (s)',\
                                    'floyd_warshall_iterative execution time (s)'])

def run_performance_test(function_name):
    """
    Runs the performance test 1000 times and adds execution times to the df_results dataframe
    """
    for i in range (1000):
        execution_time = performance_test(function_name)
        #Adds execution time to dataframe
        df_results.loc[i, function_name.__name__ + ' execution time (s)'] = execution_time

#Runs the performance tests for both functions, calculates the mean execution times and prints them
run_performance_test(floyd_warshall_recursive)
run_performance_test(floyd_warshall_iterative)
mean_recursive_execution_time = df_results['floyd_warshall_recursive execution time (s)'].mean()
mean_iterative_execution_time = df_results['floyd_warshall_iterative execution time (s)'].mean()
print("Mean recursive function execution time: ", mean_recursive_execution_time, "(s)")
print("Mean iterative function execution time: ", mean_iterative_execution_time, "(s)")

def plot_execution_time(df_results, col1, col2, title):
    """
    Plots the distribution of execution times for two columns on the same chart.
    df_results is the dataframe containing the execution times.
    col1 and col2 are the names of the columns to plot.
    title is the title of the graph.
    """
    fig, ax = plt.subplots()
    ax.hist(df_results[col1], bins=75, alpha=0.5, label=col1)
    ax.hist(df_results[col2], bins=75, alpha=0.5, label=col2)
    ax.set_title(title)
    ax.set_xlim(0, 0.00014)
    ax.set_ylim(0, 1000)
    ax.set_xlabel('Execution Time (s)')
    ax.set_ylabel('Frequency')
    ax.legend()
    plt.show()

plot_execution_time(df_results, 'floyd_warshall_recursive execution time (s)',\
                    'floyd_warshall_iterative execution time (s)',\
                    'Recursive and Iterative Execution Time Distribution')


#Tests for normal distribution of recursive function execution times
recursive_shapiro_test = shapiro(df_results['floyd_warshall_recursive execution time (s)'])
print("Shapiro Statistic for floyd_warshall_recursive_function", recursive_shapiro_test.statistic)
print("Shapiro P-Value for the floyd_warshall recursive function", recursive_shapiro_test.pvalue)

#Tests for normal distribution of iterative function execution times
iterative_shapiro_test = shapiro(df_results['floyd_warshall_iterative execution time (s)'])
print("Shapiro Statistic for floyd_warshall_iterative_function", iterative_shapiro_test.statistic)
print("Shapiro P-Value for the floyd_warshall iterative function", iterative_shapiro_test.pvalue)

#If the data is normally distributed, performs a t-test
if recursive_shapiro_test.pvalue > 0.05 and iterative_shapiro_test.pvalue > 0.05:
    ttest, pval = ttest_ind(df_results['floyd_warshall_recursive execution time (s)'],\
                            df_results['floyd_warshall_iterative execution time (s)'])

    print("p-value: ", pval)
    print("t-test: ", ttest)

    if pval < 0.05:
        print("The difference in mean execution time of the recursive and iterative functions\
              is significantly significant")
    else:
        print("The difference in mean execution time of the recursive and iterative functions\
              is not significantly significant")

#If the data is not normally distributed, prints a message to the user
else:
    print("The data is not normally distributed so it is not appropriate to perform a t-test")
