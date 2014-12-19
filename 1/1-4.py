"""
Write a method to replace all spaces in a string with '%20'; You may assume
that the string has sufficent space at the end of the string to hold the
additional characters, and that you are given the 'true' length of the string.
(Note: if you implementing in Java, please use a character array so that you
can perform the operation in place.)

Example

Input:  "Mr John Smith    "
Output: "Mr%20John%20Smith"

NOTE: The point of this exercise is to manipulate a char array without
allocating more memory. In that regard, I will only allocate more memory at
the end when I return the finished string.
"""


def url_encoding(s):
    """
    Solution from the book converted in to Python. I tried my best to use
    python idioms but keep true to the nature of the solution.
    """
    chars = [c for c in s]
    length = len(chars)

    space_count = 0
    for i in range(0, length):
        if chars[i] == ' ':
            space_count += 1
    space_count = space_count * 2

    new_len = (length + space_count)
    chars.extend([' '] * space_count)

    for i in range(length-1, 0, -1):
        if chars[i] == ' ':
            chars[new_len - 1] = '0'
            chars[new_len - 2] = '2'
            chars[new_len - 3] = '%'
            new_len -= 3
        else:
            chars[new_len - 1] = chars[i]
            new_len -= 1

    return "".join(chars)


def url_encoding_easy(s):
    """
    Using Python's builtin string replace is by far the easiest way to
    accomplish this.
    """
    return s.replace(' ', '%20')


if __name__ == '__main__':
    s = "Mr John Smith"
    print("Url endcoded version of {}: {}".format(s, url_encoding(s)))
    print("Url endcoded version of {}: {}".format(s, url_encoding_easy(s)))
