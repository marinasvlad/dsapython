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
preorder(new_bst)
print()
inorder(new_bst)
print()
postorder(new_bst)