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

csLinkedList = CSLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.append(30)
print(csLinkedList)
