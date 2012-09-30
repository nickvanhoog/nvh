import sys

# Prints the 1-indexed nth Fibonacci number
def nthfibo(n):
	fibos = [0, 1]
	if n >= 3:
		currentFibIndex = 3
		while currentFibIndex <= n:
			fibos.append(fibos[currentFibIndex - 2] + fibos[currentFibIndex - 3])
			currentFibIndex += 1

		print fibos[len(fibos) - 1]
	else:
		print fibos[n - 1]

if __name__ == '__main__':
	if len(sys.argv) != 2 or int(sys.argv[1]) <= 0:
		print 'Invalid number of arguments: one positive integer argument required'
	else:
		nthfibo(int(sys.argv[1]))