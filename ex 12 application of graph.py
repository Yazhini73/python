def dijkstra(graph, start_index):
    num_nodes = len(graph)
    visited = [False] * num_nodes           # Track visited nodes
    distances = [float('inf')] * num_nodes  # Initialize distances as infinite
    distances[start_index] = 0               # Distance to start node is 0

    for _ in range(num_nodes):
        # Select the unvisited node with the smallest distance
        min_distance = float('inf')
        min_index = -1
        for i in range(num_nodes):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                min_index = i

        # Mark this node as visited
        visited[min_index] = True

        # Update distances to adjacent nodes
        for j in range(num_nodes):
            # If there is an edge and node j is unvisited
            if graph[min_index][j] > 0 and not visited[j]:
                new_dist = distances[min_index] + graph[min_index][j]
                if new_dist < distances[j]:
                    distances[j] = new_dist

    return distances

# Define the graph nodes (using letters)
nodes = ['A', 'B', 'C', 'D', 'E', 'F']

# Graph represented as adjacency matrix (0 means no edge)
graph = [
    #A  B  C  D  E  F
    [ 0, 4, 2, 0, 0, 0],  # A
    [ 4, 0, 1, 5, 0, 0],  # B
    [ 2, 1, 0, 8, 10, 0], # C
    [ 0, 5, 8, 0, 2, 6],  # D
    [ 0, 0, 10, 2, 0, 3], # E
    [ 0, 0, 0, 6, 3, 0]   # F
]

start_node = 'A'
start_index = nodes.index(start_node)

# Run Dijkstra's algorithm
shortest_distances = dijkstra(graph, start_index)

# Print the shortest distances
print(f"Shortest distances from node {start_node}:")
for i in range(len(nodes)):
    print(f"  To node {nodes[i]}: {shortest_distances[i]}")
