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


class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        current = self.head
        rep = ''
        while current is not None:
            if current.next is None:
                rep += '({}, {})'.format(current.value, None)
            else:
                rep += '({}, {})->'.format(current.value, current.next.value)
            current = current.next
        return rep

    def insert_front(self, value):
        if self.tail is None and self.head is None:
            # This is the first Node
            self.head = self.tail = Node(value, None)
        else:
            self.head = Node(value, self.head)

    def insert_back(self, value):
        if self.empty():
            self.insert_front(value)
        self.tail.next = self.tail = Node(value, None)

    def insert_after(self, existing, value):
        existing_node = self.find(existing)
        if not existing_node:
            raise NoSuchNodeError
        existing_node.next = Node(value, existing_node.next)

    def delete(self, value):
        node = self.head
        previous = None
        while node is not None and node.value != value:
            previous = node
            node = node.next
        if not node:
            raise NoSuchNodeError
        elif node == self.tail:
            self.tail = previous
        elif node == self.head:
            self.head = node.next
        else:
            previous.next = node.next

    def find(self, value):
        current = self.head
        while current is not None and current.value != value:
            current = current.next
        if not current:
            return NoSuchNodeError
        else:
            return current

    def empty(self):
        return self.head is None


class NoSuchNodeError(Exception):
    pass


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_front(11)
    linked_list.insert_front(300)
    linked_list.insert_front(72)
    print(linked_list)
