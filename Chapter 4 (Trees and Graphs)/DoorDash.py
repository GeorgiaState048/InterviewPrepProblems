from collections import defaultdict

friends_from = [1, 2, 2, 3, 4, 5]
friends_to = [2, 4, 5, 5, 5, 6]

graph = defaultdict(list)
for i in range(len(friends_from)):
    graph[friends_from[i]].append(friends_to[i])
    graph[friends_to[i]].append(friends_from[i])
# print(graph)

l = [[1, 2, 3], [5, 4, 2], [2, 1, 3], [2, 4, 5]]
j = set(tuple(sorted(i)) for i in l)
print(j)
