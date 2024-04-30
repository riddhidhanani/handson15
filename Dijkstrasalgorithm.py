import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('inf') for node in graph}
    # Distance from start node to itself is 0
    distances[start] = 0
    # Priority queue to store nodes to be visited, with their distances
    priority_queue = [(0, start)]

    while priority_queue:
        # Pop the node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Check if the current distance is smaller than the stored distance for the current node
        if current_distance > distances[current_node]:
            continue

        # Iterate through neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If the distance to the neighbor through the current node is smaller than the stored distance
            if distance < distances[neighbor]:
                # Update the distance
                distances[neighbor] = distance
                # Add the neighbor to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 7},
    'D': {'B': 5, 'C': 7}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, "to all other nodes:", shortest_distances)
