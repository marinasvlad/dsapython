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