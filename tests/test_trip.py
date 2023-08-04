from Gragh.graph import Graph
from Gragh.graphbusinesstrip import business_trip
import pytest

@pytest.mark.parametrize("cities, expected_cost", [
    (["Metroville", "Pandora"], 82),
    (["Arendelle", "New Monstropolis", "Naboo"], 115),
    (["Naboo", "Pandora"], None),
    (["Narnia", "Arendelle", "Naboo"], None),
    (["Narnia"], None),  # Only one city, no trip possible
    (["Arendelle", "New Monstropolis"], 42),  # Direct flight without intermediate cities
    (["Pandora", "Naboo"], None),  # No direct flight between Pandora and Naboo
    (["Atlantis", "Pandora"], None),  # Non-existent city Atlantis
    (["Narnia", "Hogwarts"], None),  # Both Narnia and Hogwarts are non-existent cities
    (["Arendelle", "Arendelle"], 0),  # Trip to the same city (self-loop)
])
def test_business_trip(cities, expected_cost):
    graph = Graph()

    # Adding vertices to the graph with optional weights
    graph.add_vertex("Metroville")
    graph.add_vertex("Pandora")
    graph.add_vertex("Arendelle")
    graph.add_vertex("New Monstropolis")
    graph.add_vertex("Naboo")
    graph.add_vertex("Narnia")
    graph.add_vertex("Hogwarts")

    graph.add_edge("Pandora","Arendelle", weight=150)
    graph.add_edge("Pandora","Metroville", weight=82)
    graph.add_edge("Metroville", "Arendelle", weight=99)
    graph.add_edge("Arendelle", "New Monstropolis", weight=42)
    graph.add_edge("New Monstropolis", "Metroville", weight=105)
    graph.add_edge("New Monstropolis", "Narnia", weight=37)
    graph.add_edge("Narnia", "Naboo", weight=250)
    graph.add_edge("Metroville", "Naboo", weight=26)
    graph.add_edge("Naboo", "New Monstropolis", weight=73)

    graph.add_edge("Metroville", "Metroville", weight=0)
    graph.add_edge("Pandora", "Pandora", weight=0)
    graph.add_edge("Arendelle", "Arendelle", weight=0)
    graph.add_edge("New Monstropolis", "New Monstropolis", weight=0)
    graph.add_edge("Naboo", "Naboo", weight=0)
    graph.add_edge("Narnia", "Narnia", weight=0)
    graph.add_edge("Hogwarts", "Hogwarts", weight=0)

    





    # Run the business_trip function and compare the result with the expected output
    assert business_trip(graph, cities) == expected_cost