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
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        
        self.length += 1

    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node        
        self.length += 1

    def transverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node)
            current_node = current_node.next

    def reverse(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node)
            current_node = current_node.prev

    def search(self, target):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            currnet_node = self.head
            for _ in range(index):
                currnet_node = currnet_node.next
        else:
            currnet_node = self.tail
            for _ in range(self.length - 1, index, -1):
                currnet_node = currnet_node.prev
        
        return currnet_node

    def set(self, index, value):
        set_node = self.get(index)
        if set_node:
            set_node.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print("Index out of bounds")
            return
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            node = self.get(index - 1)
            new_node.next = node.next
            new_node.prev = node
            node.next.prev = new_node
            node.next = new_node

        self.length += 1

    def pop_first(self):
        popped_node = self.head

        if not self.head:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1

        return popped_node

    def pop(self):
        popped_node = self.tail

        if not self.tail:
            return None
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1

    def remove(self, index):
        if index <= 0 or index >= self.length:
            print("Index out of bounds")
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        if removed_node:
            removed_node = self.get(index)
            removed_node.prev.next = removed_node.next
            removed_node.next.prev = removed_node.prev
            removed_node.next = None
            removed_node.prev = None
            self.length -= 1
            return removed_node



dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)
print(dll)
dll.prepend(50)
dll.prepend(60)
print(dll)
print()
dll.transverse()
print()
dll.reverse()

print(dll.search(30))
print()
print(dll.get(0))
print(dll.get(1))
print(dll.get(2))
print(dll.get(3))
print(dll.get(4))
print()
dll.set(2, 15)
print(dll)
dll.insert(2,25)
print(dll)
dll.insert(dll.length,35)
dll.insert(0,45)
print(dll)
dll.pop_first()
print(dll)

