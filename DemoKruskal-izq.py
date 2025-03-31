from GraphKruskal import Graph
import networkx as nx
import matplotlib.pyplot as plt

# Cierra figuras anteriores
plt.close('all')

# Mapeo de letras a valores numéricos
valor = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
letra_a_indice = {letra: idx for idx, letra in enumerate(valor)}

# Lista de aristas del grafo (lado izquierdo de la imagen)
aristas_letras = [
    ('a', 'b'), ('a', 'c'), ('a', 'f'),
    ('b', 'c'), ('b', 'e'),
    ('c', 'd'), ('c', 'e'), ('c', 'f'),
    ('d', 'e'),
    ('e', 'f')
]

# Crear grafo y calcular pesos
g = Graph(6)  # a-f = 6 nodos
for u, v in aristas_letras:
    peso = valor[u] + valor[v]
    g.addEdge(letra_a_indice[u], letra_a_indice[v], peso)

print("Resultado de Kruskal:")
g.KruskalMST()

# Visualización con NetworkX
G = nx.Graph()
for letra in valor:
    G.add_node(letra)

for u, v in aristas_letras:
    peso = valor[u] + valor[v]
    G.add_edge(u, v, weight=peso)

mst = nx.minimum_spanning_tree(G)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 5))
nx.draw(G, pos, with_labels=True, node_color='lightcoral', node_size=800, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Dibujar solo las aristas del MST en rojo
nx.draw_networkx_edges(mst, pos, edge_color='red', width=2)

plt.title("Árbol de Expansión Mínima (Kruskal)")
plt.axis('off')
plt.show()
plt.close()
