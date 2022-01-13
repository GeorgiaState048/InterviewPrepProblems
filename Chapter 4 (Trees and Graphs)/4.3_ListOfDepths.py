from collections import deque

"""queue = deque()
queue.append((2, 0))
print(queue)
node, level = queue.popleft()
print(node)
print(level)"""


class BinaryNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def ListOfDepths(root):
    queue = deque()
    queue.append((root, 0))
    levels = {}

    while queue:
        currNode, level = queue.popleft()
        if level not in levels:
            levels[level] = []
        else:
            levels[level].append(currNode)
        if currNode.left:
            queue.append((currNode.left, level + 1))
        if currNode.right:
            queue.append((currNode.right, level + 1))
    return levels


def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = ListOfDepths(root)
    print(levels)


example()
