package Algorithms.Sorting;


import java.util.Comparator;

public class Checker implements Comparator<Checker.Player> {

    public class Player{
        int score;
        String name;
    }
    public int compare(Player a, Player b) {
        if(a.score == b.score){
            return a.name.compareTo(b.name);
        }
        return b.score -a.score;
    }
}
