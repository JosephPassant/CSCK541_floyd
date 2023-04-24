"""Floyd Warshall Algorithm"""

import sys
import itertools

NO_PATH = sys.maxsize

#Update the graph below to test different graphs (must be n x n matrix)

graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]

def floyd_warshall_iterative(distance):

    """
    A simple implementation of Floyd's algorithm

    The function takes a n x n matrix as an input and returns an updated
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

        # if the distance between start_node and end_node is greater than
        # the distance between start_node and intermediate plus the distance
        # between intermediate and end_node then the distance between
        # start_node and end_node is updated to the new shorter distance
        distance[start_node][end_node] = min(distance[start_node][end_node],
                        distance[start_node][intermediate]+distance[intermediate][end_node])

        # after all iterations are complete the distance matrix contains the shortest path
        # between every pair of nodes in the graph

    return distance

if __name__ == "__main__":
    print("Shortest path matrix using floyd_warshall_iterative function")
    for row in floyd_warshall_iterative(graph):
        print(row)
