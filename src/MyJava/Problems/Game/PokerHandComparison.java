package MyJava.Problems.Game;

/**
 * Created by Alestar on 3/31/2019.
 */

/**
* Given a set of 5 playing card identifiers such as 2H, 7C, QS, 10D, 2D;
* determine if this hand is better than some other hand, according to the rules of poker.
*
* Hands will be a string with 5 cards comma separated,
* each card will have 1-2 digits or Jack(J), Queen(Q), King(K), Ace(A) and a 'suit' indicator Clubs/Clover(C), Diamonds(D), Spade(S), Heart(H) (i.e. 10C, KH)
*
* Possible Hand Types Below:
*	Royal flush : A, K, Q, J, 10, all the same suit.
*	Straight flush: Five cards in a sequence, all in the same suit. (i.e 8C, 7C, 6C, 5C, 4C)
* 	Four of a kind: All four cards of the same rank. (i.e JH, JD, JS, JC, 7C)
* 	Full house: Three of a kind with a pair. (i.e 10H, 10D, 10S, 9C, 9D )
* 	Flush: Any five cards of the same suit, but not in a sequence (i.e 4S, JS, 8S, 2S, 9S )
* 	Straight: Five cards in a sequence, but not of the same suit. (i.e 9C, 8D, 7S, 6D, 5H)
* 	Three of a kind: Three cards of the same rank. (i.e 7C, 7D, 7S, KC, 3D)
*   Two pair: Two cards of the same rank. (i.e 4C, 4S, 3C, 3D, QC)
*   One pair: Two cards of the same rank. (i.e AH, AD, 8C, 4S, 7H)
*	High Card : When you haven't made any of the hands above, the highest card plays.
*				In the example below, the jack plays as the highest card.
*
*
*   The ranking of suits from highest to lowest is Spades > Hearts > Diamonds > Clubs.
*   Suits never break a tie for winning a pot.
*   Suits are used only in stud and then only to break a tie between cards of the same rank (no redeal or redraw).
*
* The goal of this is to compare between the hand types.
* Comparing 2 of the same type (i.e. 2 straights) to determine a winner is outside the scope
* and will not be tested.
*
* Implement PokerHand.isGreaterThan(...) method and return whether or not the first hand wins over the second hand.
*/
public class PokerHandComparison {


    static class PokerHand {

        private String handAsString;
        private int[] value; // Used to represent value of each hand

        public PokerHand(String hand) {
            handAsString = hand;
            value = new int[6];
        }

        public Boolean isGreaterThan(PokerHand hand2) {
            // This is where you'll implement the poker hand comparison logic

            String[] handArr1 = convertStringHandToArr(this.handAsString);
            String[] handArr2 = convertStringHandToArr(hand2.handAsString);

            int[] ranksHand1 = countRanksOfEachCard(handArr1);
            int[] ranksHand2 = countRanksOfEachCard(handArr2);


            this.value = createHandValueArr(ranksHand1, handArr1);
            hand2.value = createHandValueArr(ranksHand2, handArr2);

            return compareTo(hand2) == 1 ? true : false;
        }

        private String[] convertStringHandToArr(String hand) {
            return hand.split(",");
        }

        private String[] convertStringCardToArr(String card) {
            String suite = card.substring(card.length() - 1);
            String rank = card.substring(0, card.length() - 1);
            String[] cardArr = {rank, suite};
            return cardArr;
        }

        private int determineCardRank(String[] card) {
            switch (card[0]) {
                case "A":
                    return 1;
                case "2":
                    return 2;
                case "3":
                    return 3;
                case "4":
                    return 4;
                case "5":
                    return 5;
                case "6":
                    return 6;
                case "7":
                    return 7;
                case "8":
                    return 8;
                case "9":
                    return 9;
                case "10":
                    return 10;
                case "J":
                    return 11;
                case "Q":
                    return 12;
                case "K":
                    return 13;
            }
            return -1;
        }

        private int determineCardRankBySuite(String[] card) {

            switch (card[1]) {
                case "C":
                    return 1;
                case "D":
                    return 2;
                case "H":
                    return 3;
                case "S":
                    return 4;
            }
            return -1;
        }

        private int[] countRanksOfEachCard(String hand[]) {

            int[] ranks = new int[14];// First index of the array will be empty to correspond with the Cards rank numbering
            for (int x = 0; x <= 13; x++) {
                ranks[x] = 0; //zero the contents of the array
            }

            for (int x = 0; x <= 4; x++)// For the five Card in the Hand
            {
                String[] c = convertStringCardToArr(hand[x]);
                int r = determineCardRank(c);
                ranks[r]++;
                //increment rank array at the index of each card's rank
            }
            return ranks;
        }

