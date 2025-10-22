def iterative_dfs(graph, start):
    visited = set()
    stack = [start]  # Stack (LIFO)
   
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add neighbors in reverse to maintain DFS order
            neighbors = graph.get(node, [])
            for neighbor in reversed(neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)

def bfs(graph, start):
    visited = set()
    queue = [start]  # Queue (FIFO)
    visited.add(start)
   
    while queue:
        node = queue.pop(0)  # pop(0) dequeues from front
        print(node, end=' ')
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['B'],
    'D': ['E'],
    'E': ['C'],

}

print("Iterative DFS Traversal:")
iterative_dfs(graph, 'A')  
# Output: A B D E F C

print("\nBFS Traversal:")
bfs(graph, 'A')  
# Output: A B C D E F
