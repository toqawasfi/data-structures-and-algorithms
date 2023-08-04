from Gragh.graph import Graph
from Gragh.graphbridthfirst import breadth_first
import pytest

# Test BFS with a simple connected graph
def test_bfs_simple_connected_graph():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    # Perform BFS starting from node 1
    bfs_order = breadth_first(graph, 1)
    assert bfs_order == [1, 2, 3, 4]

    # Perform BFS starting from node 3
    bfs_order = breadth_first(graph, 3)
    assert bfs_order == [3, 1, 2, 4]

# Test BFS with a disconnected graph
def test_bfs_disconnected_graph():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_edge(1, 2)
    graph.add_edge(3, 4)

    # Perform BFS starting from node 1
    bfs_order = breadth_first(graph, 1)
    assert bfs_order == [1, 2]

    # Perform BFS starting from node 3
    bfs_order = breadth_first(graph, 3)
    assert bfs_order == [3, 4]

# Test BFS with a graph containing loops (self-edges)
def test_bfs_graph_with_loops():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(1, 1)  # Self-loop for vertex 1
    graph.add_edge(2, 2)  # Self-loop for vertex 2
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)

    # Perform BFS starting from node 1
    bfs_order = breadth_first(graph, 1)
    assert bfs_order == [1, 2, 3]

    # Perform BFS starting from node 2
    bfs_order = breadth_first(graph, 2)
    assert bfs_order == [2, 1, 3]

# Test BFS with a larger graph
def test_bfs_large_graph():
    graph = Graph()
    for i in range(1, 1001):
        graph.add_vertex(i)
        if i > 1:
            graph.add_edge(i, i-1)

    # Perform BFS starting from node 1
    bfs_order = breadth_first(graph, 1)
    assert bfs_order == list(range(1, 1001))