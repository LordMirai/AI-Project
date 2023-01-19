
class TicTacToe:

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player = 'X'
        self.winner = None

        self.used = []

        self.states = []

    def __str__(self):
        s = ''
        for row in self.board:
            s += '|'.join(row)+"\n"
        return s

    def play(self):
        while self.winner is None:
            print(self)
            self.get_move()
            self.find_terminal()
            self.switch_player()
        print(self)
        print(self.winner, "wins!")

    def get_move(self):
        while True:
            print(self.player, "'s turn")
            move = input("Enter row,col: ")
            if move == "act":
                print(self.find_actions())
                continue
            row, col = move.split(',')
            row = int(row)
            col = int(col)
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move")
                continue
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player
                self.used.append((row, col))
                self.states.append(self.board)  
            else:
                print("That square is already taken")

    def find_terminal(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                self.winner = row[0]
                return
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                self.winner = self.board[0][col]
                return
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            self.winner = self.board[0][2]
            return

    def switch_player(self):
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def find_actions(self):
        act = []
        for i in range(3):
            for j in range(3):
                if not (i, j) in self.used:
                    act.append((i, j))
        return act

    def get_value(self):
        if self.find_terminal() is None:
            return 0
        if self.winner == 'X':
            return 1
        if self.winner == 'O':
            return -1

    def max_value(self):
        if self.find_terminal() is not None:
            return self.get_value()
        v = -999
        for a in self.find_actions():
            self.board[a[0]][a[1]] = 'X'
            v = max(v, self.minvalue())
            self.board[a[0]][a[1]] = ' '
        return v

    def min_value(self):
        if self.find_terminal() is not None:
            return self.get_value()
        v = 999
        for a in self.find_actions():
            self.board[a[0]][a[1]] = 'O'
            v = min(v, self.maxvalue())
            self.board[a[0]][a[1]] = ' '
        return v
