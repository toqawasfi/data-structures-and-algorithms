from graph import Graph

graph = Graph()
vertex_A = graph.add_node('A')
vertex_B = graph.add_node('B')
vertex_C = graph.add_node('C')
vertex_D = graph.add_node('D')

graph.add_edge(vertex_A, vertex_B, weight=3)
graph.add_edge(vertex_A, vertex_C, weight=5)
graph.add_edge(vertex_B, vertex_C, weight=2)
graph.add_edge(vertex_B, vertex_D, weight=4)
graph.add_edge(vertex_C, vertex_D, weight=1)
graph.get_size()

# Get neighbors of vertex 'A'
neighbors_of_A = graph.get_neighbors(vertex_A)
print("Neighbors of vertex A:")
for neighbor_edge in neighbors_of_A:
    print(f"Neighbor: {neighbor_edge.vertex}, Weight: {neighbor_edge.weight}")



