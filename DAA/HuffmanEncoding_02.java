package DAA;
import java.util.PriorityQueue;

class HuffmanNode {
    int freq;
    char symbol;
    HuffmanNode left, right;

    HuffmanNode(char symbol, int freq) {
        this.symbol = symbol;
        this.freq = freq;
        this.left = null;
        this.right = null;
    }
}

public class HuffmanEncoding_02 {

    // Function to print Huffman Codes (recursive)
    static void printCodes(HuffmanNode root, String code) {
        if (root == null)
            return;

        // If it's a leaf node → print symbol and its code
        if (root.left == null && root.right == null && root.symbol != '#') {
            System.out.println(root.symbol + " -> " + code);
            return;
        }

        // Traverse left as '0' and right as '1'
        printCodes(root.left, code + "0");
        printCodes(root.right, code + "1");
    }

    public static void main(String[] args) {
        char[] chars = { 'a', 'b', 'c', 'd', 'e', 'f' };
        int[] freqs = { 5, 9, 12, 13, 16, 45 };

        // Min-heap (priority queue) based on frequency
        PriorityQueue<HuffmanNode> pq = new PriorityQueue<>((a, b) -> a.freq - b.freq);

        // Step 1: Create leaf nodes for each character
        for (int i = 0; i < chars.length; i++) {
            pq.add(new HuffmanNode(chars[i], freqs[i]));
        }

        // Step 2: Build the Huffman Tree
        while (pq.size() > 1) {
            // Pick two smallest frequency nodes
            HuffmanNode left = pq.poll();
            HuffmanNode right = pq.poll();

            // Create a new internal node with combined frequency
            HuffmanNode newNode = new HuffmanNode('#', left.freq + right.freq);
            newNode.left = left;
            newNode.right = right;

            // Add the new node back into the priority queue
            pq.add(newNode);
        }

        // Step 3: Print Huffman Codes
        System.out.println("Huffman Codes:");
        printCodes(pq.peek(), "");
    }
}