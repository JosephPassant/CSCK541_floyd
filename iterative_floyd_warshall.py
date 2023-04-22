"""Floyd Warshall Algorithm"""
import itertools


def floyd_warshall_iterative(distance):

    """
    A simple implementation of Floyd's algorithm

    Floyd is a function that takes a matrix as an input and returns an updated
    matrix displaying the shortest path between nodes of the input graph
    """

    max_length= len(distance[0])
    # iterates over all possible combinations of intermediate, start and nodes

    for intermediate, start_node,end_node\
          in itertools.product\
            (range(max_length),range(max_length), range(max_length)):

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
    return distance
