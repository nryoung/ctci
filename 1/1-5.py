"""
Implement a method to perform basic string compression using the counts of
repeated characters. For example, the string aabcccccaa would become a2b1c5a3.
If the compressed string would nto become smaller than the original string,
your method should return the original string.
"""


def compress(s):
    # s must contain something
    if not s:
        return ''

    char_counts = []
    count = 0
    prev_char = s[0]

    for c in s:
        if prev_char == c:
            count += 1
        else:
            char_counts.append((prev_char, count))
            prev_char = c
            count = 1

    # string finished append last bit of data
    char_counts.append((prev_char, count))

    # compress
    compressed = ''.join('%s%s' % tup for tup in char_counts)

    # Check if the compression will be larger than original
    if len(compressed) >= len(s):
        return s
    return compressed

if __name__ == '__main__':
    input_one = 'aabcccccaaa'
    s = compress(input_one)
    print 'Input String: {}, Compressed String: {}'.format(input_one, s)

    input_two = 'abcdefg'
    s = compress(input_two)
    print 'Input String: {}, Compressed String: {}'.format(input_two, s)

    input_three = 'foooooobbbbbaaaaaar'
    s = compress(input_three)
    print 'Input String: {}, Compressed String: {}'.format(input_three, s)
