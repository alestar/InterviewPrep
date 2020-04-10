package DataStructure.Trie;

import java.util.HashMap;

/**
 * Created by Alestar on 2/16/2019.
 */
public class TrieUsingHashMap {

    class TrieNode {

        private HashMap<Character, TrieNode> nodeChildren;

        public TrieNode() {
            this.nodeChildren = new HashMap<>();
        }

        public boolean hasChildNode(char character) {
            return this.nodeChildren.containsKey(character);
        }

        public void makeChildNode(char character) {
            this.nodeChildren.put(character, new TrieNode());
        }

        public TrieNode getChildNode(char character) {
            return this.nodeChildren.get(character);
        }
    }
    private TrieNode rootNode;
    private static final char END_OF_WORD_MARKER = '\0';

    public TrieUsingHashMap() {
        this.rootNode = new TrieNode();
    }

    public boolean addWord(String word) {

        TrieNode currentNode = this.rootNode;
        boolean isNewWord = false;

        // Work downwards through the trie, adding nodes
        // as needed, and keeping track of whether we add
        // any nodes.
        for (int i = 0; i < word.length(); i++) {
            char character = word.charAt(i);

            if (!currentNode.hasChildNode(character)) {
                isNewWord = true;
                currentNode.makeChildNode(character);
            }

            currentNode = currentNode.getChildNode(character);
        }

        // Explicitly mark the end of a word.
        // Otherwise, we might say a word is
        // present if it is a prefix of a different,
        // longer word that was added earlier.
        if (!currentNode.hasChildNode(END_OF_WORD_MARKER)) {
            isNewWord = true;
            currentNode.makeChildNode(END_OF_WORD_MARKER);
        }

        return isNewWord;
    }

    public boolean searchWord(String word) {
        TrieNode currentNode = this.rootNode;
        boolean found = false;

        // Work downwards through the trie, /
        // if it does not contains a char then short circuit return
        for (int i = 0; i < word.length(); i++) {
            char character = word.charAt(i);

            if (!currentNode.hasChildNode(character))
                return false;
            currentNode = currentNode.getChildNode(character);
        }
        //If the getLast node is not null and it has the end of word mark then the word was found TRUE
         return (currentNode != null && currentNode.hasChildNode(END_OF_WORD_MARKER));
    }

    public static void main(String args[])
    {
        // Input keys (use only 'a' through 'z' and lower case)
        String keys[] = {"the", "a", "there", "answer", "any",
                "by", "bye", "their"};

        String output[] = {"Not present in trie", "Present in trie"};
        TrieUsingHashMap trie= new TrieUsingHashMap();

        // Construct trie
        int i;
        for (i = 0; i < keys.length ; i++)
            trie.addWord(keys[i]);

        // Search for different keys
        if(trie.searchWord("the") == true)
            System.out.println("the --- " + output[1]);
        else System.out.println("the --- " + output[0]);

        if(trie.searchWord("these") == true)
            System.out.println("these --- " + output[1]);
        else System.out.println("these --- " + output[0]);

        if(trie.searchWord("their") == true)
            System.out.println("their --- " + output[1]);
        else System.out.println("their --- " + output[0]);

        if(trie.searchWord("thaw") == true)
            System.out.println("thaw --- " + output[1]);
        else System.out.println("thaw --- " + output[0]);

    }
}
