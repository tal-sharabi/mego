#include <stdio.h>

void main() {
    int number, reversedNumber = 0, originalNumber, remainder;

    printf("Enter a number: ");
    scanf_s("%d", &number);

    originalNumber = number; // Store the original number

    while (number > 0) {
        remainder = number % 10;
        reversedNumber = reversedNumber * 10 + remainder;
        number /= 10;
    }

    if (originalNumber == reversedNumber) {
        printf("%d is a palindromic number.\n", originalNumber);
    }
    else {
        printf("%d is not a palindromic number.\n", originalNumber);
    }
}
