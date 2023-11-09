//Whole numbers must be received repeatedly until the number 0 is received.
//The sum of the numbers received, how many numbers were received
//and their average must be output.
#include <stdio.h>
void main() {
	int score = 1, i=-1, sum_all_scores = 0;
	float average;
	printf("Write all your grades and then 0: \n");
	while (score != 0) {
		printf("Enter your grade: ");

		scanf_s("%d", &score);
		sum_all_scores += score;
		i++;
	}
	average = (float)sum_all_scores / i;
	printf("you have %d scores, your average is %.2f\n", i, average);

}