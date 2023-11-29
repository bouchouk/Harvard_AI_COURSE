"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    countx = 0
    counto = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                countx += 1
            elif board[i][j] == 'O':
                counto += 1
    if countx > counto:
        return 'O'
    else :
        return 'X'
                
            


def actions(board):
    possible_moves = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                possible_moves.add((i,j))
    return possible_moves
    


def result(board, action):
    if board[action[0]][action[1]] != None:
        raise Exception
    else:
        new_board = [row[:] for row in board]
        if player(board) == 'X':
            new_board[action[0]][action[1]] = 'X'
        else:
            new_board[action[0]][action[1]] = 'O'
    return new_board

def winner(board):
   for i in range(3):
       if board[i][0] != None and board[i][0] == board[i][1] and board[i][0] == board[i][2]:
           return board[i][0]
       elif board[0][i] != None and board[0][i] == board[1][i] and board[0][i] == board[2][i]:  
           return board[0][i]
   if board[0][0] != None and board[0][0] == board[1][1] and board[0][0] == board[2][2]:
       return board[1][1]
   elif board[2][0] != None and board[2][0] == board[1][1] and board[2][0] == board[0][2]:
       return board[1][1]
   return None

def terminal(board):
    if winner(board) != None:
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True
    


def utility(board):
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0

def max(board):
    if terminal(board) == True:
        return utility(board)
    else:
        score = -100
        for action in actions(board):
            score1 = min(result(board, action))
            if score < score1:
                score = score1
        return score

def min(board):
    if terminal(board) == True:
        return utility(board)
    else:
        score = 100
        for action in actions(board):
            score1 = max(result(board, action))
            if score > score1:
                score = score1
        return score

def minimax(board):
    if terminal(board) == True:
        return None
    else:
        my_action = None
        if player(board) == 'X':
            score = -2
            for action in actions(board):
                v = min(result(board, action))
                if v > score:
                    score = v 
                    my_action = action
            return my_action
        else:
            score = 2
            for action in actions(board):
                v = max(result(board, action))
                if v < score:
                    score = v
                    my_action = action
            return my_action