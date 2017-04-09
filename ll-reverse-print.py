"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    """Prints out a linked list in reverse.
    Idea: walk through list, adding each node's data to a new list.
    Reverse-print elements in the list.
    """

    ll_data = []  # empty list to store node data values

    current = head
    while current:
        ll_data.append(current.data)
        current = current.next

    for data in ll_data[::-1]:
        print data


  