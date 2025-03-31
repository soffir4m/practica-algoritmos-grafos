from GraphTopological import Graph
import networkx as nx
import matplotlib.pyplot as plt

def graficar_grafo_dirigido():
    G = nx.DiGraph()
    G.add_edges_from([
        ('a', 'b'),
        ('a', 'c'),
        ('b', 'd'),
        ('c', 'd')
    ])

    pos = {'a': (0, 1), 'b': (1, 2), 'c': (1, 0), 'd': (2, 1)}
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, arrows=True, node_color='skyblue', node_size=800, font_weight='bold')
    plt.title("Grafo Dirigido - Imagen Derecha")
    plt.axis('off')
    plt.show()

def main():
    g = Graph(4)  # Nodos: a=0, b=1, c=2, d=3

    g.addEdge(0, 1)  # a → b
    g.addEdge(0, 2)  # a → c
    g.addEdge(1, 3)  # b → d
    g.addEdge(2, 3)  # c → d

    print("Ordenamiento topológico del grafo:")
    g.topologicalSort()

    # Graficar
    graficar_grafo_dirigido()

if __name__ == "__main__":
    main()
