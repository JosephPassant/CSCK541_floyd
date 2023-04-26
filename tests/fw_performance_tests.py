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
df_recursive_results = pd.DataFrame(columns=['Recursive Execution Time (s)'])

#Run the performance test 1000 times and add execution time to dataframe
for i in range (1000):
    execution_time = performance_test(floyd_warshall_recursive)
    #Adds execution time to dataframe
    df_recursive_results.loc[i] = [execution_time]

#Calculates the Mean execution time for execution time recursive
mean_execution_time = df_recursive_results['Recursive Execution Time (s)'].mean()
print("Mean recursive function execution time: ", mean_execution_time, "(s)")


performance_test(floyd_warshall_iterative)
#Creates a dataframe to store execution times from iterative function
df_iterative_results = pd.DataFrame(columns=['Iterative Execution Time (s)'])

#Run the performance test 1000 times and add execution time to dataframe
for i in range (1000):
    execution_time = performance_test(floyd_warshall_iterative)
    #Add execution time to dataframe
    df_iterative_results.loc[i] = [execution_time]

#Calculates the mean execution time for execution time iterative
mean_execution_time = df_iterative_results['Iterative Execution Time (s)'].mean()
print("Mean iterative function execution time: ", mean_execution_time, "(s)")


def plot_execution_time (data_frame, title):
    """
    plots the distribution of execution times for a given function.
    DF is the dataframe containing the execution times
    function name is the name of the function i.e. recursive or iterative
    title is the title of the graph
    """
    fig, ax = plt.subplots()
    data_frame.plot.hist(bins=100, ax=ax)
    ax.set_title(title)
    ax.set_xlim(0, 6.01e-05)
    ax.set_xlabel('Execution Time (s)')
    ax.set_ylabel('Frequency')
    plt.show()

plot_execution_time(df_recursive_results, 'Recursive Execution Time Distribution')

plot_execution_time(df_iterative_results, 'Iterative Execution Time Distribution')


#Tests for normal distribution of recursive function execution times
recursive_shapiro_test = shapiro(df_recursive_results['Recursive Execution Time (s)'])
print("Shapiro Statistic for floyd_warshall_recursive_function", recursive_shapiro_test.statistic)
print("Shapiro P-Value for the floyd_warshall recursive function", recursive_shapiro_test.pvalue)

#Tests for normal distribution of iterative function execution times
iterative_shapiro_test = shapiro(df_iterative_results['Iterative Execution Time (s)'])
print("Shapiro Statistic for floyd_warshall_iterative_function", iterative_shapiro_test.statistic)
print("Shapiro P-Value for the floyd_warshall iterative function", iterative_shapiro_test.pvalue)

#If the data is normally distributed, perform a t-test
if recursive_shapiro_test.pvalue > 0.05 and iterative_shapiro_test.pvalue > 0.05:
    ttest, pval = ttest_ind(df_recursive_results['Recursive Execution Time (s)'],\
                            df_iterative_results['Iterative Execution Time (s)'])

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
