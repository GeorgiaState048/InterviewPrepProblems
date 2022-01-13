from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s, d):

        # Mark all the vertices as not visited
        visited = set()
        # Create a queue for BFS
        queue = []
        print(self.graph)
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            if d in visited:
                return True
            if s not in visited:
                visited.add(s)
                print(s, end=' ')
            #print(queue)
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
        return False

# Driver code

# Create a graph given in
# the above diagram
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

print(g.BFS('A', 'D'))
