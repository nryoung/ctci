"""
Q: Given two strings, write a method to decide if one is a permutaion of the
other.
"""


def permutation_set(a, b):
    """
    A naive implementation that I came up with utilizing a set. This has worst
    case running time of O(n ** 2).
    """

    if len(a) != len(b):
        return False

    chars = set()

    for c in a:
        chars.add(c)

    for c in b:
        if c in chars:
            continue
        else:
            return False

    return True

if __name__ == '__main__':
    a = 'aaabbbccc'
    b = 'babacabcc'
    print("'{}' is a permutation of '{}': {}".format(b, a, permutation_set(a, b)))
