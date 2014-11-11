/**
 * Implementation of DFS on BST
 */

BinaryTreenode search(BinaryTreenode root, Comparable key) {
    // Empty tree
    if (root == null) return;

    // Root is the node we are looking for
    if (key == root.getKey()) return root;

    if ( if key.compareTo(root.getKey()) < 0){
        // if key is present it is in left subtree
        return search(root.getLeft(), key);
    } else {
        // if key is present it is in right subtree
        return search(root.getRight(), key);
    }
}
