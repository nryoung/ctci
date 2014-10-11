"""
Q: Given two strings, write a method to decide if one is a permutaion of the
other.
"""


def permutation_naive(a, b):
    """
    A naive implementation iterating over. This has worst
    case running time of O(n ** 2).
    """

    if len(a) != len(b):
        return False

    chars = [c for c in a]

    for char in b:
        for x in chars:
            if char == x:
                chars.remove(x)
                break

    if chars:
        return False
    return True


def permutation_sorted(a, b):
    """
    Efficient solution that sorts both strings and then compares them. This has
    a worst running tmie of O(n * log(n))
    """
    if len(a) != len(b):
        return False

    for i, j in zip(sorted(a), sorted(b)):
        if i != j:
            return False

    return True

if __name__ == '__main__':
    a = 'aaabbbccc'
    b = 'babacabcc'
    print("'{}' is a permutation of '{}': {}".format(b, a, permutation_naive(a, b)))
    print("'{}' is a permutation of '{}': {}".format(b, a, permutation_sorted(a, b)))

    # Test when not a permutation, off by one char
    c = 'aaaabbbccc'
    d = 'aaabbbbccc'
    print("'{}' is a permutation of '{}': {}".format(c, d, permutation_naive(c, d)))
    print("'{}' is a permutation of '{}': {}".format(c, d, permutation_sorted(c, d)))
