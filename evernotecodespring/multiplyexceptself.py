import sys

if __name__ == '__main__':
	data = []
	numItems = int(raw_input())
	numZeros = 0
	runningProduct = long(1)

	for i in range(0, numItems):
		currentNum = long(raw_input())
		if currentNum != 0:
			runningProduct *= currentNum
		else:
			numZeros += 1
		data.append(currentNum)

	for i in range(0, numItems):
		if numZeros > 1 or (numZeros == 1 and data[i] != 0):
			print 0
		elif data[i] == 0:
			print runningProduct
		else:
			print runningProduct / data[i]

	sys.exit()
