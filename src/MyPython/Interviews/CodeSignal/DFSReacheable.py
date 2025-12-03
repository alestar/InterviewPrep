"""
implement a recursive dfs(graph,v) method that travers the graph for each vertex getting a list of vertices that are reachable from that vertex

"""
def dfs(graph, v, visited, result):
    visited.add(v)
    result.append(v)
    for neighbor in graph.get(v, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
def reachable_vertices(graph):
    all_reachable = {}
    for vertex in graph:
        visited = set()
        result = []
        dfs(graph, vertex, visited, result)
        all_reachable[vertex] = result
    return all_reachable

# Example usage:
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3],
    4: [5],
    5: []
}
print(reachable_vertices(graph))
# Output:
# {
#   0: [0, 1, 2, 3],
#   1: [1, 2, 0, 3],
#   2: [2, 0, 1, 3],
#   3: [3],
#   4: [4, 5],
#   5: [5]
# }
graph1 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
print(reachable_vertices(graph1))
