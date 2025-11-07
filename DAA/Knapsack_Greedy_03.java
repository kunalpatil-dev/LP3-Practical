package DAA;
import java.util.*;

class Item {
    int value, weight;
    double ratio;

    Item(int value, int weight) {
        this.value = value;
        this.weight = weight;
        this.ratio = (double) value / weight;
    }
}

public class Knapsack_Greedy_03 {

    public static double fractionalKnapsack(int capacity, int[] values, int[] weights) {
        int n = values.length;

        // Step 1: Create list of Items
        Item[] items = new Item[n];
        for (int i = 0; i < n; i++) {
            items[i] = new Item(values[i], weights[i]);
        }

        // Step 2: Sort descending by ratio
        Arrays.sort(items, (a, b) -> Double.compare(b.ratio, a.ratio));

        double totalValue = 0.0;

        // Step 3: Pick items
        for (Item item : items) {
            if (capacity == 0)
                break;

            if (item.weight <= capacity) {
                // Take full item
                totalValue += item.value;
                capacity -= item.weight;
            } else {
                // Take fraction
                totalValue += item.value * ((double) capacity / item.weight);
                capacity = 0; // Knapsack full
            }
        }

        return totalValue;
    }

    public static void main(String[] args) {
        int[] values = { 60, 100, 120 };
        int[] weights = { 10, 20, 30 };
        int capacity = 50;

        double maxValue = fractionalKnapsack(capacity, values, weights);
        System.out.println("Maximum value in knapsack = " + maxValue);
    }
}
