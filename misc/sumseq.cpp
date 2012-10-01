#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
using namespace std;

int sumArray(int* arr, int length) {
	int total = 0;
	for(int i = 0; i < length; i++) {
		total += arr[i];
	}
	return total;
}

int main() {
	// Generate numbers
	const int ARRAY_LENGTH = 10;
	int numbers[ARRAY_LENGTH];
	srand(time(NULL));
	int temp;
	cout << "[ ";
	for(int i = 0; i < ARRAY_LENGTH; i++) {
		temp = rand() % 10;
		temp % 2 == 0? numbers[i] = temp : numbers[i] = -1 * temp;
		cout << numbers[i];
		if(i < ARRAY_LENGTH - 1) {
			cout << ", ";
		}
	}
	cout << " ]\n";

	int first, last = 0;
	int startIndex, lastIndex = 0;
	int maxSum = INT_MIN;
	int currentSum = 0;

	for(first = 0; first < ARRAY_LENGTH; first++) {
		for(last = first + 1; last < ARRAY_LENGTH; last++) {
			currentSum = sumArray(numbers + first, last - first);
			if(currentSum > maxSum) {
				maxSum = currentSum;
				startIndex = first;
				lastIndex = last;
			}
		}
	}

	cout << "Largest sum is " << maxSum << " from " << startIndex << " to " << lastIndex << ", ";
	for(int i = startIndex; i <= lastIndex; i++) {
		cout << numbers[i];
		if (i < lastIndex) {
			cout << ", ";
		}
		else {
			cout << endl;
		}
	}
}