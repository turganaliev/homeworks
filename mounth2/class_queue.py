from collections import deque

class Gueue():

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def pop(self):
        q = deque()
        q.append(self.a)
        q.append(self.b)
        q.append(self.c)
        print("Initial queue")
        print(q)
        print("\nElements dequeued from the queue")
        print(q.popleft())
        print(q.popleft())
        print(q.popleft())
        print("\nQueue after removing elements")
        print(q)

a = Gueue('a', 'b', 'c')
a.pop()