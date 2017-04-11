"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def reverse_ll(head):
    """Reverses a linked list in place, returns the new head"""
    current = head
    prev = None

    while current:
        following = current.next
        current.next = prev
        prev = current
        current = following
    return prev
