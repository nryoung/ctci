"""
Another good interview question

Please write a function that, given 2 arrays sorted in increasing numeric
order, will return a 3rd array that is also sorted and contains all of the
elements from the input. Please do not use any built-in language sorting
functions. Note that ther is a way to leverage the fact that the arrays are
sorted to do this in O(N) time; There's no need to try and rewrite quicksort.

Example:
x = [-3, 1, 2, 7]
y = [-2, 8, 9, 10, 12]
merge_arrays(x, y) = [-3, -2, 1, 2, 7, 8, 9, 10, 12]
"""


def merge_lists(x, y):
    i = j = 0
    merged = []

    # Maintain two indices for each list. Only imcrement when a value is used
    # from that particular list.
    while i < len(x) and j < len(y):
        smaller = min(x[i], y[j])
        merged.append(smaller)

        # figure out which list it came from
        if smaller == x[i]:
            i += 1
        else:
            j += 1
    # Fallen out of the while loop figure out which list was exhausted and
    # merge the remaining list
    if i == len(x):
        merged.extend(y[j:])
    else:
        merged.extend(x[i:])

    return merged


if __name__ == '__main__':
    x = [-3, 1, 2, 7]
    y = [-1, 8, 9, 10, 12]
    merged = merge_lists(x, y)
    print("Lists before merge, x = {}, y = {}".format(x, y))
    print("Merged list: {}".format(merged))
