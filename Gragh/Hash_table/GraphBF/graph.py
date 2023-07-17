from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def breadth_first_search(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)

        while queue:
            current_node = queue.popleft()
            print(current_node, end=" ")

            if current_node in self.graph:
                for neighbor in self.graph[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)

    print("Breadth-First Search:")
    graph.breadth_first_search(1)
