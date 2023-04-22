"""A recursive solution to the Floyd Warshall algorithm"""

def floyd_warshall_recursive(dist):
    """
    Outer function
    Taks a graph as an argument, defines number of vertices
    iterates for number of intermediate node for all combinations of start and end node 
    returns minimum distance between nodes
    """
    vertices = len(dist)

    def shortest_path(i,j,k):
        """
        defines base case as no intermediate nodes
        if k ==-1 then the current value is dist is returned
        else the minimum distance is calculated between the direct path and that using the 
        intermediate node/s
        """
        if k == -1:
            return dist[i][j]
        else:
            return min(shortest_path(i, j, k - 1), shortest_path(i, k, k - 1)/
                        + shortest_path(k, j, k - 1))
           
    for k in range (vertices):
        for i in range (vertices):
            for j in range(vertices):
                dist[i][j] = shortest_path(i, j, k)
    return dist