        private int[] getOrderedRank(int ranks[]) {

            int[] orderedRanks = new int[5];
            int index = 0;


            if (ranks[1] == 1) //if ace, run this before because ace is highest card
            {
                //record an ace as 14 instead of one, as its the highest card
                orderedRanks[index] = 14;
                index++; //increment position
            }

            for (int x = 13; x >= 2; x--) {
                if (ranks[x] == 1)
                //we have already written code to handle the case
                //of their being two cards of the same rank
                {
                    orderedRanks[index] = x;
                    index++;
                }
            }
            return orderedRanks;
        }

        private int determineCardRankGroup(int[] ranks, Integer sameCardsBigGroup, Integer sameCardsSmallGroup, Integer rankBigGroup, Integer rankSmallGroup) {

            for (int x = 13; x >= 1; x--) {
                if (ranks[x] > sameCardsBigGroup) {
                    if (sameCardsBigGroup != 1) {//Check if 'sameCardsBigGroup' was previously assigned to something before overwriting it,
                        // So if a pair was found earlier is recorded.
                        sameCardsSmallGroup = sameCardsBigGroup;
                        rankSmallGroup = rankBigGroup;
                    }

                    sameCardsBigGroup = ranks[x];
                    rankBigGroup = x;

                } else if (ranks[x] > sameCardsSmallGroup) {
                    sameCardsSmallGroup = ranks[x];
                    rankSmallGroup = x;
                }
            }
            return rankBigGroup;
        }

        boolean isFlush(String[] hand) {
            boolean flush = true; //assume there is a flush
            for (int x = 0; x < 4; x++) {
                String[] current = convertStringCardToArr(hand[x]);
                String[] next = convertStringCardToArr(hand[x]);
                if (current[1] != next[1])//if two cards are not the same suit, then there's no flush
                    flush = false;
            }
            return flush;
        }

        boolean isStraight(int ranks[]) {

            int topStraightValue = 0;
            boolean straight = false;  //assume no straight
            for (int x = 1; x <= 9; x++) //can't have straight with lowest value of more than 10, straight will start 1-9, except special case
            {
                if (ranks[x] == 1 && ranks[x + 1] == 1 && ranks[x + 2] == 1 &&
                        ranks[x + 3] == 1 && ranks[x + 4] == 1) {
                    straight = true;
                    topStraightValue = x + 4; //4 above bottom value
                    break;
                }
            }

            if (ranks[10] == 1 && ranks[11] == 1 && ranks[12] == 1 &&
                    ranks[13] == 1 && ranks[1] == 1) //special case: ace high
            {
                straight = true;
                topStraightValue = 14; //higher than king
            }
            return straight;

        }

        private int[] createHandValueArr(int[] ranks, String[] hand) {
            int[] value = new int[6];
            int[] orderedRanks = getOrderedRank(ranks);
            Integer sameCardsBigGroup = 1, sameCardsSmallGroup = 1, rankBigGroup = 0, rankSmallGroup = 0;
            determineCardRankGroup(ranks, sameCardsBigGroup, sameCardsSmallGroup, rankBigGroup, rankSmallGroup);

            boolean isStraight = isStraight(ranks);
            boolean isFlush = isFlush(hand);

            if (sameCardsBigGroup == 1) {    //if we have no pair...
                value[0] = 1;                //this is the lowest type of hand, so it gets the lowest value
                value[1] = orderedRanks[0];  //the first determining factor is the highest card,
                value[2] = orderedRanks[1];  //then the next highest card,
                value[3] = orderedRanks[2];  //and so on
                value[4] = orderedRanks[3];
                value[5] = orderedRanks[4];
            }

            if (sameCardsBigGroup == 2 && sameCardsSmallGroup == 1) //if 1 pair
            {
                value[0] = 2;                //pair ranked higher than high card
                value[1] = rankBigGroup;   //rank of pair
                value[2] = orderedRanks[0];  //next highest cards.
                value[3] = orderedRanks[1];
                value[4] = orderedRanks[2];
            }

            if (sameCardsBigGroup == 2 && sameCardsSmallGroup == 2) //two pair
            {
                value[0] = 3;
                //rank of greater pair
                value[1] = rankBigGroup > rankSmallGroup ? rankBigGroup : rankSmallGroup;
                //rank of smaller pair
                value[2] = rankBigGroup < rankSmallGroup ? rankBigGroup : rankSmallGroup;
                value[3] = orderedRanks[0];  //extra card
            }

            if (sameCardsBigGroup == 3 && sameCardsSmallGroup != 2){//three of a kind (not full house)
                value[0] = 4;
                value[1] = rankBigGroup;
                value[2] = orderedRanks[0];
                value[3] = orderedRanks[1];
            }
            if (isStraight){
                value[0] = 5;
                value[1] =orderedRanks[0];;
                //if we have two straights,
                //the one with the highest top cards wins
            }

            if (isFlush){
                value[0] = 6;
                value[1] = orderedRanks[0]; //tie determined by ranks of cards
                value[2] = orderedRanks[1];
                value[3] = orderedRanks[2];
                value[4] = orderedRanks[3];
                value[5] = orderedRanks[4];
            }

            if (sameCardsBigGroup == 3 && sameCardsSmallGroup == 2){ //full house
                value[0] = 7;
                value[1] = rankBigGroup;
                value[2] = rankSmallGroup;
            }

            if (sameCardsBigGroup == 4){  //four of a kind
                value[0] = 8;
                value[1] = rankBigGroup;
                value[2] = orderedRanks[0];
            }

            if (isStraight && isFlush){  //straight flush
                value[0] = 9;
                value[1] =orderedRanks[0];
            }
            return value;
        }

