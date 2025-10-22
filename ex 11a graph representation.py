class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        # Update adjacency list
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # For undirected graph

        # Update adjacency matrix
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

    def print_adj_list(self):
        print("Adjacency List:")
        for i in range(self.V):
            print(f"Vertex {i}: ", end="")
            for j in self.adj_list[i]:
                print(f"{j} -> ", end="")
            print("None")

    def print_adj_matrix(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))


# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_adj_list()
G.print_adj_matrix()
