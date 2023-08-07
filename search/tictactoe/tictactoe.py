"""
Tic Tac Toe Player
"""

import math
import copy

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
    """
    Returns player who has the next turn on a board.
    determine which person go first
    """
    X_count , O_count = 0 , 0
    for i in board:
        for j in i:
            X_count += (j == X)
            O_count += (j == O)
    return X if X_count == O_count else O



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    ans = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                ans.append((i,j))
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    cur = player(board)
    i , j = action
    if board[i][j] != EMPTY:
        raise Exception("infeasible move")
    new_board[i][j] = cur
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[2][0] == board[1][1] == board[0][2]) and board[2][0] != EMPTY:
        return board[2][0]

    return  None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def ma(board):
    if terminal(board):
        return utility(board)
    v = -10
    for action in actions(board):
        v = max(v , mi(result(board , action)))
    return v

def mi(board):
    if terminal(board):
        return utility(board)
    v = 10
    for action in actions(board):
        v = min(v , ma(result(board , action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    a = actions(board)
    turn = player(board)
    v = []
    if turn == X:
        for move in a:
            v.append(mi(result(board , move)))
        a.sort()
        return a[-1]
    if turn == O:
        for move in a:
            v.append(ma(result(board , move)))
        a.sort()
        return a[0]

