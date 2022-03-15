package Java.Algorithms.Search;

import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;

/**
 * Depth-first search (DFS) is a method for exploring a tree or graph. In a DFS,
 * you go as deep as possible down one path before backing up and trying a different one.
 *
 * Depth-first search is like walking through a corn maze. You explore one path, hit a dead end, and go back and try a different one.
 *
 * Here's a how a DFS would traverse this tree, starting with the root.
 *
 * We'd go down the first path we find until we hit a dead end.
 *
 * Then we'd do the same thing again—go down a path until we hit a dead end. And again, and again, and again.
 *
 * Until we reach the end.
 *
 * Depth-first search is often compared with breadth-first search.
 *
 * Advantages:
 *      Depth-first search on a binary tree generally requires less memory than breadth-first.
 *      Depth-first search can be easily implemented with recursion.
 *  Disadvantages:
 *      A DFS doesn't necessarily find the shortest path to a node, while breadth-first search does.
 *
 * ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
 * Breadth-first search (BFS) is a method for exploring a tree or graph. In a BFS, you first explore all the nodes one step away,
 * then all the nodes two steps away, etc.
 *
 * Breadth-first search is like throwing a stone in the center of a pond. The nodes you explore "ripple out" from the starting point.
 *
 * Here's a how a BFS would traverse this tree, starting with the root.
 *
 * We'd visit all the immediate children (all the nodes that're one step away from our starting node).
 *
 * Then we'd move on to all those nodes' children (all the nodes that're two steps away from our starting node).
 *
 * And so on. Until we reach the end.
 *
 *Breadth-first search is often compared with depth-first search.
 *
 * Advantages:
 *   A BFS will find the shortest path between the starting point and any other reachable node.
 *   A depth-first search will not necessarily find the shortest path.
 * Disadvantages:
 *   A BFS on a binary tree generally requires more memory than a DFS.
 *
 */

public class GraphIntegerDFSBFS {

    private HashMap<Integer, Node> nodeLookup = new HashMap<>();

    public static class Node {
        private int id;
        LinkedList<Node> adjacent = new LinkedList<>();

        private Node(int id) {
            this.id = id;
        }
    }

    //@Todo: Get node by id
    private Node getNode(int id) {
        return new Node(id);
    }

    //@Todo: Add edfge in between nodes
    public void addEdge(int source, int dest) {

    }

    public boolean hasPathDFS(int source, int dest) {
        Node s = getNode(source);
        Node d = getNode(dest);
        HashSet<Integer> visited = new HashSet<Integer>();
        return hasPathDFS(s, d, visited);
    }

    private boolean hasPathDFS(Node source, Node dest, HashSet<Integer> visited) {
        if (visited.contains(source.id)) {
            return false;
        }
        visited.add(source.id);

        if (source == dest) {
            return true;
        }
        for (Node child : source.adjacent) {
            if (hasPathDFS(child, dest, visited)) {
                return true;
            }
        }
        return false;
    }

    private boolean hasPathBFS(Node source, Node dest) {
        LinkedList<Node> nextToVisit = new LinkedList<>();
        HashSet<Integer> visited = new HashSet<Integer>();
        nextToVisit.add(source);
        while (!nextToVisit.isEmpty()) {
            Node node = nextToVisit.remove();
            if (node == dest) {
                return true;
            }

            if (visited.contains(node.id)) {
                continue;
            }
            for (Node child : node.adjacent) {
                nextToVisit.add(child);
            }
        }
        return false;
    }




}
