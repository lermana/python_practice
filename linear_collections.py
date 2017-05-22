class LinearCollection:

    def __init__(self):
        self.items = []

    def __str__(self):
        return ", ".join((item for item in self.items))
    
    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Stack(LinearCollection):

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]


class Queue(LinearCollection):

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


class Deque(LinearCollection):

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        self.items.pop(0)

    def remove_rear(self):
        self.items.pop()








