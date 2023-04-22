"""A recursive solution to the Floyd Warshall algorithm"""

import sys

# Define a constant to represent no path between two nodes
# equal to the maximum integer value of the system
NO_PATH = sys.maxsize

#Update this graph to test different graphs (must be n x n matrix)
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]]


def floyd_warshall_recursive(dist):
    """
    Floyd_warshall_recursive takes a n x n matrix as an argument and defines
    the number of vertices in the graph.
    It then calls the recursive function shortest_path passing the number of vertices-1 
    as an argument. This represents the number of intermediate nodes (k).
    """
    vertices = len(dist)

    def shortest_path(k):
        """
        Shortest_path is the recursive function.
        It takes the number of intermediate nodes as an argument (k) defined as the number of vertices
        of an n x n matrix -1.
        It defines the base case as being where there are no intermediate nodes k ==-1.
        If k ==-1 then the current input matrix is returned.
        Else the minimum distance is calculated between the direct path betwenn i -> j
        and that using the intermediate node/s i -> k -> j.
        K is then decremented and the function is called recursively until k == -1.
        """
        # Base case
        if k == -1:
            return dist
        
        # Recursive case
        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        #Decrement k and call the function recursively
        k-=1
        return shortest_path(k)

    return shortest_path(vertices-1)

print("Shortest path matrix using floyd_warshall_recursive function")
for row in floyd_warshall_recursive(graph):
    print(row)
