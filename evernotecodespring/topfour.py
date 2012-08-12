import sys

class heap:
	"""This class provides a max-heap implementaiton for integers"""
	data = [] # Holds the node data for the heap
	numElements = 0; # The number of entries in the heap

	##### Externally facing methods #####
	
	def __init__(self, initData = []):
		data = []
		numElements = 0
		self.constructFromData(initData)

	def sort(self, dataToSort):
		""" Sorts the list of integers in dataToSort and returns the sorted list """
		self.clear()
		self.constructFromData(dataToSort)
		sortedData = []

		while self.numElements > 0:
			sortedData.append(self.extractMin())

		return sortedData

	def clear(self):
		""" Deletes the contents of this heap """
		self.data = []
		self.numElements = 0

	def extractMax(self):
		""" Returns the minimum integer from and restructures the heap as needed """
		if self.numElements == 0:
			return None

		temp = self.data[0]
		if self.numElements == 1:
			self.clear()
			return temp

		# Put the last rightmost element on bottom level at root
		self.data[0] = self.data[self.numElements - 1]
		self.data.pop(self.numElements - 1)
		self.numElements -= 1
		index = 0

		# Let the new root bubble down as necessary
		while not self.isLeaf(index) and self.smallerThanChildren(index):
			# Find smallest child and swap places
			maxChildIndex = self.getMaxChildIndex(index)
			self.swap(index, maxChildIndex)
			index = maxChildIndex
			
		return temp


	def insert(self, num):
		""" Inserts num into the heap """
		self.data.append(num)
		index = self.numElements
		self.numElements += 1

		# Bubble new node up until it's larger than its parent
		while index > 0 and self.greaterThanParent(index):
			self.swap(index, self.parentIndexOf(index))
			index = self.parentIndexOf(index)

	def constructFromData(self, givenData):
		""" Constructs a min-heap from givenData """
		self.clear()
		for i in givenData:
			self.insert(i)

	##### Internally used functions #####

	def getMaxChildIndex(self, index):
		""" Returns the index of the smallest child of data[index] """
		leftChild = self.data[self.leftChildIndexOf(index)]
		
		if self.rightChildIndexOf(index) < self.numElements:
			rightChild = self.data[self.rightChildIndexOf(index)]
			if rightChild > leftChild:
				return self.rightChildIndexOf(index)

		return self.leftChildIndexOf(index)

	def greaterThanParent(self, index):
		""" Returns true if the node at index is greater than its parent node """
		if self.data[index] > self.data[self.parentIndexOf(index)]:
			return True;
		else:
			return False;

	def smallerThanChildren(self, index):
		""" Returns true if the node at index is greater than its children nodes """
		hasLeftChild = False;
		hasRightChild = False;
		if self.leftChildIndexOf(index) < self.numElements:
			hasLeftChild  = True
		if self.rightChildIndexOf(index) < self.numElements:
			hasRightChild = True

		if not hasLeftChild and not hasRightChild:
			return True
		elif hasLeftChild and not hasRightChild:
			return self.data[index] < self.data[self.leftChildIndexOf(index)]
		elif not hasLeftChild and hasRightChild:
			return self.data[index] < self.data[self.rightChildIndexOf(index)]
		else: # has both children
			return self.data[index] < self.data[self.leftChildIndexOf(index)] or self.data[index] < self.data[self.rightChildIndexOf(index)]

	def parentIndexOf(self, n):
		return (n - 1) / 2

	def leftChildIndexOf(self, n):
		return 2*n + 1

	def rightChildIndexOf(self, n):
		return 2*n + 2

	def isLeaf(self, index):
		""" Returns true if the node at index has a left child, and false otherwise """
		if self.leftChildIndexOf(index) >= self.numElements:
			return True
		else:
			return False

	def hasRightChild(self, index):
		""" Returns true if the node at index has a right child, and false otherwise """
		if self.rightChildIndexOf(index) < self.numElements:
			return True
		else:
			return False

	def swap(self, index1, index2):
		""" Swaps the integers at indices index1 and index2 """
		temp = self.data[index1]
		self.data[index1] = self.data[index2]
		self.data[index2] = temp

if __name__ == '__main__':
	numLines = int(raw_input())
	nums = []

	for i in range(0, numLines):
		nums.append(int(raw_input()))

	myHeap = heap()
	myHeap.constructFromData(nums)
	for i in range(0, 4):
		print myHeap.extractMax()
	