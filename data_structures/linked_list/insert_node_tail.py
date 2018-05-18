"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    new_node = Node(data=data, next_node=None)
    if head is None:
        head = new_node
    elif head.next is None:
        head.next = new_node
    else:
        Insert(head.next, data)
    return head
