import matplotlib.pyplot as plt
import networkx as nx


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].append(v)
        else:
            self.graph[u] = [v]

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node} -> {', '.join(neighbors)}")

# Generar el grafo
g = Graph()
g.add_edge('a', 'b')
g.add_edge('a', 'c')
g.add_edge('a', 'd')
g.add_edge('c', 'd')

# imprimir el grafo
g.print_graph()

G = nx.Graph()

G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')

G.add_edge('a', 'b')
G.add_edge('a', 'c')
G.add_edge('a', 'd')
G.add_edge('c', 'd')

pos = {'a': (0, 0), 'b': (-1, -1), 'c': (1, -1), 'd': (0, -2)}
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold')
plt.show()