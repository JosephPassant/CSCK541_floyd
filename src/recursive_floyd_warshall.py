"""A recursive solution to the Floyd Warshall algorithm."""

import sys

NO_PATH = sys.maxsize

#Update the graph below to test different graphs (must be n x n matrix)

graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]


def floyd_warshall_recursive(dist):
    """
    Floyd_warshall_recursive takes a n x n edge weight matrix as an argument and defines
    the number of vertices.
    It then calls the recursive function shortest_path passing the input graph and the number\
    of vertices-1 as an arguments for i, j and k respectively.
    """

    vertices = len(dist)

    def shortest_path(dist,i, j, k):

        """
        Shortest_path is the recursive function.
        It takes an weighted distance matrix, i, j and k as arguments.
        dist is the input matrix passed by the outer floyd_warshall_recursive function.
        i and j are the start and end nodes respectively, k is the number of intermediate nodes.
        i and j are all set to vertices-1 (the number of vertices in the graph minus 1).
        The function defines the base case as being where there are no intermediate nodes k ==-1.
        If k ==-1 then the current dist matrix is returned.
        The function loops through all combinations of j, i and k and updates the shortest\
        distance between i and j by considering the minimum between the current distance between\
        i and j and the distance between i and k plus the distance between k and j. 
        """
        # if k is -1 then have finished processing all pairs of i and j for all values of k
        # and the distance matrix is returned
        if k == -1:
            return dist

        # If i is -1 then have finished prcessing al rows for the current k
        # the fucntion is called for the next vlaue of k and i and j are reset v-1
        if i == -1:
            return shortest_path(dist, vertices-1, vertices-1, k-1)

        # if j is -1 then have finished processing all columns for the current k and i
        # the function is called for the next column for i and j is reset to v-1
        if j == -1:
            return shortest_path(dist, i-1, vertices-1, k)

        # update the shortest distance betwen i and j by cosidering the minimum between\
        # the current distance between i and j and the distance between i and k plus\
        # the distance between k and j
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        # decrement j by 1 and call the function again for current i and k
        return shortest_path(dist, i, j-1, k)

    # call the shortest path function with i, j and k set to vertices-1
    return shortest_path(dist, vertices-1, vertices-1, vertices-1)

if __name__ == "__main__":
    print("Shortest path matrix using floyd_warshall_recursive function")
    for row in floyd_warshall_recursive(graph):
        print(row)
