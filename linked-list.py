
class Node:
    def __init__(self, data):
        self.data = data
        self.next = Node

box1 = Node(1)
box2 = Node(10)
box3 = Node(40)
box4 = Node(90)
box5 = Node(200)

box1.next = box2
box2.next = box3
box3.next = box4
box4.next = box5

    

print(box1.data, box2.data, box3.data, box4.data, box5.data)

