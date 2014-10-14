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
    XXX: WORK IN PROGRESS
    """
    char_array = [c for c in s]

    space_count = 0
    for i in range(0, len(char_array)):
        if i == ' ':
            space_count += 1
    new_len = (len(char_array)-1) + space_count * 2

    for i in range(len(char_array)-1, 0, -1):
        if char_array[i] == ' ':
            char_array[new_len - 1] = '0'
            char_array[new_len - 2] = '2'
            char_array[new_len - 3] = '%'
            new_len -= 3
        else:
            char_array[new_len - 1] = char_array[i]
            new_len -= 1

    return "".join(char_array)

if __name__ == '__main__':
    s = "Mr John Smith    "
    print("Url endcoded version of {}: {}".format(s, url_encoding(s)))
