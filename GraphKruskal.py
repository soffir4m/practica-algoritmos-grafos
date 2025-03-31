from collections import defaultdict

class Graph:
    def __init__(self, vertices=None, directed=False):
        self.directed = directed
        if directed:
            self.adj_list = defaultdict(list)
        else:
            self.V = vertices
            self.edges = []

    def addEdge(self, u, v, w):
        self.edges.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i, e = 0, 0
        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = self.edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("\nAristas del MST (índices):")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{u} -- {v} == {weight}")

        print("\nAristas del MST (letras):")
        indice_a_letra = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f'}
        for u, v, weight in result:
            print(f"{indice_a_letra[u]} -- {indice_a_letra[v]} == {weight}")

        print("\nCosto mínimo total:", minimumCost)
