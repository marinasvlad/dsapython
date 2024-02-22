class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head

        result = ''

        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
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

    def prepend(self,value):
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

    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            raise Exception("Index out of range")

        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                self.tail.next = new_node

            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node

        elif index == self.length:
            self.tail.next = new_node
            new_node.next=self.head
            self.tail = new_node

        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def transverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
        


cs_ll  = CSLinkedList()

cs_ll.append(10)
cs_ll.append(20)
cs_ll.append(30)

print(cs_ll)

cs_ll.prepend(40)
cs_ll.prepend(50)


print(cs_ll)

cs_ll.insert(3,15)

print(cs_ll)

cs_ll.insert(1,1)

print(cs_ll)

cs_ll.insert(0,25)
print(cs_ll)

cs_ll.transverse()