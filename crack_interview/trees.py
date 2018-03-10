""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    '''
    if root.left and root.right:
        result = root.data is None or (root.data > root.left.data and root.data < root.right.data)
        checkBST(root.left)
        checkBST(root.right)
        return result
    else:
        return True
    '''
    return check(root, 0, 10000)
def check(n, minN, maxN):
	if n == None:
		return True
	if n.data <= minN or n.data >= maxN:
		return False
	return check(n.left, minN, n.data) and check(n.right, n.data, maxN)
