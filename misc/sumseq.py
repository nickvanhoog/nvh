import sys
from random import randint

def largestSequence(numbers):
	# numbers holds integers. This method finds the largest sum obtained by summing
	# consecutive elements in numbers and details the sum and the sequence that yielded it. 
	print numbers
	startIndex = 0
	endIndex = 0
	maxSum = -sys.maxint - 1 # Smallest possible integer in Python 2.x, 3.x seems to be different?
	listLength = len(numbers)
	currentSum = 0;

	for first in range(0, listLength):
		for last in range(first, listLength):
			currentSum = sum(numbers[first:last + 1])
			if currentSum > maxSum:
				maxSum = currentSum
				startIndex = first
				endIndex = last

	print 'Largest sum is ' + str(maxSum) + ' from ' + str(startIndex) + ' to ' + str(endIndex) + ', ' + str(numbers[startIndex:endIndex + 1])

if __name__ == '__main__':
	numbers = []
	# Generate random integers and pass them to largestSequence()
	for i in range(0, 10):
		numbers.append(randint(-10, 10))

	largestSequence(numbers)