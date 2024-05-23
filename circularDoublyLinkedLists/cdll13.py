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
        return new_node

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
        return new_node

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

    def search(self, value):
        if self.head is None:
            return False
        else:
            current = self.head
            for _ in range(self.length):
                if current.value == value:
                    return True
                current = current.next
            return False
        
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        return current
    
    def set(self, value, index):
        if index < 0 or index >= self.length:
            return None
        node = self.get(index)
        node.value = value
        return node
    
    def insert(self, value, index):
        if index < 0 or index > self.length:
            return None
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            if index == 0:
                return self.prepend(value)
            if index == self.length:
                return self.append(value)
            
            new_node = Node(value)
            prev_node = self.get(index - 1)
            new_node.prev = prev_node
            new_node.next = prev_node.next
            prev_node.next.prev = new_node
            prev_node.next = new_node
            self.length += 1
            return new_node

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:        
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        removed_node = self.get(index)
        
        removed_node.prev.next = removed_node.next
        removed_node.next.prev = removed_node.prev
        removed_node.next = None
        removed_node.prev = None
        self.length -= 1
        return removed_node

    
        
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
print()
print(cdll.search(100))
print(cdll.search(150))
print()
print()
print(cdll.get(0).value, end = ' ')
print(cdll.get(1).value, end = ' ')
print(cdll.get(5).value, end = ' ')
print()
cdll.set(65, 0)
cdll.set(55, 1)
print(cdll)
cdll.insert(97, 3)
print(cdll)
cdll.remove(2)
print(cdll)

