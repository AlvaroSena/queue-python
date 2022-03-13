class Queue:
    def __init__(self, elements):
        self.elements = elements

    def enqueue(self, elem): 
        item = self.elements.append(elem)
        return item

    def dequeue(self):
        elem = self.elements.pop(0)
        return elem

elements = []
queue = Queue(elements)

queue.enqueue(1)
queue.enqueue(4)
queue.enqueue(112)
queue.dequeue()
print(queue.elements)