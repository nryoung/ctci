"""
Implements a simple linked list
"""


class Node(object):
    """
    Node element, stores data and "pointer" to next Node. Pointer is used
    loosely here as Python doesn't have a real concept of a pointer.
    """
    def __init__(self, value, n):
        self.value = value
        self.next = n
