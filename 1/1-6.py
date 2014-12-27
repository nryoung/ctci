"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in
place?
"""


def rotate(matrix, n):
    for layer in range(0, n/2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last-offset][first]

            # bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            # right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return matrix

if __name__ == '__main__':
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print rotate(m, 3)
