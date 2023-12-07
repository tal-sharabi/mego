#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define SIZE 5

void main() {
    srand(time(NULL));

    int arr1[SIZE], i, number;

    for (i = 0; i < SIZE; i++) {
        arr1[i] = rand() % 10;
        number = arr1[i];
        printf("%d", number);

    }
    

}