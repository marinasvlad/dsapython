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

    def transversal(self):
        if self.head is None:
            print("The CDLL is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.value)
                current_node = current_node.next
                if current_node == self.head:
                    break

    def reverse_transversal(self):
        if self.tail is None:
            print("The CDLL is empty")
        else:
            current_node = self.tail
            while current_node:
                print(current_node.value)
                current_node = current_node.prev
                if current_node == self.tail:
                    break

        
    def search(self, value):
        if self.head is None:
            return "CDLL is empty"
        else:
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    return current_node.value
                if current_node == self.tail:
                    return "The value does not exist"
                current_node = current_node.next

    def delete_node(self, location):
        if self.head is None:
            print("The CDLL is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            if location == 1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
            
            print("The node has been deleted")
            
cdll = CircularDoublyLinkedList()
cdll.create_cdll(5)

cdll.inser_cdll(0,0)
cdll.inser_cdll(1,1)
cdll.inser_cdll(2,2)

print([node.value for node in cdll])
cdll.transversal()
print()
cdll.reverse_transversal()
print()

print(cdll.search(7))
cdll.inser_cdll(5,2)
cdll.inser_cdll(1,2)
cdll.inser_cdll(7,2)
print([node.value for node in cdll])

cdll.delete_node(0)
cdll.delete_node(1)
# cdll.delete_node(3)

print([node.value for node in cdll])
