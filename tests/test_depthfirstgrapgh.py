from Gragh.graph import Graph
from Gragh.graphdepthfirst import depth_first
import pytest


def test_depth_first_linear_graph():
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("C", "D")

    start_node = "A"
    traversal_result = depth_first(my_graph, start_node)
    assert traversal_result == ["A", "B", "C", "D"]



def test_depth_first_branching_graph():
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    my_graph.add_vertex("E")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("A", "D")
    my_graph.add_edge("D", "E")

    start_node = "A"
    traversal_result = depth_first(my_graph, start_node)
    assert traversal_result == ["A", "B", "C", "D", "E"]


def test_depth_first_disconnected_graph():
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_vertex("D")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("C", "D")

    start_node = "A"
    traversal_result = depth_first(my_graph, start_node)
    assert traversal_result == ["A", "B"]