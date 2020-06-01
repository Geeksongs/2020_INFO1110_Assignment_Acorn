import emoji
def grid_to_string(grid, player):
    """Turns a grid and player into a string grid -- list of list of Cells
        player -- a Player with water buckets

    Arguments:


    Returns:
        string: A string representation of the grid and player.
    """

    grid_two = [[0] * len(grid[1]) for i in range(len(grid))]

    i = 0
    while i < len(grid):
        j = 0

        while j < len(grid[i]):
            if grid[i][j] == "A":
                player.row = i
                player.col = j

            elif grid[i][j].display == "Y":
                grid_two[i][j] = "Y"
            elif grid[i][j].display == "X":
                grid_two[i][j] = "X"
            elif grid[i][j].display == " ":
                grid_two[i][j] = " "
            elif grid[i][j].display == "*":
                grid_two[i][j] = "*"
            elif grid[i][j].display == "F":
                grid_two[i][j] = "F"
            elif grid[i][j].display == "W":
                grid_two[i][j] = "W"
            elif grid[i][j].display == "1":
                grid_two[i][j] = "1"
            elif grid[i][j].display == "2":
                grid_two[i][j] = "2"
            elif grid[i][j].display == "3":
                grid_two[i][j] = "3"
            elif grid[i][j].display == "4":
                grid_two[i][j] = "4"
            elif grid[i][j].display == "5":
                grid_two[i][j] = "5"
            elif grid[i][j].display == "6":
                grid_two[i][j] = "6"
            elif grid[i][j].display == "7":
                grid_two[i][j] = "7"
            elif grid[i][j].display == "8":
                grid_two[i][j] = "8"
            elif grid[i][j].display == "9":
                grid_two[i][j] = "9"
            elif grid[i][j].display == "0":
                grid_two[i][j] = "0"
            j = j + 1
        i = i + 1
    grid_two[player.row][player.col] = "A"

    string = ''
    i = 0
    while i < len(grid):

        string = string + "".join(str(v) for v in grid_two[i])
        string = string + "\n"
        i = i + 1
    if player.num_water_buckets == 1:
        string = string + "\n" + "You have {} water buckets.".format(player.num_water_buckets)
    else:
        string = string + "\n" + "You have {} water buckets.".format(player.num_water_buckets)
    return emoji.emojize(string)
