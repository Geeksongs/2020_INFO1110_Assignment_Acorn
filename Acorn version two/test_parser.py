from game_parser import parse

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def test_parse():
    # The first test case,both are positive tests
    wall = Wall()
    start = Start()
    end = End()
    teleplort = Teleport(2)
    f = open("wall.txt", "r")
    line = f.readlines()  # get the string gird,put it in the the parse function
    f.close()
    new_grid = parse(line)
    i = 0
    count = 0
    maxnumber = len(new_grid) * len(new_grid[0])
    if type(new_grid[0][0]) == type(wall):
        count += 1
    if type(new_grid[0][1]) == type(start):
        count += 1
    if type(new_grid[0][2]) == type(wall):
        count += 1
    if type(new_grid[1][0]) == type(wall):
        count += 1
    if type(new_grid[1][1]) == type(end):
        count += 1
    if type(new_grid[1][2]) == type(wall):
        count += 1
    assert maxnumber == count, "Test case 1 did not pass"
    print("Test case 1 for Parse pass")

    # The second test case ,edge test case
    f = open("board_hard.txt", "r")
    line = f.readlines()
    f.close()
    grid_two = parse(line)
    assert isinstance(grid_two[0][0], type(wall)) and isinstance(grid_two[5][3], type(teleplort)) == True, \
        "Test case 2 did not pass"
    print("Test case 2 for Parse pass")


def run_tests():
    test_parse()
    print()



