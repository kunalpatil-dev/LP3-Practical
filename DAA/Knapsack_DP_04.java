package DAA;
public class Knapsack_DP_04 {

    static int knapsack(int[] values, int[] weights, int capacity) {
        int n = values.length;
        int[][] dp = new int[n + 1][capacity + 1];

        // Build table dp[][] in bottom-up manner
        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                if (i == 0 || w == 0)
                    dp[i][w] = 0;
                else if (weights[i - 1] <= w)
                    dp[i][w] = Math.max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]);
                else
                    dp[i][w] = dp[i - 1][w];
            }
        }

        // Backtracking to find selected items
        int res = dp[n][capacity];
        int w = capacity;
        System.out.println("Selected Items:");
        for (int i = n; i > 0 && res > 0; i--) {
            if (res != dp[i - 1][w]) {
                System.out.println("Item with weight " + weights[i - 1] + " and value " + values[i - 1]);
                res -= values[i - 1];
                w -= weights[i - 1];
            }
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) {
        int[] values = { 60, 100, 120 };
        int[] weights = { 10, 20, 30 };
        int capacity = 50;

        int maxValue = knapsack(values, weights, capacity);
        System.out.println("Maximum value achievable: " + maxValue);
    }
}