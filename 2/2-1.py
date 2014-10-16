"""
Write code to remove duplicates from an unsorted linked list.

FOLLOW UP

How would you solve this problem if a temporary buffer is not allowed?
"""
from linked_list import LinkedList


def deduplicate_with_hash(node):
    """
    Makes use of temporary "hash table" (dictionary) to keep track of all the
    values seen so far. Worst case running time of O(n)
    """
    tracker = {}
    previous = None
    while node is not None:
        if node.value in tracker.keys():
            previous.next = node.next
        else:
            tracker[node.value] = True
            previous = node
        node = node.next

def deduplicate_without_hash(head):
    """
    Removes nodes with duplicate values. Uses two "pointers" to keep track of
    current location. Wrost case running time of O(n**2).
    """
    if head is None:
        return

    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_front(11)
    linked_list.insert_front(300)
    linked_list.insert_front(72)
    linked_list.insert_front(72)

    print("{}".format(linked_list))
    deduplicate_with_hash(linked_list.head)
    print("{}".format(linked_list))

    linked_list = LinkedList()
    linked_list.insert_front(72)
    linked_list.insert_front(300)
    linked_list.insert_front(72)
    linked_list.insert_front(11)

    print("{}".format(linked_list))
    deduplicate_without_hash(linked_list.head)
    print("{}".format(linked_list))
