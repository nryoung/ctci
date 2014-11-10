/**
 * Implement a function to check if a binary tree is balanced. For the purposes
 * of of this question, a balanced tree is defined to be a tree such that
 * heights of the two subtrees of any node never differ by more than one.
 */

/* ANSWER:
 * This code recurse's on each subtree of root. As it recurse's it checks along
 * the way that each each subtree is balanced. If one subtree is not balanced
 * it will immediately return -1. If it is balanced it will return the height
 * of the tree.
 *
 * This runs in O(N) time and uses O(H) space, where H is the height of the
 * tree.
 */
public static int checkHeight(TreeNode root) {
    if ( root == null) {
        return 0; // Height of 0
    }

    /* Check if left is balanced */
    int leftHeight = checkHeight(root.left);
    if (leftHeight == -1) {
        return -1; // Not balanced
    }

    /* Check if right is balanced */
    int rightHeight = checkHeight(root.right);
    if (rightHeight == -1) {
        return -1; // Not balanced
    }

    /* Check if current node is balanced. */
    int heightDiff = leftHeight - rightHeight;
    if (Math.abs(heightDiff) > 1) {
        return -1; // Not balanced
    } else {
        /* Return height */
        return Math.max(leftHeight, rightHeight) + 1;
    }

}

public static boolean isBalanced(TreeNode root) {
    if (checkHeight(root) == -1) {
        return false;
    } else {
        return true;
    }
}

