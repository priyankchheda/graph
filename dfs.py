from graph import Graph


def dfs(g_obj, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for next_node in g_obj.neighbours(vertex):
                if next_node not in visited:
                    stack.append(next_node)
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


if __name__ == "__main__":
    main()
