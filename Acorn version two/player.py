class Player:
    def __init__(self, row, col):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = row
        self.col = col
        self.moves = []

    def move(self, move):
        # get the parameter "move" to store moves

        self.moves.append(move)

    def reverse_move(self):
        # delete the move , because the acorn bumps into the wall
        self.moves.pop()

    def integration_moves(self):
        # transform moves(lists) to strings
        return ", ".join(self.moves)

    def quit_game(self):
        # use this function to quit this game
        print("Bye!")
        exit()

    def lose_game(self):
        #  if we lose the game, then call this function
        print()
        print("You step into the fires and watch your dreams disappear :(.")
        print()
        print("The Fire Nation triumphs! The Honourable Furious Fore"
              "st is reduced to a pile of ash and is scattered to the "
              "winds by the next storm... You have been roasted.")
        print()
        print("You made {} moves.".format(len(self.moves)))
        print("Your moves: {}".format(self.integration_moves()))
        print()
        print("=====================\n===== GAME OVER =====\n=="
              "===================")
        exit()

