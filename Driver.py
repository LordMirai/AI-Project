from search import run_search
from Node import Node
from tictactoe import TicTacToe
from game.test_pygame import Game

if __name__ != "__main__":
    print("Driver run from external context. terminated")
    exit(0)

print("Driver start.")

# n1 = Node(1)
# n2 = Node(2, n1)
# n3 = Node(3, n2)
# n4 = Node(4, n3)
# n5 = Node(5, n4)
# n6 = Node(6, n5)
#
#
# game = TicTacToe()
# game.play()

Game().start_game()
