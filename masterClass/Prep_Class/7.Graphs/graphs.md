# Graph Data Structure in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Graph Terminology](#graph-terminology)
3. [Types of Graphs](#types-of-graphs)
4. [Graph Representation](#graph-representation)
5. [Graph Traversal](#graph-traversal)
   - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
   - [Depth-First Search (DFS)](#depth-first-search-dfs)
6. [Graph Implementation](#graph-implementation)
7. [Example Code](#example-code)
8. [Use Cases](#use-cases)
9. [Time Complexity](#time-complexity)

---

## Introduction

A **graph** is a non-linear data structure that consists of a set of nodes (vertices) and edges connecting these nodes. Graphs are used to represent networks such as social media connections, transportation systems, web page links, and more.

## Graph Terminology

- **Vertex (Node)**: A fundamental unit representing a data point in the graph.
- **Edge**: A connection between two vertices.
- **Directed Graph**: Edges have a direction, going from one vertex to another (like a one-way street).
- **Undirected Graph**: Edges do not have a direction (like a two-way street).
- **Weighted Graph**: Each edge has a weight (cost) associated with it.
- **Unweighted Graph**: All edges have the same weight or no weight at all.
- **Path**: A sequence of vertices connected by edges.
- **Cycle**: A path that starts and ends at the same vertex.

## Types of Graphs

1. **Directed vs. Undirected Graphs**:

   - In **directed graphs**, edges have a direction, represented by arrows.
   - In **undirected graphs**, edges have no direction, represented by simple lines.

2. **Weighted vs. Unweighted Graphs**:

   - In **weighted graphs**, edges carry a weight (distance, cost, etc.).
   - In **unweighted graphs**, all edges are considered equal.

3. **Connected vs. Disconnected Graphs**:
   - A **connected graph** has a path between every pair of vertices.
   - A **disconnected graph** has at least one pair of vertices without a connecting path.

## Graph Representation

Graphs can be represented in multiple ways:

1. **Adjacency Matrix**:

   - A 2D array where the cell at row `i` and column `j` represents the presence (and possibly the weight) of an edge between vertex `i` and vertex `j`.
   - Suitable for dense graphs.

2. **Adjacency List**:
   - A list where each index represents a vertex, and the corresponding value is a list of adjacent vertices.
   - More efficient for sparse graphs.

### Example Representations

For a graph with vertices A, B, C, and edges A-B, A-C:

- **Adjacency Matrix**:
- { 'A': ['B', 'C'], 'B': ['A'], 'C': ['A'] }

## Graph Traversal

Traversal algorithms visit nodes in a graph systematically. Two common methods are:

### Breadth-First Search (BFS)

- Visits all nodes at the present depth before moving to the next level.
- Uses a queue to track the nodes to be visited.
- Suitable for finding the shortest path in unweighted graphs.

### Depth-First Search (DFS)

- Visits a node and explores as far as possible along each branch before backtracking.
- Uses a stack (or recursion) to explore the graph.
- Suitable for tasks like detecting cycles or paths.

## Graph Implementation

Graphs can be implemented using an adjacency list or an adjacency matrix. In this example, we'll use an adjacency list for its simplicity and efficiency.

## Example Code

Here is a simple implementation of an unweighted, undirected graph using an adjacency list in Python:

```python
class Graph:
  def __init__(self):
      self.adjacency_list = {}

  def add_vertex(self, vertex):
      # Add a new vertex to the graph
      if vertex not in self.adjacency_list:
          self.adjacency_list[vertex] = []

  def add_edge(self, vertex1, vertex2):
      # Add an edge between two vertices (undirected)
      if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
          self.adjacency_list[vertex1].append(vertex2)
          self.adjacency_list[vertex2].append(vertex1)

  def remove_edge(self, vertex1, vertex2):
      # Remove the edge between two vertices
      if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
          try:
              self.adjacency_list[vertex1].remove(vertex2)
              self.adjacency_list[vertex2].remove(vertex1)
          except ValueError:
              pass

  def remove_vertex(self, vertex):
      # Remove a vertex and its connected edges
      if vertex in self.adjacency_list:
          for adjacent in self.adjacency_list[vertex]:
              self.adjacency_list[adjacent].remove(vertex)
          del self.adjacency_list[vertex]

  def display(self):
      # Display the graph as an adjacency list
      for vertex in self.adjacency_list:
          print(vertex, ":", self.adjacency_list[vertex])

  def bfs(self, start_vertex):
      # Perform Breadth-First Search
      visited = set()
      queue = [start_vertex]
      result = []
      while queue:
          current = queue.pop(0)
          if current not in visited:
              visited.add(current)
              result.append(current)
              for neighbor in self.adjacency_list[current]:
                  if neighbor not in visited:
                      queue.append(neighbor)
      return result

  def dfs(self, start_vertex):
      # Perform Depth-First Search
      visited = set()
      stack = [start_vertex]
      result = []
      while stack:
          current = stack.pop()
          if current not in visited:
              visited.add(current)
              result.append(current)
              for neighbor in reversed(self.adjacency_list[current]):
                  if neighbor not in visited:
                      stack.append(neighbor)
      return result
```

## Use Cases

Graphs are widely used in various applications:

- **Social Networks**: Representing connections between people.
- **Web Crawlers**: Indexing web pages by crawling from one link to another.
- **Maps and Navigation**: Finding the shortest path between locations.
- **Scheduling Problems**: Task scheduling, job sequencing, etc.
- **Computer Networks**: Routing protocols in networking.

## Time Complexity

| Operation            | Adjacency List | Adjacency Matrix |
| -------------------- | -------------- | ---------------- |
| Add Vertex           | O(1)           | O(V^2)           |
| Add Edge             | O(1)           | O(1)             |
| Remove Vertex        | O(V + E)       | O(V^2)           |
| Remove Edge          | O(E)           | O(1)             |
| Check if Edge Exists | O(V)           | O(1)             |
| Graph Traversal      | O(V + E)       | O(V^2)           |

Where **V** is the number of vertices and **E** is the number of edges.

Graphs are a versatile and powerful data structure used in many fields of computer science. This guide provides a basic understanding of graphs, their types, traversal techniques, and example implementations. More advanced topics such as weighted graphs, shortest path algorithms (Dijkstra's, Bellman-Ford), and minimum spanning trees can further enhance graph-related applications.
