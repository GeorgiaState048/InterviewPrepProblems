from collections import defaultdict


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):
        print(self.graph)
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)

        # OR

        visited = set()
        stack = []
        stack.append(v)
        print()
        while stack:
            s = stack.pop(len(stack) - 1)
            if s not in visited:
                print(s, end=' ')
                visited.add(s)

            for i in self.graph[s]:
                if i not in visited:
                    stack.append(i)


# Driver code


# Create a graph given
# in the above diagram
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
"""g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)"""

g.DFS('A')
