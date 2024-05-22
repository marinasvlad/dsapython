class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        if self.length == 0:
            return result
        else:
            temp = self.head
            for _ in range(self.length - 1):
                result += str(temp.value) + '<->'
                temp = temp.next
            result += str(self.tail.value)
            return result
                
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def traverse(self):
        if self.length == 0:
            print("The list is empty")
        else:
            temp = self.head
            for _ in range(self.length):
                print(temp.value, end = " ")
                temp = temp.next

    def reverse_traverse(self):
        if self.length == 0:
            print("The list is empty")
        else:
            temp = self.tail
            for _ in range(self.length):
                print(temp.value, end = " ")
                temp = temp.prev
             
    def search(self,value):
        if self.length == 0:
            return False
        else:
            temp = self.head
            while temp is not None:
                if temp.value == value:
                    return True
                temp = temp.next
            return False 
        
    def get(self, index):
        if index < 0 or index > self.length:
            print('Index out of range')
            return None
        else:
            if self.length == 0:
                return None
            else:
                if(index < self.length // 2):
                    temp = self.head
                    for _ in range(index):
                        temp = temp.next
                    return temp
                else:
                    temp = self.tail
                    for _ in range(self.length - 1, index, -1):
                        temp = temp.prev
                    return temp
                
    def set(self, value, index):
        if self.head is None:
            print("The list is empty")
            return None
        else:
            node = self.get(index)
            node.value = value
            return node
    
    def insert(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print('Index out of range')
            return new_node
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.length:
                self.prepend(value)
            else:
                prev_node = self.get(index - 1)
                new_node.next = prev_node.next
                new_node.prev = prev_node
                prev_node.next.prev = new_node
                prev_node.next = new_node
                self.length += 1
    
    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            popped_node = self.head
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
            popped_node.next = None
            self.length -= 1
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            popped_node = self.tail
            prev_node = popped_node.prev
            prev_node.next = None
            self.tail = prev_node
            popped_node.prev = None
            self.length -= 1


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
print(dll)
dll.prepend(200)
dll.prepend(500)
print(dll)
dll.traverse()
print()
dll.reverse_traverse()
print()
print(dll.search(75))
print(dll.search(40))
print(dll.get(dll.length).value)
dll.set(250, 5)
print(dll)
dll.insert(205,2)
print(dll)
dll.pop_first()
print(dll)
dll.pop()
print(dll)
