from depthfirst import Graph

graph = Graph()
node_a = graph.add_node("A")
node_b = graph.add_node("B")
node_c = graph.add_node("C")
node_d = graph.add_node("D")
node_e = graph.add_node("E")

graph.add_edge(node_a, node_b)
graph.add_edge(node_a, node_c)
graph.add_edge(node_b, node_d)
graph.add_edge(node_b, node_e)

start_vertex = node_a
result = graph.depth_first(start_vertex)
# print("Pre-Order Depth-First Traversal from vertex {}: {}".format(start_vertex.value, result))
print(result)