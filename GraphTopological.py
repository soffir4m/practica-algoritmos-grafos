from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSort(self):
        in_degree = [0] * self.V

        # Calcular grados de entrada
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        # Cola con nodos de grado de entrada 0
        queue = deque([i for i in range(self.V) if in_degree[i] == 0])
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if len(topo_order) != self.V:
            print("El grafo tiene un ciclo, no se puede hacer ordenamiento topológico.")
        else:
            letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
            orden_letras = [letras[i] for i in topo_order]
            print("Ordenamiento topológico (índices):", topo_order)
            print("Ordenamiento topológico (letras):", " → ".join(orden_letras))
