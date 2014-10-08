"""
Q: Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?


NOTE: The book assumes that the input is going to be a lower case string of
letters.
"""

"""
The easiest and most readable solution is to use a data strucuture like a set
to keep track of the letters that have you have already seen. This also allows
the code to be more general allowing to check for uniqueness for any sort of
strings not just lower case letters
"""
def is_unique_readable(s):
    """
    Iterates over input string 's' adding each char to a set. Returns False if
    the char has been before, otherwise True if all chars in the string are
    unique.
    """
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True


"""
To satisfy the 'cannot use additional data structures' requirement the author
uses quite a clever little hack. The author initializes an 'int' in Java which
she assumes will be given 32 bits, which will coincendtally all be initialized
to zero. This gives us a bit vector that we can use to see if a lowercase
letter has been seen before. If this is the first time we see a letter we set
the corresponding location in the bit vector to 1. If this is not the first
time we have seen a letter, then the bit will already be set to 1 and the
function can return False.

NOTE: I would never write code like this in production unless I absolutely had
to. If I had to, then I would ensure that there was a lot of documentation
explaining the logic behind the decision.
"""
def is_unique_clever(s):
    """
    Iterates over string 's' setting entries in a bit vector using bitwise
    operations. Returns False if the char has been seen before, otherwise True
    if all chars in the string are unique.
    """
    if len(s) > 26:
        return False

    checker = 0
    for char in s:
        val = ord(char) - ord('a')

        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)

    return True

if __name__ == '__main__':
    print("'abcdef' is unique: {}".format(is_unique_readable('abcdef')))
    print("'aabcd' is not unique: {}".format(is_unique_readable('aabcd')))

    print("'abcdef' is unique: {}".format(is_unique_clever('abcdef')))
    print("'aabcd' is not unique: {}".format(is_unique_clever('aabcd')))
