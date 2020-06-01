from grid import grid_to_string
from game_parser import read_lines
from player import Player


def test_grid():
    # Positive tests
    # 1.The first test case for grid_to_string function
    # 2.create one grid
    grid_one = read_lines("board_simple.txt")
    # 3.create one player
    player = Player(0, 2)
    # 4.test if grid_to_string function work fine
    assert grid_to_string(grid_one,
                          player) == "**A**\n*   *\n**Y**\n\nYou have 0 " \
                                     "water buckets.", "Test one did not pass"
    print("Test case 1 for Grid pass")

    # 5.The second test case for grid_to_string function
    # 6.create the second grid for testing
    grid_two = read_lines("board_medium.txt")
    # 7.creat one player
    player = Player(0, 2)
    # 8.test if grid_to_string function works fine
    assert grid_to_string(grid_two, player) == "**A***\n*    *\n* ** *\n*    *\n*    *\n" \
                                               "****Y*\n\nYou have 0 water buckets.", "Test t" \
                                                                                      "wo did not pass "
    print("Test case 2 for Grid pass")

    # The third test case for grid_to_string function
    grid_three = read_lines("board_normal.txt")
    player = Player(0, 2)
    assert grid_to_string(grid_three
                          , player) == "**A****\n*  " \
                                       "3  *\n* 3   *\n****Y**\n" \
                                       "\nYou have 0 water " \
                                       "buckets.", "Test three did not pass."
    print("Test case 3 for Grid pass")



def run_tests():
    test_grid()
    print()

