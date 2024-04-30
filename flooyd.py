def floyd_warshall(graph):
    # Number of vertices in the graph
    n = len(graph)
    
    # Initialize the distance matrix with the graph values
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    
    # Update the distance matrix with direct edges
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]
    
    # Compute shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example graph represented as an adjacency matrix
graph = [
    [0, 5, float('inf'), 10],
    [float('inf'), 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 1],
    [float('inf'), float('inf'), float('inf'), 0]
]

result = floyd_warshall(graph)
print("Shortest distances between every pair of vertices:")
for row in result:
    print(row)
