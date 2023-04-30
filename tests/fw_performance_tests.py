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

#Creates a dataframe to store execution times for performance_test function
df_results = pd.DataFrame(columns=['floyd_warshall_recursive execution time (s)',\
                                    'floyd_warshall_iterative execution time (s)'])

def performance_test(function_name):
    """
    Undertakes a performance test for a given function using timeit and repeats this 200 times
    the execution times are added to the df_results dataframe
    The mean execution time for the function is printed to the terminal
    """
    for i in range (200): 
        start_time = timeit.default_timer()
        function_name(graph)
        execution_time = timeit.default_timer() - start_time
        df_results.loc[i, function_name.__name__ + ' execution time (s)'] = execution_time

    print("mean", function_name.__name__, "execution time: ", df_results[function_name.__name__ + \
                                                            ' execution time (s)'].mean(), "(s)")

#Runs the performance tests for both iterative and recursive functions
performance_test(floyd_warshall_recursive)
performance_test(floyd_warshall_iterative)

# Change all df_results values to numeric values to resolve error in ttest outcome if data\
# normally distributed
df_results = df_results.apply(pd.to_numeric)

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
    print("t-test statistic: ", ttest)

    if pval < 0.05:
        print("The difference in mean execution time of the recursive and iterative functions\
              is statistically significant")
    else:
        print("The difference in mean execution time of the recursive and iterative functions\
              is not statistically significant")

#If the data is not normally distributed, prints a message to the user
else:
    print("The data is not normally distributed so it is not appropriate to perform a t-test")

def plot_execution_time(col1, col2, title):
    """
    Plots the distribution of execution times for two columns on the same chart.
    df_results is the dataframe containing the execution times.
    col1 and col2 are the names of the columns to plot.
    title is the title of the graph.
    """
    fig, axis = plt.subplots()
    axis.hist(df_results[col1], bins=20, label=col1)
    axis.hist(df_results[col2], bins=20, label=col2)
    axis.set_title(title)
    axis.set_xlim(0, 0.00014)
    axis.set_ylim(0, 200)
    axis.set_xlabel('Execution Time (s)')
    axis.set_ylabel('Frequency')
    axis.legend()
    plt.show()

# Plots the distribution of execution times for both functions
# At end to enable compeltion of script without needing to close the graph
plot_execution_time('floyd_warshall_recursive execution time (s)',\
                    'floyd_warshall_iterative execution time (s)',\
                    'Recursive and Iterative Execution Time Distribution')
