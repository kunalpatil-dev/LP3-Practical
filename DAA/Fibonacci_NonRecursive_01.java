package DAA;
// Iterative
public class Fibonacci_NonRecursive_01 {

    static void fib(int n) {
        int a = 0, b = 1, c;

        if (n >= 1)
            System.out.print(a + " ");
        if (n >= 2)
            System.out.print(b + " ");

        for (int i = 2; i < n; i++) {
            c = a + b;
            System.out.print(c + " ");
            a = b;
            b = c;
        }
    }

    public static void main(String[] args) {
        int n = 10;

        System.out.println("Iterative Fibonacci:");
        fib(n);
    }
}
