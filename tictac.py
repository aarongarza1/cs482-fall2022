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
    
        # Checking for Rows for X or O victory.
        for row in range(3) :    
            if (self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]) :       
                if (self.board[row][0] == self.player) :
                    return 1
                elif (self.board[row][0] == -self.player) :
                    return -1
    
        # Checking for Columns for X or O victory.
        for col in range(3) :
        
            if (self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]) :
            
                if (self.board[0][col] == self.player) :
                    return 1
                elif (self.board[0][col] == -self.player) :
                    return -1
    
        # Checking for Diagonals for X or O victory.
        if (self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]) :
        
            if (self.board[0][0] == self.player) :
                return 1
            elif (self.board[0][0] == -self.player) :
                return -1
    
        if (self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]) :
        
            if (self.board[0][2] == self.player) :
                return 1
            elif (self.board[0][2] == -self.player) :
                return -1
    
        return 0
    def isMovesLeft(self) :
    
        for i in range(3) :
            for j in range(3) :
                if (self.board[i][j] == 0) :
                    return True
        return False
    def play_game(self):
        bestVal = -1000
        bestMove = (-1, -1)
        earlyWin = 0 
        while(self.eval_win() != 1):
            for i in range(3) :   
                
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self.board[i][j] == 0) :
                    
                        # Make the move
                        self.board[i][j] = self.player
                        earlyWin = self.eval_win()
                        if(earlyWin == 1):
                            break
                        # compute evaluation function for this
                        # move.
                        moveVal = self.minimax(0, False)
        
                        # Undo the move
                        self.board[i][j] = 0
        
                        # If the value of the current move is
                        # more than the best value, then update
                        # best/
                        if (moveVal > bestVal) :               
                            bestMove = (i, j)
                            bestVal = moveVal
                if(earlyWin == 1):
                    break
    
        self.board[bestMove[0]][bestMove[1]] = self.player
        return self.board, self.eval_win()

    def minimax(self, depth, isMax) :
        score = self.eval_win()
    
        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 1) :
            return score
    
        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == -1) :
            return score
    
        # If there are no more moves and no winner then
        # it is a tie
        if (self.isMovesLeft() == False) :
            return 0
    
        # If this maximizer's move
        if (isMax) :    
            best = -1000
    
            # Traverse all cells
            for i in range(3) :        
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self.board[i][j]==0) :
                    
                        # Make the move
                        self.board[i][j] = self.player
    
                        # Call minimax recursively and choose
                        # the maximum value
                        best = max( best, self.minimax(
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
                        self.board[i][j] = -self.player
    
                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, self.minimax(depth + 1, not isMax))
    
                        # Undo the move
                        self.board[i][j] = 0
            return best


def load_board( filename ):
    return np.loadtxt( filename)

# def save_board( self, filename ):
#         np.savetxt( filename, self.board, fmt='%d')

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