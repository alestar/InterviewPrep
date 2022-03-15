package Java.DataStructure.Trie;

/**
 * Created by Alestar on 2/16/2019.
 */
// Java implementation of search and insert operations
// on Java.DataStructure.Trie
public class TrieUsingArrays {
    // Alphabet size (# of symbols)
    static final int ALPHABET_SIZE = 26;

    // trie node
    static class TrieNode{
        TrieNode[] children = new TrieNode[ALPHABET_SIZE];

        // isEndOfWord is true if the node represents
        // end of a word
        boolean isEndOfWord;

        TrieNode(){
            isEndOfWord = false;
            for (int i = 0; i < ALPHABET_SIZE; i++)
                children[i] = null;
        }
    };

    static TrieNode root  = new TrieNode();

    // If not present, inserts word into trie
    // If the word is prefix of trie node,
    // just marks leaf node
    static void insert(String word){
        int index;
        TrieNode curentNode = root;

        for (int level = 0; level < word.length(); level++)
        {
            index = word.charAt(level) - 'a';
            if (curentNode.children[index] == null)
                curentNode.children[index] = new TrieNode();

            curentNode = curentNode.children[index];
        }

        // mark getLast node as leaf
        curentNode.isEndOfWord = true;
    }

    // Returns true if word presents in trie, else false
    static boolean search(String word){

        int index;
        TrieNode curr = root;

        for (int level = 0; level < word.length(); level++)
        {
            index = word.charAt(level) - 'a';

            if (curr.children[index] == null)
                return false;

            curr = curr.children[index];
        }

        return (curr != null && curr.isEndOfWord);
    }

    // Driver
    public static void main(String args[])
    {
        // Input words (use only 'a' through 'z' and lower case)
        String words[] = {"the", "a", "there", "answer", "any",
                "by", "bye", "their"};
        String output[] = {"Not present in trie", "Present in trie"};


        // Construct trie
        for (int i = 0; i < words.length ; i++)
            insert(words[i]);

        // Search for different words
        if(search("the") == true)
            System.out.println("the --- " + output[1]);
        else System.out.println("the --- " + output[0]);

        if(search("these") == true)
            System.out.println("these --- " + output[1]);
        else System.out.println("these --- " + output[0]);

        if(search("their") == true)
            System.out.println("their --- " + output[1]);
        else System.out.println("their --- " + output[0]);

        if(search("thaw") == true)
            System.out.println("thaw --- " + output[1]);
        else System.out.println("thaw --- " + output[0]);

    }
}




