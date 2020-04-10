package Problems.NP;

/**
 * Created by Alestar on 2/18/2019.
 */
public class CakeThief {

    public static class CakeType {

        final int weight;
        final int value;

        public CakeType(int weight, int value) {
            this.weight = weight;
            this.value  = value;
        }
    }

    public static class InfinityException extends RuntimeException {
        public InfinityException() {
            super("Max value is infinity!");
        }
    }

    public static long maxDuffelBagValue(CakeType[] cakeTypes, int weightCapacity) {

        // we make an array to hold the maximum possible value at every
        // duffel bag weight capacity from 0 to weightCapacity
        // starting each index with value 0
        long[] maxValuesAtCapacities = new long[weightCapacity + 1];

        for (int currentCapacity = 0; currentCapacity <= weightCapacity; currentCapacity++) {

            // set a variable to hold the max monetary value so far for currentCapacity
            long currentMaxValue = 0;

            for (CakeType cakeType : cakeTypes) {

                // if a cake weighs 0 and has a positive value the value of our duffel bag is infinite!
                if (cakeType.weight == 0 && cakeType.value != 0) {
                    throw new InfinityException();
                }

                // if the current cake weighs as much or less than the current weight capacity
                // it's possible taking the cake would get a better value
                if (cakeType.weight <= currentCapacity) {

                    // so we check: should we use the cake or not?
                    // if we use the cake, the most kilograms we can include to the bag (in addition to the cake we're adding)
                    // is the current capacity minus the cake's weight.
                    // We find the max value at that integer capacity in our array maxValuesAtCapacities
                    long maxValueUsingCake = cakeType.value
                            + maxValuesAtCapacities[currentCapacity - cakeType.weight];

                    // now we see if it's worth taking the cake. how does the
                    // value with the cake compare to the currentMaxValue?
                    currentMaxValue = Math.max(maxValueUsingCake, currentMaxValue);
                }
            }

            // add each capacity's max value to our array so we can use them
            // when calculating all the remaining capacities
            maxValuesAtCapacities[currentCapacity] = currentMaxValue;
        }

        return maxValuesAtCapacities[weightCapacity];
    }

    public static void main(String[] args) {
        CakeType[] cakeTypes = new CakeType[] {
                new CakeType(7, 160),
                new CakeType(3, 90),
                new CakeType(2, 15),
        };

        int capacity = 20;

        // Complexity is O(n,C) where n is number of cakes (_n =3) and C is capacity (c = 20), at worst 3*20 = 60 calculations per runtime for the example
        //This is a bottom-top approach
        System.out.println("The max value is: " + maxDuffelBagValue(cakeTypes, capacity));
    }
}
