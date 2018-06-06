"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def levelOrder(root):
    q = []
    q.append(root)
    while q is not None:
        node = q.pop(0)
        print node.data,
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
