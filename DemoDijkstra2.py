import networkx as nx
import matplotlib.pyplot as plt
from GraphDijkstra import Graph

def main_grafo_ciudades():
    print("\n GRAFO DE CIUDADES ")
    nombres = [
        "Champlain", "Highgate Springs", "Derby Line", "St. Johnsbury",
        "White River Jct.", "Concord", "Reading", "Houlton", "Bangor",
        "Albany", "Newburgh", "New York", "Springfield", "Hartford",
        "New Haven", "Sturbridge", "Weston", "Boston", "Canton", "Providence"
    ]
    ciudades = {nombre: idx for idx, nombre in enumerate(nombres)}

    g2 = Graph(len(nombres), nombres)

    # Agregar aristas
    g2.agregar_arista(ciudades["Champlain"], ciudades["Highgate Springs"], 130)
    g2.agregar_arista(ciudades["Highgate Springs"], ciudades["St. Johnsbury"], 60)
    g2.agregar_arista(ciudades["Derby Line"], ciudades["St. Johnsbury"], 50)
    g2.agregar_arista(ciudades["St. Johnsbury"], ciudades["White River Jct."], 64)
    g2.agregar_arista(ciudades["White River Jct."], ciudades["Concord"], 105)
    g2.agregar_arista(ciudades["Concord"], ciudades["Reading"], 56)
    g2.agregar_arista(ciudades["Reading"], ciudades["Weston"], 19)
    g2.agregar_arista(ciudades["Weston"], ciudades["Boston"], 17)
    g2.agregar_arista(ciudades["Boston"], ciudades["Canton"], 20)
    g2.agregar_arista(ciudades["Canton"], ciudades["Providence"], 32)
    g2.agregar_arista(ciudades["Providence"], ciudades["New Haven"], 39)
    g2.agregar_arista(ciudades["New Haven"], ciudades["New York"], 81)
    g2.agregar_arista(ciudades["New York"], ciudades["Newburgh"], 69)
    g2.agregar_arista(ciudades["Newburgh"], ciudades["Albany"], 90)
    g2.agregar_arista(ciudades["Albany"], ciudades["Springfield"], 87)
    g2.agregar_arista(ciudades["Springfield"], ciudades["White River Jct."], 122)
    g2.agregar_arista(ciudades["Springfield"], ciudades["Sturbridge"], 36)
    g2.agregar_arista(ciudades["Hartford"], ciudades["Sturbridge"], 43)
    g2.agregar_arista(ciudades["Newburgh"], ciudades["Hartford"], 97)
    g2.agregar_arista(ciudades["Hartford"], ciudades["New Haven"], 39)
    g2.agregar_arista(ciudades["Reading"], ciudades["Bangor"], 227)
    g2.agregar_arista(ciudades["Bangor"], ciudades["Houlton"], 120)

    g2.dijkstra(ciudades["New York"])

    # Visualización
    edges = g2.get_edges()
    G = nx.Graph()
    G.add_weighted_edges_from(edges)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=8, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title("Mapa de Ciudades y Conexiones (Pesos en millas)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main_grafo_ciudades()