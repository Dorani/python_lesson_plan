class Graph:
    def __init__(self):
        # Initialize an empty adjacency list to represent the graph
        self.adj_list = {}

    def print_graph(self):
        # Print the adjacency list of each vertex
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        # Add a new vertex to the graph if it does not already exist
        if vertex not in self.adj_list.keys():
            # Initialize the vertex with an empty list of connections
            self.adj_list[vertex] = []
            return True
        # Return False if the vertex already exists
        return False

    def add_edge(self, v1, v2):
        # Add an undirected edge between two vertices if both vertices exist
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # Add the connection from v1 to v2
            self.adj_list[v1].append(v2)
            # Add the connection from v2 to v1
            self.adj_list[v2].append(v1)
            return True
        # Return False if either of the vertices does not exist
        return False

    def remove_edge(self, v1, v2):
        # Remove the undirected edge between two vertices if both exist
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys(): 
            try:
                # Try to remove v2 from the list of v1's connections
                self.adj_list[v1].remove(v2)
                # Try to remove v1 from the list of v2's connections
                self.adj_list[v2].remove(v1)
            except ValueError:
                # If the edge is not found, pass (do nothing)
                pass
            return True
        # Return False if either vertex does not exist
        return False

    def remove_vertex(self, vertex):
        # Remove a vertex and all its connections from the graph
        if vertex in self.adj_list.keys():
            # Loop through each connected vertex and remove the edge to the current vertex
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            # Delete the vertex from the adjacency list
            del self.adj_list[vertex]
            return True
        # Return False if the vertex does not exist
        return False        

# Example usage
my_graph = Graph()
# Adding vertices
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

# Adding edges
my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

# Print the graph before removing a vertex
print('Graph before remove_vertex():')
my_graph.print_graph()
# Expected output:
# A : ['B', 'C', 'D']
# B : ['A', 'D']
# C : ['A', 'D']
# D : ['A', 'B', 'C']

# Remove vertex 'D' and all its associated edges
my_graph.remove_vertex('D')

# Print the graph after removing vertex 'D'
print('\nGraph after remove_vertex():')
my_graph.print_graph()
# Expected output:
# A : ['B', 'C']
# B : ['A']
# C : ['A']

"""
EXPECTED OUTPUT:
----------------
    Graph before remove_vertex():
    A : ['B', 'C', 'D']
    B : ['A', 'D']
    C : ['A', 'D']
    D : ['A', 'B', 'C']

    Graph after remove_vertex():
    A : ['B', 'C']
    B : ['A']
    C : ['A']
"""
