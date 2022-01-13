from collections import deque
stack = deque()
queue = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

arr = []
rows = 5
col = 6
for i in range(rows):
    arr.append([])
    for j in range(col):
        arr[i].append(0)
arr[3][4] = 2
print(arr[3][4])
print(arr)