class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

class Linked_List:
    def __init__(self, head):
        self.head = Node(head)
        self.next = Node

    def add(self, data):
        self.head.next = Node(data)

# Head
l = Linked_List(1)
print(l.head.data)

# Add box or node
l.add(2)
print(l.head.next.data)
l.add(4)
print(l.head.next.data)
l.add(10)
print(l.head.next.data)
