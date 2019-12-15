from graph import Graph


def find_path(g, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not g.is_vertex(start):
        return None
    for node in g.neighbours(start):
        if node not in path:
            newpath = find_path(g, node, end, path)
            return newpath
    return None


def find_all_path(g, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not g.is_vertex(start):
        return None
    paths = []
    for node in g.neighbours(start):
        if node not in path:
            newpaths = find_all_path(g, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


g = {
    '1': ['2', '3'],
    '2': ['3', '1'],
    '3': ['1', '2', '4'],
    '4': ['3']
}
g = Graph(g)
print(find_all_path(g, '1', '3'))