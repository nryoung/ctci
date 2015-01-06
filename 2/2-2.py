"""
Q: Implement an algorithm to find the kth to the last element of a singly
linked list.

NOTE: I was confused by the wording of this question. To me it makes more sense
if it were to read: 'Return the kth from the last element'.
"""
from linked_list import LinkedList


def find_k_from_last(head, k, i):
    """
    Uses recursion to find this
    """
    if not head:
        return None

    node = find_k_from_last(head.next, k, i)
    #XXX
    i += 1
    if i == k:
        return head
    return node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_front(11)
    linked_list.insert_front(300)
    linked_list.insert_front(72)
    linked_list.insert_front(99)
    linked_list.insert_front(87)
    linked_list.insert_front(89)
    linked_list.insert_front(29)

    k = 3
    print('Finding k:{} from the last element:{}'.format(
        k, find_k_from_last(linked_list.head, k, 0).value)
    )
