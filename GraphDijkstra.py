import sys
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices, labels=None):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.labels = labels if labels else [str(i) for i in range(vertices)]

    def agregar_arista(self, u, v, peso):
        self.graph[u][v] = peso
        self.graph[v][u] = peso

    def get_edges(self):
        edges = []
        for u in range(self.V):
            for v in range(u + 1, self.V):
                if self.graph[u][v] > 0:
                    edges.append((self.labels[u], self.labels[v], self.graph[u][v]))
        return edges

    def min_distance(self, dist, sptSet):
        min_val = sys.maxsize
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, sptSet)
            if u == -1:
                break
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not sptSet[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        print(f"\n🔹 Distancias desde {self.labels[src]}:\n")
        for i in range(self.V):
            print(f"{self.labels[i]} → {dist[i]}")