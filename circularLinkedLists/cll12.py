class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        temp = self.head
        if self.length == 0:
            return result
        else:
            for _ in range(self.length - 1):
                result += str(temp.value) + ' -> '
                temp = temp.next
            result += str(temp.value)
            return result 

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        
    def insert(self, value, index):
        new_node = Node(value)
        if index < 0 or index > self.length:
            print('Index out of range')
            return None
        elif index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = self.head
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1
        return new_node


    def traverse(self):
        if self.length == 0:
            print("The list is empty")
        else:
            temp = self.head
            for _ in range(self.length):
               print(temp.value, end = " ")
               temp = temp.next
    
    def search(self, value):
        if self.head is None:
            return -1
        else:
            temp = self.head
            for index in range(self.length):
                if temp.value == value:
                    return index
                temp = temp.next
    
    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp
                
    def set(self, value, index):
        if index < 0 or index > self.length:
            return False
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = value
            return True

    def pop_first(self):
        popped_node = self.head
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
        
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            pre_tail = self.get(self.length - 2)
            self.tail = pre_tail
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            if index == 0:
                if self.length == 1:
                    self.head = None
                    self.tail = None
                    self.length = 0
                else:
                    removed_node = self.head
                    self.head = self.head.next
                    self.tail.next = self.head
                    removed_node.next = None
                    self.length -= 1
                    return removed_node
            if index == self.length:
                self.pop()
            else:
                pre_removed = self.get(index - 1)
                removed_node = pre_removed.next
                pre_removed.next = removed_node.next
                removed_node.next = None
                self.length -= 1
                return removed_node
            

    def delete_all(self):
        self.head = None
        self.tail.next = None
        self.tail = None
        self.length = 0

csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.append(30)
print(csLinkedList)
csLinkedList.prepend(1)
csLinkedList.prepend(2)
csLinkedList.prepend(3)
print(csLinkedList)
csLinkedList.insert(100, 3)
print(csLinkedList)
csLinkedList.traverse()
print()
print(csLinkedList.search(3))
print(csLinkedList.get(3).value)
print(csLinkedList)
csLinkedList.pop_first()
print(csLinkedList)
csLinkedList.pop()
print(csLinkedList)
csLinkedList.remove(4)
print(csLinkedList)