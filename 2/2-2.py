"""
Q: Implement an algorithm to find the kth to the last element of a singly
linked list.

NOTE: I was confused by the wording of this question. To me it makes more sense
if it were to read: 'Return the kth from the last element'.
"""
from linked_list import LinkedList


def find_k_from_last(head, k, i, buf):
    """
    Uses recursion to find the tail of the linked list. Along the way all of
    the values are put in to a buffer. Once the tail is found we take length of
    linked_list - k from the buffer and that will be our value. That is floated
    up through the call stack. Think of the buffer as a circular buffer
    (sorta).

    The advantage of using recursion is that it is extremely easy to implement.
    The disadvantage is that this will eat up O(n) space and O(n) time. If we
    had a real the circular buffer then the space would be O(k).
    """
    if not head:
        return buf[i-k]
    buf.append(head.value)

    value = find_k_from_last(head.next, k, i+1, buf)
    return value

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
        k, find_k_from_last(linked_list.head, k, 0, []))
    )
