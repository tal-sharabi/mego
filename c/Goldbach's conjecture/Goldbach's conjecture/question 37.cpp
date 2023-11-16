#include <stdio.h>

int isPrime(int num);
void checkGoldbachConjecture(int num);

int main() {
    int num;

    for (num = 4; num <= 100000; num += 2) {
        checkGoldbachConjecture(num);
    }

    return 0;
}

int isPrime(int num) {
    int divisor;

    if (num <= 1) {
        return 0;
    }

    for (divisor = 2; divisor <= num / 2; divisor++) {
        if (num % divisor == 0) {
            return 0;
        }
    }

    return 1;
}

void checkGoldbachConjecture(int num) {
    int i;

    if (num % 2 != 0) {
        // Even numbers are only the sum of two odd primes
        return;
    }

    for (i = 2; i <= num / 2; i++) {
        if (isPrime(i) && isPrime(num - i)) {
            printf("%d = %d + %d\n", num, i, num - i);
            return;
        }
    }

    // If no pair of primes is found, Goldbach's conjecture is not true for this number
    printf("%d cannot be expressed as the sum of two primes\n", num);
}
