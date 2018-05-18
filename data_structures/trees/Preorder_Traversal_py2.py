"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def print_node(root):
    print root.data,
    if root.left is not None:
        print_node(root.left)
    if root.right is not None:
        print_node(root.right)
        
def preOrder(root):
    if root.data is not None:
        print_node(root)
    else:
        print('NULL')