/**
 * Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
 */

/* ANSWER:
 * A simple graph traversal can be used here. In this cased I decided on an
 * iterative BFS solution. This uses a simple linked list queue and enum states
 * to keep track of which nodes it has already visited. This is to avoid an
 * infinite cycle in our traversal.
 *
 * While DFS could potentially faster, it also has the potential of being much
 * slower as it might traverse verly deeply in node's adjacent nodes before
 * checking the next node.
 */

public enum State {
    Unvisited, Visited, Visiting;
}

public static boolean search(Graph g, Node start, Node end) {
    // operates a Queue
    LinkedList<Node> q = new LinkedList<Node>();

    for (Node u : g.getNodes()) {
        u.state = State.Unvisited;
    }
    start.state = State.Visiting;
    q.add(start);
    Node u;
    while (!q.isEmpty()) {
        u = q.removeFisrt(); // i.e., dequeue()
        if ( u != null) {
            for (Node v : u.getAdjacent()) {
                if (v.state == State.Unvisited) {
                    if (v == end) {
                        return true;
                    } else {
                        v.state = State.Visiting;
                        q.add(v);
                    }
                }
            }
            u.state = State.Visited;
        }
    }
    return false;
}
