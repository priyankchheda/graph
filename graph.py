from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph_dict = defaultdict(list)

    def add_edge(self, node, neighbour):
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print(f"{node} -> {neighbour}")

def main():
    g = Graph()
    g.add_edge('1', '2')
    g.add_edge('1', '3')
    g.add_edge('2', '3')
    g.add_edge('2', '1')
    g.add_edge('3', '1')
    g.add_edge('3', '2')
    g.add_edge('3', '4')
    g.add_edge('4', '3')
    g.show_edges()
    print(g.graph_dict)


if __name__ == "__main__":
    main()