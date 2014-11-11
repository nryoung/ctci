/**
 * Implementation of DFS on BST
 */

void search(BinaryTreenode root) {
    // Empty tree
    if (root == null) return;
    visit(root);
    root.visited = true;

    foreach(Node n in root.adjacent) {
        if (n.visited == false) {
            search(n);
        }
    }
}
