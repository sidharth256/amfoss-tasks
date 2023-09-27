#include <stdio.h>

int main() {
    int n, i, j;

    printf("Enter a number (n): ");
    scanf("%d", &n);
    
    if (n<2) {
        printf("There are no prime numbers below 2");
    } else {
    printf("Prime numbers up to %d:\n", n);
        
    }

    for (i = 2; i <= n; i++) {
        int isPrime = 1;

        for (j = 2; j < i; j++) {
            if (i % j == 0) {
                isPrime = 0;
                break;
            }
        }

        if (isPrime) {
            printf("%d ", i);
        }
    }

    printf("\n");

    return 0;
}
