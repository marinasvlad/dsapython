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



preorder_transversal(new_t)
print()
inorder_traversal(new_t)
print()
postorder_traversal(new_t)