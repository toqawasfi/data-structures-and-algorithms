class Graph:
    def __init__(self):
        """
        Initialize an empty graph with no vertices
        """
        self.vertices = {}
    
    def add_vertex(self, value):
        """
        Add a vertex to the graph
        value -- the value of the vertex
        """
        if value not in self.vertices:
            self.vertices[value] = []
    
    def add_edge(self, vertex1, vertex2, weight=None):
        """
        Add a new edge between two vertices in the graph
        vertex1 -- the first vertex to be connected by the edge
        vertex2 -- the second vertex to be connected by the edge
        weight -- (optional) the weight of the edge
        """
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex1 == vertex2:
                self.vertices[vertex1].append((vertex2, weight))
            else:
                self.vertices[vertex1].append((vertex2, weight))
                self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        """
        Get all of the vertices in the graph
        """
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        """
        Get the neighbors of a given vertex
        vertex -- the vertex to get the neighbors of
        """
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return []
    
    def size(self):
        """
        Get the total number of vertices in the graph
        """
        return len(self.vertices)