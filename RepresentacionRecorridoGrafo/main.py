import matplotlib.pyplot as plt
import networkx as nx


class Vertice:
    def __init__(self, x):
        self.clave = x
        self.vecinos = []

class Grafo_ND_SP:
    def __init__(self):
        self.vertices = []

    def agregarVertice(self, n):
        self.vertices.append(n)

    def agregarArista(self, a, b):
        a.vecinos.append(b)
        b.vecinos.append(a)

    def mostrarVecinos(self):
        print("Datos del grafo:")
        for u in self.vertices:
            print("Vertice", u.clave, ":", end=" ")
            for v in u.vecinos:
                print(v.clave, "", end=" ")
            print("")

    def mostrarGrafo(self):
        G = nx.Graph()
        for u in self.vertices:
            for v in u.vecinos:
                G.add_edge(u.clave, v.clave)

        pos = {'a': (-10, -1), 'b': (5, 0), 'c': (5, -2), 'e': (10, -1), 'f': (-5, -2), 'g': (-5, 0)}
        nx.draw(G, pos, with_labels=True, node_size=500, node_color='red', font_size=12, font_weight='bold', font_color='white')
        plt.show()

grafo = Grafo_ND_SP()

a = Vertice('a')
b = Vertice('b')
c = Vertice('c')
e = Vertice('e')
f = Vertice('f')
g = Vertice('g')

grafo.agregarVertice(a)
grafo.agregarVertice(b)
grafo.agregarVertice(c)
grafo.agregarVertice(e)
grafo.agregarVertice(f)
grafo.agregarVertice(g)

grafo.agregarArista(a, g)
grafo.agregarArista(a, f)
grafo.agregarArista(g, b)
grafo.agregarArista(b, e)
grafo.agregarArista(e, c)
grafo.agregarArista(f, c)
grafo.agregarArista(a, f)
grafo.agregarArista(g, f)
grafo.agregarArista(g, c)
grafo.agregarArista(b, f)
grafo.agregarArista(b, c)

grafo.mostrarVecinos()
grafo.mostrarGrafo()