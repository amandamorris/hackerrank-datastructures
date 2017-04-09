"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def delete(head, position):
    """Deletes the positionth item from a linkedlist, and returns the head"""
    # to delete the head:
    if position == 0:
        new_head = head.next
        head.next = None
        return new_head

    #  to delete a middle node:
    current = head
    index = 1  # initialize index to correspond to current.next
    while current.next:
        if index == position:
            current.next = current.next.next
            return head
        else:  # advance index and current node
            index += 1
            current = current.next