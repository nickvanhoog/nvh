#include <iostream>
#include <string>
#include <vector>
using namespace std;

// Calculates the user's desired 1-indexed Fibonacci number
int main() {
	int n = 0;
	string userInput = "";
	do {
		cout << "Enter which 1-indexed Fibonacci number you'd like: ";
		getline(cin, userInput);
		n = atoi(userInput.c_str());
		if(n <= 0) {
			cout << "Please enter a number greater than zero.\n";
		}
	} while(n <= 0);

	vector<int> fibos;
	fibos.push_back(0);
	fibos.push_back(1);

	if(n >= 3) {
		int currentFibIndex = 3;
		while(currentFibIndex <= n) {
			fibos.push_back(fibos[currentFibIndex - 2] + fibos[currentFibIndex - 3]);
			currentFibIndex++;
		}
		cout << fibos[fibos.size() - 1] << endl;
	}
	else {
		cout << fibos[n - 1] << endl;
	}
}