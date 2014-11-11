/**
 * Given a sorted (increasing order) array with unique integer elements, write
 * an algorithm to create a binary search tree with minimal height.
 */

/**
 * ANSWER:
 * The values in a sorted array should not be inserted as is. This will cause
 * the BST to be nowhere near minimal height. The optimal solution is to have
 * the middle of the array be the root. Then the left half of the array (the
 * smaller half) be the left subtree and the right half of the arrya (the
 * larger half) be the right subtree. This can be achieved very simply with
 * recursion
 */

TreeNode crateMinimalBST(int arr[], int start, int end) {
    if (end < start) {
        return null;
    }

    int mid = (start + end) / 2;
    TreeNode n = new TreeNode(arr[mid]);
    n.left = createMinimalBST(arr, start, mid - 1);
    n.right = createMinimalBST(arr, mid + 1, end);
    return n;
}

TreeNode createMinimalBST(int array[]) {
    return createMinimalBST(array, 0, array.length - 1);
}
