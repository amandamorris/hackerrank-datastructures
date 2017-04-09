"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    new_node = Node(data=data)
    # if position = 0, the new node is the new head
    if position == 0:
        new_node.next = head
        return new_node

    # initialize variables to track index of list and current node
    index = 1  #index of next node
    current = head

    while current.next:
        if index == position:
            new_node.next = current.next
            current.next = new_node
            return head
        current = current.next  # move current forward
        index += 1  # increment index

    # if we get to the last item and haven't inserted/returned yet, insert at
    # the end
    current.next = new_node
    return head



