from GraphDijkstra import Graph

def main_grafo_letras():
    print("\n GRAFO DE LETRAS (A-H)")
    g = Graph(8)  # 8 nodos: A-H

    # Aristas con peso (según imagen)
    g.agregar_arista(0, 1, 3)
    g.agregar_arista(0, 2, 5)
    g.agregar_arista(0, 7, 10)
    g.agregar_arista(1, 2, 5)
    g.agregar_arista(1, 3, 8)
    g.agregar_arista(1, 4, 6)
    g.agregar_arista(1, 6, 6)
    g.agregar_arista(1, 7, 9)
    g.agregar_arista(2, 4, 4)
    g.agregar_arista(2, 5, 7)
    g.agregar_arista(2, 6, 6)
    g.agregar_arista(3, 6, 12)
    g.agregar_arista(3, 7, 2)
    g.agregar_arista(4, 5, 1)
    g.agregar_arista(4, 6, 9)
    g.agregar_arista(4, 7, 14)

    g.dijkstra(0)  # Desde nodo A (0)

if __name__ == "__main__":
    main_grafo_letras()
