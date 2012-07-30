import sys

class graph:
	""" A class to represent a graph. It can be weighted or unweighted, directed or undirected. """
	adjacencyLists = [] # Each entry i is an adjacency list for vertex i consisting of tuples (j, distance to j)
	weighted = False
	directed = False
	currentVertex = 0

	def __init__(self, w = False, d = False):
		self.adjacencyLists = []
		self.directed = d
		self.weighted = w
		self.currentVertex = 0

	def weighted(self):
		return self.weighted

	def directed(self):
		return self.directed

	def addVertex(self, adjList):
		""" Adds a vertex to the graph as represented by an adjacency list """
		self.adjacencyLists.append(adjList)

	def numConnections(self):
		""" Returns the total number of connections. If A is connected to B (undirected), it is counted twice """
		total = 0
		for a in self.adjacencyLists:
			total += len(a)
		return total

	def numVertices(self):
		""" Returns the total number of vertices in the graph """
		return len(adjacencyLists)

	def getNextVertex(self):
		""" Returns the adjacency list of the next iterated vertex """
		a = self.adjacencyLists[self.currentVertex]
		currentVertex += 1
		return a

	def clear(self):
		""" Clears all data from the graph and sets it to a default state """
		self.currentVertex = 0
		self.adjacencyLists = []
		self.directed = False
		self.weighted = False

	def output(self):
		for i in range(0, len(self.adjacencyLists)):
			print str(i) + ': ' + str(self.adjacencyLists[i])

if __name__ == '__main__':
	g = graph()
	g.addVertex([(1, 1), (4, 1)])
	g.addVertex([(0, 1), (2, 1), (4, 1)])
	g.output()	

