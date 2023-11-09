#include <stdio.h>

int reverseNumber(int num) {
    int reversed = 0;
    while (num > 0) {
        reversed = reversed * 10 + num % 10;
        num /= 10;
    }
    return reversed;
}

int main() {
    printf("Numbers that satisfy the property:\n");

    for (int number = 100; number <= 999; number++) {
        // Check if the number is a palindrome
        if (number / 100 != number % 10) {
            int reversed = reverseNumber(number);
            int difference = (number > reversed) ? (number - reversed) : (reversed - number);
            int sum = difference + reverseNumber(difference);

            if (sum == 1089) {
                printf("%d\n", number);
            }
        }
    }

    return 0;
}
