#!/bin/python
import random
import operator

# Complete the function below to print 2 integers separated by a single space which will be your next move 
# Refer section <i>Output format</i> for more details
def nextMove(player,board):
	opponent = ''
	wentFirst = False
	if player == 'X':
		wentFirst = True
		opponent = 'O'
	else:
		opponent = 'X'

	myPositions = []
	oppPositions = []

	for i in range(0, 3):
		for j in range(0, 3):
			if board[i][j] == player:
				myPositions.append((i, j))
			elif board[i][j] == opponent:
				oppPositions.append((i, j))

	# First turn, take a corner
	if len(myPositions) + len(oppPositions) == 0:
		print '0 0'
		return
	# The opponent made the first move and this is our first response.
	elif len(myPositions) + len(oppPositions) == 1:
		if oppPositions[0] == (1, 1):
			print '0 0'
			return
		else:
			print '1 1'
			return
	else:
		# Any immediate threats/win opportunities? If so, try and block/win
		# Check horizontal and vertical 2 in a row
		for i in range(0, 3):
			# Check row i
			if (board[i].count(player) == 2 and board[i].count(opponent) == 0) or (board[i].count(opponent) == 2 and board[i].count(player) == 0):
				for j in range(0, 3):
					if board[i][j] == '_':
						print str(i) + ' ' + str(j)
						return
			
			# Now check column i
			column = []
			for j in range(0, 3):
				column.append(board[j][i])
			# column now contains column i
			if (column.count(player) == 2 and column.count(opponent) == 0) or (column.count(opponent) == 2 and column.count(player) == 0):
				print str(operator.indexOf(column, '_')) + ' ' + str(i)
				return
			
		#Check for diagonal 2 in a row, both the opponent and me:
		diag = [ board[0][0], board[1][1], board[2][2] ]
		if (diag.count(player) == 2 and diag.count(opponent) == 0) or (diag.count(opponent) == 2 and diag.count(player) == 0):
			if operator.indexOf(diag, '_') == 0:
				print '0 0'
				return
			elif operator.indexOf(diag, '_') == 1:
				print '1 1'
				return
			else:
				print '2 2'
				return
		diag = [ board[2][0], board[1][1], board[0][2] ]
		if (diag.count(player) == 2 and diag.count(opponent) == 0) or (diag.count(opponent) == 2 and diag.count(player) == 0):
			if operator.indexOf(diag, '_') == 0:
				print '2 0'
				return
			elif operator.indexOf(diag, '_') == 1:
				print '1 1'
				return
			else:
				print '0 2'
				return

		#Check if opponent has two opposite corners (and no two in a row horizontally / vertically) and place in middle side spot if possible
		if (board[0][0] == opponent and board[2][2] == opponent) or (board[2][0] == opponent and board[0][2] == opponent):
			if board[1][1] == '_':
				print '1 1'
				return
			else:
				# Find a spot next to the corners that's open
				if board[0][1] == '_':
					print '0 1'
					return
				elif board[1][0] == '_':
					print '1 0'
					return
				elif board[1][2] == '_':
					print '1 2'
					return
				elif board[2][1] == '_':
					print '2 1'
					return

		# If we've gotten here, the opponent does not have two in a row and they also aren't on the corners, pick a random spot
		for i in range(0, 3):
			for j in range(0, 3):
				if board[i][j] == '_':
					print str(i) + ' ' + str(j)
					return
	 

#If player is X, I'm the first player.
#If player is O, I'm the second player.
player = raw_input()

#Read the board now. The board is a 3x3 array filled with X, O or _.
board = []
for i in xrange(0, 3):
    board.append(raw_input())

nextMove(player,board);  
