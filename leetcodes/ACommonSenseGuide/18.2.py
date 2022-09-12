class WeightedGraphVertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}
    def add_adjacent_vertex(self, vertex, weight):
        self.adjacent_vertices[vertex] = weight
        
    