class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        current = self.head
        for _ in range(self.length - 1):
            result += str(current.value) + '<->'
            current = current.next
        result += str(current.value)
        return result 

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        for _ in range(self.length):
            print(current.value, end = ' ')
            current = current.next
    
    def reverse_traverse(self):
        current = self.tail
        for _ in range(self.length):
            print(current.value, end = ' ')
            current = current.prev
cdll = CircularDoublyLinkedList()
cdll.append(100)
cdll.append(200)
cdll.append(300)
print(cdll)
cdll.prepend(40)
cdll.prepend(50)
cdll.prepend(60)
print(cdll)
print()
cdll.traverse()
print()
cdll.reverse_traverse()