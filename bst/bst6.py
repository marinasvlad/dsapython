from q4 import Queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_node(root, node_value):
    if root.data == None:
        root.data = node_value
    elif node_value <= root.data:
        if root.left is None:
            root.left = BSTNode(node_value)
        else:
            insert_node(root.left, node_value)
    else:
        if root.right is None:
            root.right = BSTNode(node_value)
        else:
            insert_node(root.right, node_value)
    
    return "Node has been inserted"

def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end = " ")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def level_order(root):
    if not root:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left is not None:
                custom_queue.enqueue(root.value.left)
            if root.value.right is not None:
                custom_queue.enqueue(root.value.right)


def search(root, value):
    if root is None:
        print("Element not found")
    elif value < root.data:
        search(root.left, value)
    elif value > root.data:
        search(root.right, value)
    elif value == root.data:
        print("Element found")

new_bst = BSTNode(None)

insert_node(new_bst, 70)
insert_node(new_bst, 50)
insert_node(new_bst, 90)
insert_node(new_bst, 30)
insert_node(new_bst, 60)
insert_node(new_bst, 80)
insert_node(new_bst, 100)
insert_node(new_bst, 20)
insert_node(new_bst, 40)
postorder(new_bst)
print()
level_order(new_bst)
print()
search(new_bst, 20)