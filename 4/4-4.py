"""
Given a binary tree, design an algorithm which creates a linked list of all teh
nodes at each depth (e.g., if you have a tree with depth D, you'll have D
linked lists).

ANSWER:
Suprisingly you can use DFS to solve this one. Slight modifications of the
algorithm are needed to account for what level it is on.
"""

def create_level_linked_list(root, lists, level):

    if root == None: # Base case
        return


    # True if this is the first time we have visited this level, so create a
    # new linked list and add it to then end of our lists
    if len(lists) == level:
        linked_list = LinkedList()
        lists.append(list)

    # Otherwise we already have a linked_list for this level and we just grab
    # it from list
    else:
        linked_list = lists[level]

    # Actually add the node to our linked list
    linked_list.add(root)

    # Recurse!
    create_level_linked_list(root.left, lists, level + 1)
    create_level_linked_list(root.right, lists, level + 1)


def start_level_linked_lists(root):
    # Small starter function to kick everything off
    lists = []
    create_level_linked_list(root, lists, 0)
    return lists
