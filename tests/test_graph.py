import pytest
from Gragh.graph import Graph

def test_add_vertex():
    g = Graph()
    g.add_vertex('A')
    assert 'A' in g.get_vertices()

def test_add_edge():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_edge('A', 'B', weight=1)
    assert ('B', 1) in g.get_neighbors('A')
    assert ('A', 1) in g.get_neighbors('B')

def test_get_vertices():
    g = Graph()
    assert g.get_vertices() == []
    g.add_vertex('A')
    g.add_vertex('B')
    assert g.get_vertices() == ['A', 'B']

def test_get_neighbors():
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_edge('A', 'B', weight=1)
    g.add_edge('B', 'C', weight=2)
    assert g.get_neighbors('A') == [('B', 1)]
    assert g.get_neighbors('B') == [('A', 1), ('C', 2)]
    assert g.get_neighbors('C') == [('B', 2)]

def test_size():
    g = Graph()
    assert g.size() == 0
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    assert g.size() == 3

def test_single_vertex_and_edge():
    g = Graph()
    g.add_vertex('A')
    g.add_edge('A', 'A', weight=1)
    assert g.get_vertices() == ['A']
    assert g.get_neighbors('A') == [('A', 1)]
    assert g.size() == 1