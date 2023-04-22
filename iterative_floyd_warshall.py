"""Floyd Warshall Algorithm"""

import sys
import itertools

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0, 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(graph[0])


def floyd(distance):

    """
    A simple implementation of Floyd's algorithm

    floyd is a function that takes a matrix as an input and returns an updated
    matrix displaying the shortest path between nodes of the input graph
    """

# iterates over all possible combinations of intermediate, start and nodes

    for intermediate, start_node,end_node\
          in itertools.product\
            (range(MAX_LENGTH),range(MAX_LENGTH), range(MAX_LENGTH)):

        # if start_node and end_node are the same then the distance between them is set to 0.

        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # if start_node and end node are not equal then the following
        # formula computes the shortest distance between start_node and
        # end_node by considering all intermediate nodes

        distance[start_node][end_node] = min(distance[start_node][end_node],
                        distance[start_node][intermediate]+distance[intermediate][end_node])

        # after all iterations are complete the distance matrix contains the shortest path
        # between every pair of nodes in the graph

    # prints the updated matrix
    print(distance)


# calls the floyd function providing the graph matrix as input which finds
# the shortest path between nodes

floyd(graph)