        int compareTo(PokerHand that) {
            for (int x = 0; x < 6; x++) //cycle through values
            {
                if (this.value[x] > that.value[x])
                    return 1;
                else if (this.value[x] < that.value[x])
                    return -1;
            }
            return 0; //if hands are equal
        }

        @Override
        public String toString() {
            return handAsString;
        }

        public static void testHand1IsGreaterThanHand2(String hand1AsString, String hand2AsString, Boolean expectedResult) {
            PokerHand hand1 = new PokerHand(hand1AsString);
            PokerHand hand2 = new PokerHand(hand2AsString);
            System.out.println("Hand1[" + hand1 + "] > Hand2[" + hand2 + "] \t-- " +
                    "expected: " + expectedResult + ", actual: " + hand1.isGreaterThan(hand2));
        }

        public static void main(String[] args) {
            testHand1IsGreaterThanHand2(
                    "8C,9C,10C,JC,QC", // Straight flush: Five cards in a sequence, all in the same suit. (i.e 8C, 7C, 6C, 5C, 4C)
                    "6S,7H,8D,9H,10D",
                    true);

            testHand1IsGreaterThanHand2(
                    "4H,4D,4C,4S,JS", // Four of a kind: All four cards of the same rank. (i.e JH, JD, JS, JC, 7C)
                    "6C,6S,KH,AS,AD",
                    true);

            testHand1IsGreaterThanHand2(
                    "6C,6D,6H,9C,KD",
                    "5C,3C,10C,KC,7C", // Flush: Any five cards of the same suit, but not in a sequence (i.e 4S, JS, 8S, 2S, 9S )
                    false);

            testHand1IsGreaterThanHand2(
                    "4H,4D,4C,KC,KD", // Full house: Three of a kind with a pair. (i.e 10H, 10D, 10S, 9C, 9D )
                    "9D,6S,KH,AS,AD",
                    true);

            testHand1IsGreaterThanHand2(
                    "6C,6D,6H,9C,KD",
                    "2C,3C,4S,5S,6S", // Straight: Five cards in a sequence, but not of the same suit. (i.e 9C, 8D, 7S, 6D, 5H)
                    false);

            testHand1IsGreaterThanHand2(
                    "7C,7D,7S,3H,4D", // Three of a kind: Three cards of the same rank. (i.e 7C, 7D, 7S, KC, 3D)
                    "9S,6S,10D,AS,AD",
                    true);

            testHand1IsGreaterThanHand2(
                    "2S,2D,JH,7S,AC",
                    "8C,8H,10S,KH,KS", // Two pair: Two cards of the same rank. (i.e 4C, 4S, 3C, 3D, QC)
                    false);

            testHand1IsGreaterThanHand2(
                    "AC,AH,3C,QH,10C", // One pair: Two cards of the same rank. (i.e AH, AD, 8C, 4S, 7H)
                    "3S,2D,KH,JS,AD",
                    true);
        }
    }
}


