def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    print(vertex.value)
    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices[adjacent_vertex.value]:
            continue
        dfs_traverse(adjacent_vertex, visited_vertices)
def bfs_traverse(start_vertex):
    queue = []
    visited_vertex = {}
    visited_vertex[start_vertex.value] = True
    while queue:
        current_vertex = queue.pop(0)
        print(current_vertex.value)
        for adjacent_vertex in current_vertex.adjacent_vertices:
            if not visited_vertex[adjacent_vertex.value]:
                visited_vertex[adjacent_vertex.value] = True
                queue.append(adjacent_vertex)
    
                
        
    