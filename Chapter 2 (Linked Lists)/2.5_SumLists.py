from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sumLists(headA, headB):
    numA = ""
    numB = ""
    while headA:
        numA += str(headA.val)
        headA = headA.next

    while headB:
        numB += str(headB.val)
        headB = headB.next

    numA = numA[::-1]
    numB = numB[::-1]
    sumNums = str(int(numA) + int(numB))

    output = Node(int(sumNums[0]))
    curr = output
    for i in range(1, len(sumNums)):
        curr.next = Node(int(sumNums[i]))
        curr = curr.next
    outputList = []
    while output:
        outputList.append(output.val)
        output = output.next
    return outputList


listA = Node(7)
listA.next = Node(1)
listA.next.next = Node(6)

listB = Node(5)
listB.next = Node(9)
listB.next.next = Node(2)

#print(sumLists(listA, listB))

q = deque()
q.appendleft(0)
q.appendleft(0)
q.appendleft(0)
print(q)