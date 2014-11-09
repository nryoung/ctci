"""
Question I got asked in a phone interview:

Given a list of intervals like:
l = [(5, 7), (11, 116), (3, 6), (10, 12), (6, 12)]

Write a function that will merge overlapping intervals.
"""


def merge_intervals(intervals):
    """
    A simple algorithm can be used:
    1. Sort the intervals in increasing order
    2. Push the first interval on the stack
    3. Iterate through intervals and for each one compare current interval
       with the top of the stack and:
        A. If current interval does not overlap, push on to stack
        B. If current interval does overlap, merge both intervals in to one
           and push on to stack
    4. At the end return stack
    """
    sorted_by_lower_bound = sorted(intervals, key=lambda tup: tup[0])
    merged = []

    for higher in sorted_by_lower_bound:
        if not merged:
            merged.append(higher)
        else:
            lower = merged[-1]
            if higher[0] <= lower[1]:
                upper_bound = max(lower[1], higher[1])
                merged[-1] = (lower[0], upper_bound)
            else:
                merged.append(higher)
    return merged

if __name__ == '__main__':

    overlapping_intervals = [(5, 7), (11, 116), (3, 4), (10, 12), (6, 12)]
    print("Original list of intervals: {}".format(overlapping_intervals))
    merged_list = merge_intervals(overlapping_intervals)
    print("List of intervals after merge_intervals: {}".format(merged_list))
