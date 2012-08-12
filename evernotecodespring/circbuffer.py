import sys

class circularbuffer:
	maxSize = 0;
	size = 0;
	firstAdded = -1;
	lastAdded = -1;
	data = []

	def __init__(self, n):
		self.size = 0
		self.maxSize = n
		for i in range(0, n):
			self.data.append(None)

	def nextIndex(self):
		""" Gets the next index to insert at """
		if self.lastAdded == self.maxSize - 1:
			return 0

		return (self.lastAdded + 1)

	def append(self, line):
		""" Adds line to the buffer """
		if self.size == 0:
			self.data[0] = line
			self.lastAdded = 0
			self.firstAdded = 0
			self.size += 1;
		else:
			nextIndex = self.nextIndex()
			self.data[nextIndex] = line
			self.lastAdded = nextIndex
			if nextIndex == self.firstAdded:
				self.firstAdded += 1
				if self.firstAdded == self.maxSize:
					self.firstAdded = 0
			else:
				self.size += 1

	def remove(self, n):
		""" Removes the oldest n items from the buffer """
		for i in range(0, n):
			self.data[self.firstAdded] = None
			self.size -= 1
			if self.firstAdded == self.maxSize - 1:
				self.firstAdded = 0
			else:
				self.firstAdded += 1

	def list(self):
		""" Lists all of the items in the buffer from oldest to newest """
		current = self.firstAdded
		for i in range(0, self.size):
			print self.data[current]
			if current == self.maxSize - 1:
				current = 0
			else:
				current += 1

if __name__ == '__main__':
	bufferSize = raw_input()
	cb = circularbuffer(int(bufferSize))
	line = raw_input()
	while line != "Q":
		if line[0] == 'A':
			linesToAppend = int(line[2:len(line)])
			for i in range(0, linesToAppend):
				lta = raw_input()
				cb.append(lta)
		elif line[0] == 'R':
			linesToRemove = int(line[2:len(line)])
			cb.remove(linesToRemove)
		elif line[0] == 'L':
			cb.list()
		line = raw_input()