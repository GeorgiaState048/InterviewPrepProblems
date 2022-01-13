from collections import defaultdict


class SetOfStacks:
    def __init__(self, limit):
        self.setStacks = defaultdict(list)
        self.limit = limit

    def push(self, num):
        if len(self.setStacks) == 0:
            self.setStacks[1].append(num)
        elif len(self.setStacks[len(self.setStacks)]) >= self.limit:
            self.setStacks[len(self.setStacks) + 1].append(num)
        else:
            self.setStacks[len(self.setStacks)].append(num)

    def popAtIndex(self, index):
        self.setStacks[index].pop()

    def pop(self):
        if len(self.setStacks[len(self.setStacks)]) > 0:
            self.setStacks[len(self.setStacks)].pop()
        else:
            del self.setStacks[len(self.setStacks)]
            self.setStacks[len(self.setStacks)].pop()


print(num)
n = SetOfStacks(3)
n.push(2)
n.push(3)
n.push(4)
n.push(5)
n.pop()
n.pop()
print(n.setStacks)
