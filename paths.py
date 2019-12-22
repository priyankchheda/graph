""" finding paths from one graph node to another graph node
"""
from graph import Graph


def find_path(g_obj, start, end, path=[]):
    """ returns any existing path from start node to end node """
    path = path + [start]
    if start == end:
        return path
    if not g_obj.is_vertex(start):
        return None
    for node in g_obj.neighbours(start):
        if node not in path:
            newpath = find_path(g_obj, node, end, path)
            return newpath
    return None


def find_all_path(g_obj, start, end, path=[]):
    """ returns all existing path from start node to end node """
    path = path + [start]
    if start == end:
        return [path]
    if not g_obj.is_vertex(start):
        return None
    paths = []
    for node in g_obj.neighbours(start):
        if node not in path:
            newpaths = find_all_path(g_obj, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(g_obj, start, end, path=[]):
    """ returns shortest existing path from start node to end node """
    path = path + [start]
    if start == end:
        return path
    if not g_obj.is_vertex(start):
        return None
    shortest = None
    for node in g_obj.neighbours(start):
        if node not in path:
            newpath = find_shortest_path(g_obj, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def main():
    """ operational function """
    g_dict = {
        '1': ['2', '3'],
        '2': ['3', '1'],
        '3': ['1', '2', '4'],
        '4': ['3']
    }
    g_obj = Graph(g_dict)
    print(find_path(g_obj, '1', '3'))
    print(find_all_path(g_obj, '1', '3'))
    print(find_shortest_path(g_obj, '1', '3'))


if __name__ == "__main__":
    main()
