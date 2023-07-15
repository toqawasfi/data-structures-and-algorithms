from vertex import Node

class Edge:
    def __init__(self,vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}
        self.size=0

    def add_node(self, value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        self.size+=1
        return new_vertex
    
    def add_edge(self,node1, node2, weight=0):

        if not node1 in self.adj_list.keys():
            return("this node does not exist")
        
        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output += f'{vertex} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex} -----> '
            output += '\n'
        return output
    def get_vertices(self):
        list1=list(self.adj_list.keys()) 
        for i in list1 :
            print (i)

    
    def get_neighbors(self, vertex):
        neighbors = self.adj_list.get(vertex, [])
        
        return neighbors
    def get_size(self):
       print(self.size)