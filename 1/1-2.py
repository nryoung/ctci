"""
Q: Implement a function void reverse(char* str) in C or C++ which reverses a
null terminated string.

NOTE: While this question is specific to C/C++ it can be accomplished serveral
ways in Python.
"""


def reverse_list_slicing(s):
    """
    Uses list slicing to reverse the string.
    """
    return s[::-1]


def reverse_builtin(s):
    """
    Uses the builtin `reversed` method to reverse s
    """
    return ''.join(reversed(s))

if __name__ == '__main__':
    s = 'The string that should be reversed'

    print(reverse_list_slicing(s))
    print(reverse_builtin(s))
