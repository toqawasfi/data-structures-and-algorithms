class Node:
    def __init__(self, value=None):
        """
        Initialize a Node object with the given value.

        Parameters:
            value (any, optional): The value to be stored in the Node. Default is None.
        """
        self.value = value

    def __str__(self):
        """
        Return the string representation of the Node's value.
        """
        return str(self.value)


class Edge:
    def __init__(self, vertex, weight=0):
        """
        Initialize an Edge object connecting to the given vertex with an optional weight.

        Parameters:
            vertex (Node): The vertex (Node) that this edge connects to.
            weight (float, optional): The weight of the edge. Default is 0.
        """
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
        Initialize an empty Graph with an adjacency list to store the vertices and edges.
        """
        self.adj_list = {}
        self.size = 0

    def add_node(self, value):
        """
        Add a new vertex (Node) to the graph.

        Parameters:
            value (any): The value to be stored in the new vertex.

        Returns:
            Node: The newly created vertex (Node).
        """
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        self.size += 1
        return new_vertex

    def add_edge(self, node1, node2, weight=0):
        """
        Add a new edge connecting two vertices (Nodes) with an optional weight.

        Parameters:
            node1 (Node): The first vertex (Node) of the edge.
            node2 (Node): The second vertex (Node) of the edge.
            weight (float, optional): The weight of the edge. Default is 0.

        Returns:
            str: If either of the given nodes does not exist in the graph, returns an error message.
        """
        if node1 not in self.adj_list.keys() or node2 not in self.adj_list.keys():
            return "This node does not exist"

        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        """
        Return a string representation of the graph, showing its adjacency list.
        """
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output

    def get_vertices(self):
        """
        Print all vertices (Nodes) in the graph.
        """
        for vertex in self.adj_list.keys():
            print(vertex)

    def get_neighbors(self, vertex):
        """
        Get all neighboring vertices (Nodes) connected to the given vertex.

        Parameters:
            vertex (Node): The vertex (Node) for which to retrieve neighbors.

        Returns:
            list: A list of neighboring vertices (Nodes).
        """
        neighbors = self.adj_list.get(vertex, [])
        return neighbors

    def get_size(self):
        """
        Print the number of vertices in the graph.
        """
        print(self.size)

    def depth_first(self, start_vertex):
        """
        Perform a pre-order depth-first traversal of the graph starting from the given vertex.

        Parameters:
            start_vertex (Node): The starting vertex (Node) of the traversal.

        Returns:
            list: A list of vertices in their pre-order depth-first traversal order.
        """
        traversal_order = []

        def dfs(vertex):
            vertex.visited = True
            traversal_order.append(vertex.value)

            for edge in self.adj_list[vertex]:
                if not edge.vertex.visited:
                    dfs(edge.vertex)

        # Mark all vertices as unvisited before starting the traversal
        for vertex in self.adj_list.keys():
            vertex.visited = False

        dfs(start_vertex)
        return traversal_order
