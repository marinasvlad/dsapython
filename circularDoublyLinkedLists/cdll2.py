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
        
    def inser_cdll(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            new_node  = Node(value)
            if location == 0:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.head = new_node
                self.tail.next = new_node
            elif location == 1:
                new_node.next = self.head
                new_node.prev = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node
            
            return "The node has been successfully inserted"
        
cdll = CircularDoublyLinkedList()
cdll.create_cdll(5)

cdll.inser_cdll(0,0)
cdll.inser_cdll(1,1)
cdll.inser_cdll(2,2)

print([node.value for node in cdll])