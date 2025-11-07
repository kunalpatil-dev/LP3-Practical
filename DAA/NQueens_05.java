package DAA;
public class NQueens_05 {

    static final int N = 8;           // board size
    static int[][] board = new int[N][N];

    // Print the board
    static void printBoard() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i][j] == 1 ? "Q " : ". ");
            }
            System.out.println();
        }
        System.out.println();
    }

    // Check if placing a queen at (row, col) is safe
    static boolean isSafe(int row, int col) {

        // Check column
        for (int i = 0; i < row; i++)
            if (board[i][col] == 1)
                return false;

        // Check upper left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--)
            if (board[i][j] == 1)
                return false;

        // Check upper right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < N; i--, j++)
            if (board[i][j] == 1)
                return false;

        return true;
    }

    // Solve recursively
    static boolean solve(int row) {
        // Base case
        if (row == N) {
            System.out.println("Final 8-Queens Solution:\n");
            printBoard();
            return true;
        }

        // Try all columns for this row
        for (int col = 0; col < N; col++) {
            if (isSafe(row, col)) {
                board[row][col] = 1;

                if (solve(row + 1))
                    return true;

                board[row][col] = 0;   // Backtrack
            }
        }
        return false;
    }

    public static void main(String[] args) {

        // Initialize: First queen at (0, 0)
        board[0][0] = 1;

        System.out.println("Starting with first Queen at (0, 0):\n");
        printBoard();

        // Solve remaining queens
        if (!solve(1)) {
            System.out.println("No solution found!");
        }
    }
}
