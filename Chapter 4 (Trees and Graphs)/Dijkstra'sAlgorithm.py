"""Dijkstra's algorithm on a directed, cyclic graph where no weights are negative(is that possible lol)
   This is an ITERATIVE Algorithm."""
graph = {'a': {'b': 10, 'c': 3}, 'b': {'c': 1, 'd': 2}, 'c': {'b': 4, 'd': 8, 'e': 2}, 'd': {'e': 7}, 'e': {'d': 9}}


# graph = {'a': {'b': 1, 'c': 1}, 'b': {'c': 1, 'd': 1}, 'c': {'b': 1, 'd': 1, 'e': 1}, 'd': {'e': 1, 'h': 1}, 'e': {'d': 1}, 'h': {}}
# graph = {'a': {'b': 1, 'c': 1}, 'b': {'c': 1, 'd': 1}, 'c': {'b': 1, 'd': 1, 'e': 1}, 'd': {'e': 1, 'h': 1}, 'e': {'d': 1}, 'h': {}}

def dijkstra(my_graph, start, goal):
    shortest_distance = {}  # contains shortest distance from 'start' to every other node in graph
    predecessor = {}  # finds the shortest path. This gets continually
    # updated with where the path to the current node came from.
    unseen_nodes = my_graph  # holds all unvisited nodes.
    infinity = 9999999999  # set shortest distance to this value
    path = []  # shown at the end
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0
    # {'a': 0, 'b': 9999999999, 'c': 9999999999, 'd': 9999999999, 'e': 9999999999}

    while unseen_nodes:

        # Finds which node we have to go to after visiting a vertex
        min_node = None  # Must choose node that has lowest distance of all unvisited neighbor nodes.
        # This makes the algorithm greedy
        print(unseen_nodes)
        print(shortest_distance)
        for node in unseen_nodes:
            print(node, " ", min_node)
            if min_node is None:
                min_node = node
            print(shortest_distance[node], " ", shortest_distance[min_node])
            if shortest_distance[node] < shortest_distance[min_node]:
                # elif shortest_distance[node] <= shortest_distance[min_node]:
                min_node = node
            print("")

        #  Main part of the algorithm
        for childNode, weight in my_graph[min_node].items():
            print(childNode, " This is child node")
            print(shortest_distance[min_node], " ", shortest_distance[childNode])
            if weight + shortest_distance[min_node] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[min_node]
                predecessor[childNode] = min_node
        unseen_nodes.pop(min_node)

    currentNode = goal
    while currentNode != start:
        try:  # just in case a node does not reach every node.
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break

    path.insert(0, start)
    if shortest_distance[goal] != infinity:  # if a shortest distance to a node is infinity, it wasn't reached
        print('Shortest distance is ' + str(shortest_distance[goal]))
        print('The path is ' + str(path))


dijkstra(graph, 'a', 'd')
