
de is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def printLeft(root):
    if root is not None:
        printLeft(root.left)
        print root.data,

def printRight(root):
    if root is not None:
        print root.data,
        printRight(root.right)

def topView(root):
    printLeft(root)
    printRight(root.right)
