package DAA;

// Recursive
import java.util.Scanner;

public class Fibonacci_Recursive_01 {
    static int fib(int n) {
        if (n <= 1) {
            return 1;
        }
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter num:");
        int num = sc.nextInt();

        System.out.println("Recursive Fibonacci: ");
        for (int i = 0; i < num; i++) {
            System.out.print(fib(i) + " ");
        }

        sc.close();
    }
}
