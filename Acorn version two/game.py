from game_parser import read_lines
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


class Game:
    def __init__(self, filename):
        self.filename = filename
        self.grid = read_lines(filename)
        self.row = 0
        self.col = 0
        self.find_x()
        self.player = Player(self.row, self.col)
        self.print_water = 0
        self.print_fire = 0
        self.print_live_fire = 0
        self.print_wall = 0
        self.print_magic = 0
        self.print_end_game = 0
        self.bad_input  = 0

    def game_move(self, move):
        """

            Args:
                move: the move we have made , which are "a,s,d,q,w,e"

            Returns:
                If we get the parameter-move,it will pass it to
                next_step() function,which will actually move the
                Acorn .

        """
        if move == "q":
            print()
            print("Bye!")
            exit()

        elif move.lower() == "e":
            self.next_step(move.lower())


        elif move.lower() == "a":
            self.next_step(move.lower())

        elif move.lower() == "s":
            self.next_step(move.lower())

        elif move.lower() == "w":
            self.next_step(move.lower())

        elif move.lower() == "d":
            self.next_step(move.lower())

        else:
            self.bad_input += 1


    def display(self):
        print(grid_to_string(self.grid, self.player))
        print()
        if self.print_water > 0:
            print("Thank the Honourable Furious Forest, you've found a bucket of water!")
            print()
            self.print_water = self.print_water - 1
        elif self.print_fire > 0:
            self.player.reverse_move()
            self.player.lose_game()

        elif self.print_live_fire > 0:
            print(
                "With your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!")
            print()
            self.print_live_fire -= 1
        elif self.print_wall > 0:

            print("You walked into a wall. Oof!")
            print()
            self.print_wall -= 1
        elif self.print_magic > 0:
            print("Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.")
            self.print_magic -= 1
            print()
        elif self.print_end_game > 0:
            if len(self.player.moves) == 1:
                print()
                print(
                    "You conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
                print()
                print("You made {} move.".format(len(self.player.moves)))
                print("Your move: {}".format(self.player.integration_moves()))
                print()
                print("=====================\n====== YOU WIN! =====\n=====================")
                exit()
            else:
                print()
                print(
                    "You conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.")
                print()
                print("You made {} moves.".format(len(self.player.moves)))
                print("Your moves: {}".format(self.player.integration_moves()))
                print()
                print("=====================\n====== YOU WIN! =====\n=====================")
                exit()
        elif self.bad_input > 0:
            print("Please enter a valid move (w, a, s, d, e, q).")
            print()
            self.bad_input -= 1

    def find_x(self):
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[i]):
                if self.grid[i][j].display == "X":
                    self.row = i
                    self.col = j
                    break

                j = j + 1
            i = i + 1

    def next_step(self, move):
        """
        
        Args:
            move: The move we made which are "a,s,d,q,w,e"

        Returns:
            nothing, but it can change the acorn's coordinate, when
            the acorn pass the water, fire or teleport, it will print
            the corresponding information. 

        """
        start = Start()
        end = End()
        air = Air()
        wall = Wall()
        fire = Fire()
        water = Water()

        if move == "w":
            x = -1
            y = 0

        elif move == "s":
            x = 1
            y = 0

        elif move == "a":
            x = 0
            y = -1

        elif move == "d":
            x = 0
            y = 1

        elif move == "e":
            x = 0
            y = 0

            if self.grid[self.player.row][self.player.col].display == "1":
                self.find_teleport(1, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "2":
                self.find_teleport(2, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "3":
                self.find_teleport(3, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "4":
                self.find_teleport(4, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "5":
                self.find_teleport(5, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "6":
                self.find_teleport(6, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "7":
                self.find_teleport(7, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "8":
                self.find_teleport(8, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "9":
                self.find_teleport(9, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
            elif self.grid[self.player.row][self.player.col].display == "0":
                self.find_teleport(0, self.player.row, self.player.col)
                self.print_magic += 1
                self.player.move(move)
                return
        if type(self.grid[self.player.row + x][self.player.col + y]) == type(water):

            self.player.num_water_buckets = self.player.num_water_buckets + 1
            self.print_water += 1
            self.player.col = self.player.col + y
            self.player.row = self.player.row + x
            self.grid[self.player.row][self.player.col] = air

            self.player.move(move)


        elif type(self.grid[self.player.row + x][self.player.col + y]) == type(fire):
            self.player.num_water_buckets = self.player.num_water_buckets - 1
            if self.player.num_water_buckets < 0:
                self.player.move(move)
                self.print_fire += 1
                self.player.num_water_buckets = 0
            else:
                self.print_live_fire += 1
            self.player.col = self.player.col + y
            self.player.row = self.player.row + x
            self.grid[self.player.row][self.player.col] = air
            self.player.move(move)

        elif self.grid[self.player.row + x][self.player.col + y].display == "1":

            self.print_magic += 1
            self.find_teleport(1, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "2":
            self.print_magic += 1
            self.find_teleport(2, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "3":
            self.print_magic += 1
            self.find_teleport(3, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "4":
            self.print_magic += 1
            self.find_teleport(4, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "5":
            self.print_magic += 1
            self.find_teleport(5, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "6":
            self.print_magic += 1
            self.find_teleport(6, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "7":
            self.print_magic += 1
            self.find_teleport(7, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "8":
            self.print_magic += 1
            self.find_teleport(8, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "9":
            self.print_magic += 1
            self.find_teleport(9, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif self.grid[self.player.row + x][self.player.col + y].display == "0":
            self.print_magic += 1
            self.find_teleport(0, self.player.row + x, self.player.col + y)
            self.player.move(move)
        elif type(self.grid[self.player.row + x][self.player.col + y]) == type(air):
            self.player.move(move)
            self.player.row = self.player.row + x
            self.player.col = self.player.col + y

        elif type(self.grid[self.player.row + x][self.player.col + y]) == type(wall):
            self.print_wall += 1
        elif type(self.grid[self.player.row + x][self.player.col + y]) == type(end):
            self.player.row = self.player.row + x
            self.player.col = self.player.col + y
            self.player.move(move)
            self.print_end_game += 1
        elif type(self.grid[self.player.row + x][self.player.col + y]) == type(start):
            self.player.row = self.player.row + x
            self.player.col = self.player.col + y
            self.player.move(move)
        else:
            pass

    def find_teleport(self, telestring, row, col):
        """

        Args:
            telestring:the number of the teleport
            row:the x-coordinate of the teleport
            col:the y-coordinate of the teleport

        Returns:

        """
        i = 0
        while i < len(self.grid):
            j = 0
            while j < len(self.grid[i]):
                if self.grid[i][j].display == str(telestring):
                    if i == row and j == col:
                        pass
                    else:
                        self.player.row = i
                        self.player.col = j

                        break

                j = j + 1
            i = i + 1

















































