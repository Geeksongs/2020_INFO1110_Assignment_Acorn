from game import Game
import os
import sys

# Your code...
if os.path.exists("board_hard.txt"):
    pass
else:
    print("{} does not exist!".format("board_hard.txt"))
    exit()

game = Game("board_hard.txt")
game.display()
move = input("Input a move: ")

while True:


    game.game_move(move)
    game.display()
    print()
    move = input("Input a move: ")









