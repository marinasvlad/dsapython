from q3 import Queue as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            newNode = BSTNode(nodeValue)
            rootNode.leftChild = newNode
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            newNode = BSTNode(nodeValue)
            rootNode.rightChild = newNode
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "The node has been successfuly inserted"

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)   

def leverOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def search(rootNode, value):
    if rootNode is None:
        return "Node not found"
    
    if rootNode.data == value:
        return "The node was found"
    elif value > rootNode.data:
        return search(rootNode.rightChild, value)
    else:
        return search(rootNode.leftChild, value)
    
def minValue(bstNode):
    current = bstNode
    while(current.leftChild is not None):
        current = current.leftChild
    return current


    
def deleteNode(rootNode, value):
    if rootNode is None:
        return rootNode
    
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        temp = minValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The bst has been successfully deleted"

newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
print()
print(deleteBST(newBST))
leverOrderTraversal(newBST)