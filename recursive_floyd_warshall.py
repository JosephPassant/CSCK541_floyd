"""A recursive solution to the Floyd Warshall algorithm"""

def floyd_warshall_recursive(dist):
    """
    This outer function takes a graph as an argument and defines
    the number of vertices in the graph.
    It then calls the recursive function shortest_path passing the number of vertices-1 
    as an argument. This represents the number of intermediate nodes (k).
    """
    vertices = len(dist)

    def shortest_path(k):
        """
        This is the recursive function.
        It defines the base case as being where there are no intermediate nodes k ==-1.
        If k ==-1 then the current input matrix is returned.
        Else the minimum distance is calculated between the direct path betwenn i -> j
        and that using the intermediate node/s i -> k -> j.
        K is then decremented and the function is called recursively until k == -1.
        """
        if k == -1:
            return dist

        for i in range(vertices):
            for j in range(vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        k-=1
        return shortest_path(k)

    return shortest_path(vertices-1)
