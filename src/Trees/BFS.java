package Trees;

import java.util.*;

/**
 * Created by Alestar on 2/18/2019.
 */
public class BFS {

    private static String[] reconstructPath(Map<String, String> previousNodes,
                                            String startNode, String endNode) {

        List<String> reversedShortestPath = new ArrayList<>();

        // start from the end of the path and work backwards
        String currentNode = endNode;

        while (currentNode != null) {
            reversedShortestPath.add(currentNode);
            currentNode = previousNodes.get(currentNode);
        }

        // reverse our path to get the right order
        // by flipping it around, in place
        Collections.reverse(reversedShortestPath);
        return reversedShortestPath.toArray(new String[reversedShortestPath.size()]);
    }

    public static String[] bfsGetPath(Map<String, String[]> graph, String startNode, String endNode) {

        if (!graph.containsKey(startNode)) {
            throw new IllegalArgumentException("Start node not in graph");
        }
        if (!graph.containsKey(endNode)) {
            throw new IllegalArgumentException("End node not in graph");
        }

        Queue<String> nodesToVisit = new ArrayDeque<>();
        nodesToVisit.add(startNode);

        // keep track of how we got to each node
        // we'll use this to reconstruct the shortest path at the end
        // we'll ALSO use this to keep track of which nodes we've
        // already visited
        Map<String, String> howWeReachedNodes = new HashMap<>();
        howWeReachedNodes.put(startNode, null);

        while (!nodesToVisit.isEmpty()) {
            String currentNode = nodesToVisit.remove();

            // stop when we reach the end node
            if (currentNode.equals(endNode)) {
                return reconstructPath(howWeReachedNodes, startNode, endNode);
            }

            for (String neighbor : graph.get(currentNode)) {
                if (!howWeReachedNodes.containsKey(neighbor)) {
                    nodesToVisit.add(neighbor);
                    howWeReachedNodes.put(neighbor, currentNode);
                }
            }
        }

        // if we get here, then we never found the end node
        // so there's NO path from startNode to endNode
        return null;
    }
    public static void main(String[] args) {
        Map<String, String[]> network = new HashMap<String, String[]>() {{
            put("Min",     new String[] { "William", "Jayden", "Omar" });
            put("William", new String[] { "Min", "Noam" });
            put("Jayden",  new String[] { "Min", "Amelia", "Ren", "Noam" });
            put("Ren",     new String[] { "Jayden", "Omar" });
            put("Amelia",  new String[] { "Jayden", "Adam", "Miguel" });
            put("Adam",    new String[] { "Amelia", "Miguel", "Sofia", "Lucas" });
            put("Miguel",  new String[] { "Amelia", "Adam", "Liam", "Nathan" });
            put("Noam",    new String[] { "Nathan", "Jayden", "William" });
            put("Omar",    new String[] { "Ren", "Min", "Scott" });
        }};
        System.out.println("The route for the message is: " + Arrays.toString(bfsGetPath(network,"Jayden", "Adam")));
    }
}
