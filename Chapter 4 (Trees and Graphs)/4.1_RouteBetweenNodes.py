"""Route Between Nodes: Given a directed graph, design an algorithm
to find out whether there is a route between two nodes."""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def checkRoute(self, s, d):

        visited = set()
        queue = []
        queue.append(s)

        while queue:

            s = queue.pop(0)
            if d in visited:
                return True
            if s not in visited:
                visited.add(s)
                print(s, end=' ')
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
        return False

g = Graph()
g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'A')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'A')
g.addEdge('C', 'F')
g.addEdge('D', 'B')
g.addEdge('E', 'B')
g.addEdge('E', 'F')
g.addEdge('F', 'C')
g.addEdge('F', 'E')
print(g.checkRoute('A', 'D'))
