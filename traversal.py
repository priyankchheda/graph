""" Graph Traversal Algorithms
"""
from graph import Graph


def dfs(g_obj, start):
    """ depth first search graph traversal algorithm"""
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for next_node in g_obj.neighbours(vertex):
                if next_node not in visited:
                    stack.append(next_node)
    return visited

def bfs(g_obj, start):
    """ breath first search graph traversal algorithm"""
    visited, queue = set(), [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            for next_node in g_obj.neighbours(node):
                if next_node not in visited:
                    queue.append(next_node)
    return visited


def main():
    """ operational function """
    g_dict = {
        '1': ['2', '3'],
        '2': ['3', '1'],
        '3': ['1', '2', '4'],
        '4': ['3']
    }
    g_obj = Graph(g_dict)
    print(dfs(g_obj, '1'))
    print(bfs(g_obj, '1'))


if __name__ == "__main__":
    main()
