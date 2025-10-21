package MyJava.DataStructure.Trie;

//import org.testng.annotations.Test;

//import org.junit.Test;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
//import static org.testng.Assert.assertTrue;

public class TrieGeneric {

    private TrieNodeGeneric root;

    public TrieGeneric() {
        this.root = new TrieNodeGeneric();
    }
    // If not present, inserts word into trie
    // If the word is prefix of trie node,
    // just marks leaf node

    /**
     *
     * @param word
     *
     * Set a current node as a root node
     * Set the current letter as the first letter of the word
     * If the current node has already an existing reference to the current letter (through one of the elements in the “children” field),
     * then set current node to that referenced node. Otherwise, create a new node, set the letter equal to the current letter,
     * and also initialize current node to this new node
     * Repeat step 3 until the key is traversed
     */
    public void insert(String word) {
        TrieNodeGeneric current = root;

        for (int i = 0; i < word.length(); i++) {
            current = current.getChildren()
                    .computeIfAbsent(word.charAt(i), c -> new TrieNodeGeneric());
        }
        current.setEndOfWord(true);
    }

    // Returns true if word presents in trie, else false

    /**
     * * @param word
     * @return
     *
     * Get children of the root
     * Iterate through each character of the String
     * Check whether that character is already a part of a sub-trie. If it isn't present anywhere in the trie, then stop the search and return false
     * Repeat the second and the third step until there isn't any character left in the String. If the end of the String is reached, return true
     */
    public boolean find(String word) {
        TrieNodeGeneric current = root;
        for (int i = 0; i < word.length(); i++) {
            char ch = word.charAt(i);
            TrieNodeGeneric node = current.getChildren().get(ch);
            if (node == null) {
                return false;
            }
            current = node;
        }
        return current.isEndOfWord();
    }

    /**
     * @param word
     *
     * Check whether this element is already part of the trie
     * If the element is found, then remove it from the trie
     */
    public void delete(String word) {
        delete(root, word, 0);
    }

    private boolean delete(TrieNodeGeneric current, String word, int index) {
        if (index == word.length()) {
            if (!current.isEndOfWord()) {
                return false;
            }
            current.setEndOfWord(false);
            return current.getChildren().isEmpty();
        }
        char ch = word.charAt(index);
        TrieNodeGeneric node = current.getChildren().get(ch);
        if (node == null) {
            return false;
        }
        boolean shouldDeleteCurrentNode = delete(node, word, index + 1) && !node.isEndOfWord();

        if (shouldDeleteCurrentNode) {
            current.getChildren().remove(ch);
            return current.getChildren().isEmpty();
        }
        return false;
    }

    private static TrieGeneric createExampleTrie() {
        TrieGeneric trie = new TrieGeneric();

        trie.insert("Programming");
        trie.insert("is");
        trie.insert("a");
        trie.insert("way");
        trie.insert("of");
        trie.insert("life");
        return trie;
    }


    @Test
    public void givenATrie_WhenAddingElements_ThenTrieContainsThoseElements() {
        TrieGeneric trie = createExampleTrie();

        assertFalse(trie.find("3"));
        assertFalse(trie.find("vida"));
        assertTrue(trie.find("life"));
    }

    @Test
    void whenDeletingElements_ThenTreeDoesNotContainThoseElements() {
        TrieGeneric trie = createExampleTrie();

        assertTrue(trie.find("life"));
        trie.delete("life");
        assertFalse(trie.find("life"));
    }

    // Driver
    public static void main(String args[]){

    }

}
