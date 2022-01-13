from collections import defaultdict

test = [
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'E'],
    ['B', 'A'],
    ['B', 'C'],
    ['C', 'A'],
    ['C', 'B'],
    ['C', 'D'],
    ['C', 'E'],
    ['D', 'C'],
    ['E', 'A'],
    ['E', 'C'],
]
a = [8, 2, 4, 6]
segments = []
mins = []
x = 2
for i in range(len(a) - x + 1):
    segments.append(a[i:i+x])
print(segments)
for j in range(len(segments)):
    mins.append(min(segments[j]))
print(max(mins))
graph = defaultdict(list)
"""for node in test:
    graph[node[0]].append(node[1])
print(graph)"""

