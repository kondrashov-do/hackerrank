"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""
def print_node(node):
    print(node.data)
    if node.next is not None:
        print_node(node.next)
        
def print_list(head):
    if head is not None:
        print_node(head)
    else:
        print('NULL')
    