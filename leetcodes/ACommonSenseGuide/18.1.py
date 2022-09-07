def dfs_traverse(vertex, visited_vertices={}):
    visited_vertices[vertex.value] = True
    print(vertex.value)
    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices[adjacent_vertex.value]:
            continue
        dfs_traverse(adjacent_vertex, visited_vertices)
