from game import Game


def test_game():
    # Test 1 for game_move() function
    game = Game("simple.txt")
    move = "s"
    game.game_move(move)
    assert game.player.row == 1 and game.player.col == 1, "Test case 1 fail."
    print("Test case 1 for Game pass")

    # Test 2 for game_move() function
    game = Game("board_hard.txt")
    game.game_move("s")
    game.game_move("s")
    game.game_move("s")
    assert game.player.row == 3 and game.player.col == 1, "Test case 2 fail."
    print("Test case 2 for Game pass")

    # Test 3 for find_teleport function(Find if it can get the right position of X)
    game = Game("simple.txt")
    game.find_teleport(1, 2, 1)
    assert game.player.row == 1 and game.player.col == 4, "Test case 3 fail."
    print("Test case 3 for Game pass")

def run_tests():
    test_game()
    print()
