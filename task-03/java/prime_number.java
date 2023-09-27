import java.util.Scanner;

public class PrimeNumbers {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number (n): ");
        
        int n;
        while (true) {
            if (scanner.hasNextInt()) {
                n = scanner.nextInt();
                break;
            } else {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.nextLine();
            }
        }
        
        
        if (n < 2) {
            System.out.print("There are no prime numbers below 2");
        } else {
            System.out.println("Prime numbers up to " + n + ":");
        }
        for (int i = 2; i <= n; i++) {
            boolean isPrime = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
        
        scanner.close();
    }
}    
