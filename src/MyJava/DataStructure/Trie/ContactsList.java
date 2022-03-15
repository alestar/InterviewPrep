package MyJava.DataStructure.Trie;

public class ContactsList {

    private static int NUMBER_OF_CHARACTERS = 26;// Alphabet Characters
    TrieNodeGeneric[] children= new TrieNodeGeneric[NUMBER_OF_CHARACTERS];

    private TrieGeneric trieGen;
    private int size = 0;

    private static int getCharIndex(char c){
        return c- 'a';
    }

    private TrieNodeGeneric retrieveNode(char c){
        return children[getCharIndex(c)];
    }

    private void addNode(char c, TrieNodeGeneric node){
        children[getCharIndex(c)] =  node;
    }

    public void addWord(String s){

        addWordFromIndex(s.toLowerCase(), 0);
    }

    public void addWordFromIndex(String s, int index){

      if(index == s.length()) return;

      char current = s.charAt(index);
      TrieNodeGeneric child = retrieveNode(current);
      if(child == null){
          child = new TrieNodeGeneric();
          addNode(current,child);
          size++;
      }
      this.addWordFromIndex(s, index +1);
    }

    public int findCount(String s, int index){

        if(index == s.length()){
            return size;
        }
        TrieNodeGeneric child = retrieveNode(s.toLowerCase().charAt(index));
        if(child == null){
            return 0;
        }
        return this.findCount(s, index +1);


    }


    public static void main(String[] args) {

        String names[] = {"Gayle", "Gary", "Geena", "Alex", "Andy"};

        ContactsList contacts= new ContactsList();
        contacts.addWord(names[0]);
        contacts.addWord(names[1]);
        contacts.addWord(names[2]);
        contacts.addWord(names[3]);
        contacts.addWord(names[4]);

        System.out.println("Added Name 'Gayle': " + contacts.findCount(names[0],0));
        System.out.println("Added Name 'Gary': " + contacts.findCount(names[1],0));
        System.out.println("Added Name 'Geena': " + contacts.findCount(names[2],0));
        System.out.println("Added Name 'Alex': " + contacts.findCount(names[3],0));
        System.out.println("Added Name 'Andy': " + contacts.findCount(names[4],0));
    }

}


