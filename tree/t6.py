from ..queue.q4 import Queue as queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

new_t = TreeNode("Drinks")
left_child = TreeNode("Hot")
right_child = TreeNode("Cold")
new_t.right_child = right_child
new_t.left_child = left_child

def preorder_transversal(root_node):
    if not root_node:
        return
    print(root_node.data)
    preorder_transversal(root_node.left_child)
    preorder_transversal(root_node.right_child)

def inorder_traversal(root_node):
    if not root_node:
        return
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)

def postorder_traversal(root_node):
    if not root_node:
        return
    postorder_traversal(root_node.left_child)
    postorder_traversal(root_node.right_child)
    print(root_node.data)

def lever_order_traversal(root_node):
    if not root_node:
        return
    else:
        custom_queue = queue()
        custom_queue.enqueue(root_node)
        while not(custom_queue.is_empty()):
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)

preorder_transversal(new_t)
print()
inorder_traversal(new_t)
print()
postorder_traversal(new_t)
lever_order_traversal(new_t)