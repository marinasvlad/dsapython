class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

            if node == self.tail.next:
                break

    def create_cdll(self, node_value):
        new_node = Node(node_value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        return "CDLL is created successfully"
        
        
cdll = CircularDoublyLinkedList()
cdll.create_cdll(5)
print([node.value for node in cdll])