"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head is not None:
        currentNode = head
        nodes = set()
        while currentNode.next is not None:
            nodes.add(currentNode)
            if currentNode.next in nodes:
                return True
            else:
                currentNode = currentNode.next
        return False
    else:
        return False