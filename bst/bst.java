/**
 * Implementation of a BST
 */

class BinaryTreenode {
    // fields
    private Comparable key;
    private BinaryTreenode left, right;

    // methods

    //constructor
    public BinaryTreenode(Comparable k, BinaryTreenode l, BinaryTreenode r) {
        key = k;
        left = l;
        right = r;
    }

    // access to fields
    public Comparable getKey() {return key;}
    public BinaryTreenode getLeft() {return left;}
    public BinaryTreenode getRight() {return right;}

    //change fields
    public void setKey(Comparable k) {key = k;}
    public void setLeft(BinaryTreenode l) {key = k;}
    public void setRight(BinaryTreenode r) {right = r;}
}

class BST {
    // fields
    private BinaryTreenode root; // ptr to the root of the BSt

    // methods
    public BST() {root=null;} // constructor

    // add key to this BST; error if it already there
    public void insert(Comparable key) throws DuplicateException {
        if (root == null) {
            root = new BinaryTreenode(key, null, null);
        } else {
            insert(root, key);
        }
    }

    private static void insert(BinaryTreenode T, Comparable k) throws DuplicateException {
        // precondition: T != null
        if (T.getKey().equals(k)) throw new DuplicateException();
        if (k.compareTo(T.getKey()) < 0) {
            // add k as left child of T if it doesn't already have one else
            // insert into T's left subtree
            if (T.getLeft() == null) T.setLeft( new BinaryTreenode(k, null, null));
            else insert(T.getLeft(), k);
        } else {
            // here whe k > T's key
            // insert k as right child of T if it doesn't already have on else
            // insert into T's right subtree
            if (T.getRight() == null) T.setRight( new BinaryTreenode(k, null, null));
            else insert(T.getRight(), k);
        }
    }

    // remove the node containing key from this BST if it is there; otherwise,
    // do nothing
    public void delete(Comparable key) {
    root = delete(root, key);
    }

    private static BinaryTreenode delete(BinaryTreenode T, Comparable key) {
        if (T == null) return null;
        if (key.equals(T.getKey())) {
            // T is the node to be removed
            if (T.getLeft() == null && T.getRight() == null) return null;
            if (T.getLeft() == null) return T.getRight();
            if (T.getRight() == null) return T.getLeft();

            // here if T has 2 children
            BinaryTreenode tmp = smallestNode(T.getRight());
            // copy key field from tmp to T
            T.setKey( tmp.getKey() );

            // now delete tmp from T's right subtree and return
            T.setRight( delete(T.getRight(), tmp.getKey()));
            return T;

        } else if (key.compareTo(T.getKey()) < 0) {
            T.setLeft(delete(T.getLeft(), key));
            return T;
        } else {
            T.setRight( delete(T.getRight(), key));
            return T;
        }
    }
    // if key is in this BST, return true; otherwise, return false
    public boolean lookup(Comparable key) {
        return lookup(root, key);
    }

    private static boolean lookup(BinaryTreenode T, Comparable k) {
        if (T == null) return false;
        if (T.getKey().equals(k)) return true;

        // if not then we recurse either in the left or right subtree
        if (k.compareTo(T.getKey()) < 0) {
            // k < this node's key; look in left subtree
            return lookup(T.getLeft(), k);
        } else {
            // k > this node's key; look in right subtree
            return lookup(T.getRight(), k);
        }
    }

    // print the values in thsi BST in sorted order (to p)
    public void print(PrintWriter p) {
    // stuff here
    }

    private static BinaryTreenode smallestNode(BinaryTreenode T) {
        if (T.left == null) return T;
        else return smallestNode(T.left);
    }
}
