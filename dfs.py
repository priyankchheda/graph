from graph import Graph


def dfs(g, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for nextNode in g.neighbours(vertex):
                if nextNode not in visited:
                    stack.append(nextNode)
    return visited


g = {
    '1': ['2', '3'],
    '2': ['3', '1'],
    '3': ['1', '2', '4'],
    '4': ['3']
}
g = Graph(g)
print(dfs(g, '1'))