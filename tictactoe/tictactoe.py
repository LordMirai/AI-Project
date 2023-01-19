"""
Tic Tac Toe Player
"""

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


def count_empty(board):
    cnt = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                cnt += 1
    return cnt


def count_xo(board):
    x = 0
    o = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                o += 1
    return x, o


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x, o = count_xo(board)

    return O if x > o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    acts = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acts.add((i, j))
    return acts


def result(board: list, action: tuple[int, int]):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, column = action

    brd = copy.deepcopy(board)
    if action not in actions(brd):  # invalid action
        raise RuntimeError("Cell isn't empty.")
    brd[row][column] = player(brd)
    return brd


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:  # full row
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:  # full column
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:  # \
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:  # /
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    if count_empty(board) > 0:
        return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)

    if the_winner == X:
        return 1
    elif the_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        options = []

        for act in actions(board):
            options.append((minval(result(board, act)), act))
        options.sort(key=lambda x: x[0])
        options.reverse()  # so highest is first

        return options[0][1]

    if player(board) == O:
        options = []

        for act in actions(board):
            options.append([maxval(result(board, act)), act])
        options.sort(key=lambda x: x[0])

        return options[0][1]


def maxval(board):
    out = -999
    if terminal(board):
        return utility(board)
    for act in actions(board):
        out = max(out, minval(result(board, act)))
        return out


def minval(board):
    out = 999
    if terminal(board):
        return utility(board)
    for act in actions(board):
        out = min(out, maxval(result(board, act)))
        return out
