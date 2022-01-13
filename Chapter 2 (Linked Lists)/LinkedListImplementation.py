class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def returnKthToLast(head, k):
    if not head:
        return 0

    index = returnKthToLast(head.next, k) + 1

    if index == k:
        print(head.val)
    return index


top = Node(0)
top.next = Node(1)
top.next.next = Node(2)
top.next.next.next = Node(3)
top.next.next.next.next = Node(4)
top.next.next.next.next.next = Node(5)

returnKthToLast(top, 2)
