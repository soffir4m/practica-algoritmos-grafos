from GraphVariant1 import Graph
#pregunta 1 de la practica
def run_grafo_1():
    print("\nGRAFO 1 - Topological Sort")
    g = Graph()
    g.addEdge('0', '4')
    g.addEdge('1', '4')
    g.addEdge('2', '4')
    g.addEdge('3', '2')
    g.addEdge('4', '5')
    g.topologicalSort()

def run_grafo_2():
    print("\nGRAFO 2 - Topological Sort")
    g = Graph()
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('A', 'E')
    g.addEdge('B', 'D')
    g.addEdge('C', 'D')
    g.topologicalSort()

def run_grafo_3():
    print("\nGRAFO 3 - Topological Sort")
    g = Graph()
    g.addEdge('a', 'b')
    g.addEdge('b', 't')
    g.addEdge('b', 'm')
    g.addEdge('t', 'g')
    g.addEdge('g', 'k')
    g.addEdge('s', 'g')
    g.topologicalSort()

def main():
    run_grafo_1()
    run_grafo_2()
    run_grafo_3()

if __name__ == "__main__":
    main()
