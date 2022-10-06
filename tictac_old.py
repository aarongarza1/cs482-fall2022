#!/usr/bin/python3

from dataclasses import dataclass
import numpy as np
import argparse

class TicTacToe:
	def __init__(self, board=None, player=1) -> None:
		if board is None:
			self.board = self.init_board()
		else:
			self.board = board
		self.player = player

	def init_board(self):
		return np.array([[0,0,0],[0,0,0],[0,0,0]])

	def print_board(self):
		print (self.board)

	def eval_win(self):
		for i in range(0, 3):
			if (self.board[0][i] != 0 and self.board[1][i] == self.board[0][i] and self.board[2][i] == self.board[0][i]):
				return 1 if self.board[0, i] == 1 else -1
		for i in range(0, 3):
			if (self.board[i][0] == 1 and self.board[i][1] == 1 and self.board[i][2] == 1):
				return 1
			elif (self.board[i][0] == -1 and self.board[i][1] == -1 and self.board[i][2] == -1):
				return -1

		if (self.board[0][0] != 0 and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]):
			return 1 if self.board[0][0] == 1 else -1

		if (self.board[0][2] != 0 and self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]):
			return 1 if self.board[0][2] == 1 else -1


		
		return 0

	def play_game(self):
		best_move_found = False
		bestVal = -1000
		bestMove = (-1, -1)
		result = -2
		while(result != None and result != 1 and result != -1):
			for i in range (0, 3):
				for j in range(0, 3):
					if (self.board[i][j] == 0 and self.board[i][j] != 1 and self.board[i][j] != -1) :
						# Make the move
						self.board[i][j] = self.player
			
						# compute evaluation function for this
						# move.
						moveVal = self.minimax(0, False)
			
						# Undo the move
						self.board[i][j] = 0							# If the value of the current move is
						# more than the best value, then update
						# best/
						if (moveVal > bestVal):               
							bestMove = (i, j) 
							bestVal = moveVal

			if(self.player == 1):
				self.board[bestMove] = 1
			#	print("1's move")
				print(bestMove)
			if(self.player == -1):
				self.board[bestMove] = -1
			#	print("-1's move")
				print(bestMove)
			# self.print_board()
			self.player = -1 if self.player == 1 else 1
			result = self.eval_win()
			self.print_board()
			# print(result)


		return self.board, self.eval_win()
	def minimax(self, depth, isMax) :
		result = self.eval_win()

		if (result == 1) :
		#	print("Result 1")
			return 1 if self.player == 1 else -1
			

		if (result == -1) :
		#	print("Result -1")
			return -1 if self.player == -1 else 1
			
	
		if (movesPossible(self.board) == False) :
			return 0
			

		# If this maximizer's move
		if (isMax) :    
			best = -1000
	
			# Traverse all cells
			for i in range(3) :        
				for j in range(3) :
				
					# Check if cell is empty
					if (self.board[i][j] == 0) :
						# Make the move
						self.board[i][j] = self.player
	
						# Call minimax recursively and choose
						# the maximum value
						best = max(best, self.minimax(
												depth + 1,
												not isMax) )
	
						# Undo the move
						self.board[i][j] = 0
			return best
	
		# If this minimizer's move
		else :
			best = 1000
	
			# Traverse all cells
			for i in range(3) :        
				for j in range(3) :
				
					# Check if cell is empty
					if (self.board[i][j] == 0) :
					
						# Make the move
						self.board[i][j] = 1 if self.player == -1 else 1
	
						# Call minimax recursively and choose
						# the minimum value
						best = min(best, self.minimax(depth + 1, not isMax))
	
						# Undo the move
						self.board[i][j] = 0
			return best


def movesPossible(board) :
 
    for i in range(0, 3) :
        for j in range(0, 3) :
            if (board[i][j] == 0) :
                return True
    return False
def load_board( filename ):
	return np.loadtxt( filename)

# def save_board( self, filename ):
# 	np.savetxt( filename, self.board, fmt='%d')

def main():
	parser = argparse.ArgumentParser(description='Play tic tac toe')
	parser.add_argument('-f', '--file', default=None, type=str ,help='load board from file')
	parser.add_argument('-p', '--player', default=1, type=int, choices=[1,-1] ,help='player that playes first, 1 or -1')
	args = parser.parse_args()

	board = load_board(args.file) if args.file else None
	testcase = np.array([[1,0,0],
                             [-1,1,0],
                             [-1,0,0]])
	ttt = TicTacToe(testcase, args.player)
	# ttt.print_board()
	b,p = ttt.play_game()
	print("final board: \n{}".format(b))
	print("winner: player {}".format(p))

if __name__ == '__main__':
	main()