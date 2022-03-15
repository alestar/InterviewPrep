package Java.DataStructure.Trie;

import java.util.HashMap;

public class TrieNodeGeneric {

    private static int ALPHABET_SIZE = 26;// Alphabet Characters
    private HashMap<Character, TrieNodeGeneric> children;
    private String content;
    private boolean endOfWord;

    public TrieNodeGeneric() {
        this.children = new HashMap<>();
    }


    public HashMap<Character, TrieNodeGeneric> getChildren() {
        return children;
    }

    public void setChildren(HashMap<Character, TrieNodeGeneric> children) {
        this.children = children;
    }

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public boolean isEndOfWord() {
        return endOfWord;
    }

    public void setEndOfWord(boolean endOfWord) {
        this.endOfWord = endOfWord;
    }

}
