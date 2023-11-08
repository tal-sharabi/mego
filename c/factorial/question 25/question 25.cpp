#include <stdio.h>

void factorial(int num);

void main() {
    int num;

    printf("Enter a number please: ");
    scanf_s("%d", &num);

    factorial(num);
}

void factorial(int num) {
    int fact = 1;

    for (int i = 1; i <= num; i++) {
        fact = fact * i;
    }
    if (fact > 0) {
        printf("The factorial value is %d\n", fact);
    }
    else {
        printf("invalid number");
    }
}
