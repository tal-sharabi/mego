#include<stdio.h>
#include<stdlib.h>
#include<time.h>

// count dividers
int countDividers(int num) {

    int counter = 0, i;

    for (i = 1; i <= num / 2; i++)
        if (num % i == 0) // i is divider
            counter++; // count as divider

    return counter;

}

// display number with max dividers
void displayNumWithMaxDividers(int max) {

    int number, maxDividers = 0, maxNumber = 0, i;

    for (i = 1; i <= 10; i++) {

        number = rand() % (max)+1;
        printf("%d: %d\n", i, number);

        if (countDividers(number) > maxDividers) {
            maxNumber = number;
            maxDividers = countDividers(maxNumber);
        }

    }
    printf("\n\nnumber is: %d, dividers: %d \n\n", maxNumber, maxDividers);

}

void main() {

    srand(time(NULL)); // synch with clock

    displayNumWithMaxDividers(1000);

}

