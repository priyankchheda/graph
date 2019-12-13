class Graph:
    def __init__(self, graph_dict=None):
        """ initialize a graph object
            if no dictionary or none is given, an empty dictionary
            will be used
            :param graph_dict: initial graph setup
        """
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_vertex(self, node):
        """ Adds new vertex to graph. If vertex is already present in graph,
            no action will take place.
            :param node: new node to be added to graph
        """
        if node not in self.graph_dict:
            self.graph_dict[node] = []

    def add_edge(self, node, neighbour):
        """ Adds new directed edge to graph starting from 'node' to 'neighbor'
            It will insert node to graph, if the node is not already present
            :param node: starting graph vertex
            :param neighbour: ending graph vertex
        """
        if node not in self.graph_dict:
            self.add_vertex(node)
        if neighbour not in self.graph_dict:
            self.add_vertex(neighbour)
        self.graph_dict[node].append(neighbour)

    def order(self):
        """ Order returns the order of a graph i.e. number of vertices
            :returns: returns number of vertices
        """
        return len(self.graph_dict.keys())

    def neighbours(self, node):
        """ returns all vertices of given node
            :param node: graph vertex
            :returns: all node neighbour vertices
        """
        return self.graph_dict[node]

    def show_edges(self):
        """ show all the graph edges """
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print(f"{node} -> {neighbour}")


def main():
    g = {
        '1': ['2', '3'],
        '2': ['3', '1'],
        '3': ['1', '2', '4'],
        '4': ['3']
    }
    g = Graph(g)
    g.show_edges()
    print(g.graph_dict)


if __name__ == "__main__":
    main()