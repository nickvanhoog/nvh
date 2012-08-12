import sys
import heapq

if __name__ == '__main__':
	numTerms = int(raw_input())
	freqMap = {}

	for i in range(0, numTerms):
		line = raw_input()
		if freqMap.has_key(line):
			freqMap[line] += 1
		else:
			freqMap[line] = 1

	numFrequentTerms = int(raw_input())

	h = []
	for term in freqMap:
		heapq.heappush(h, (-1*freqMap[term], term))

	for i in range(0, numFrequentTerms):
		freq, term = heapq.heappop(h)
		print term