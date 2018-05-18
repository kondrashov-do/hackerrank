"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def print_postorder_node(root):
    if root.left is not None:
        print_postorder_node(root.left)
    if root.right is not None:
        print_postorder_node(root.right)
    print root.data,
        
def postOrder(root):
    if root is not None:
        print_postorder_node(root)
    else:
        print 'NULL'