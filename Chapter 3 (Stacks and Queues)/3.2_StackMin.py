class Stack:
    def __init__(self):
        self.stack = []
        self.minVal = None
        self.mins = []

    def add(self, num):
        if self.minVal is None:
            self.minVal = num
            self.stack.append(num)
            self.mins.append(num)
        elif num < self.minVal:
            self.minVal = num
            self.stack.append(num)
            self.mins.append(num)
        else:
            self.stack.append(num)

    def pop(self):
        if self.stack[-1] == self.minVal:
            self.mins.pop()
            self.minVal = self.mins[-1]
            self.stack.pop()
        else:
            self.stack.pop()

    def minValue(self):
        return self.minVal


n = Stack()
n.add(5)
n.add(22)
n.add(4)
n.add(3)
print(n.stack)
print(n.minVal)
n.pop()
print(n.stack)
print(n.minVal)