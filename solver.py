import sys
from game_parser import read_lines
from game import Game
from run import search_coords


def left(coords):
    return [coords[0], coords[1] - 1]


def down(coords):
    return [coords[0] + 1, coords[1]]


def right(coords):
    return [coords[0], coords[1] + 1]


def up(coords):
    return [coords[0] - 1, coords[1]]


def coords_sub(coords_one, coords_two):
    row = coords_one[0] - coords_two[0]
    col = coords_one[1] - coords_two[1]
    return row, col


def teleport_pair(coords, game_coords):
    item = search_coords(game_coords, coords)   # 猜测search_coords返回的是某个cell具体的字符串
    if item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        for value in game_coords[item]:
            if value != coords:
                return value
    return -1


def dfs(game, game_coords):
    stack_moves = [[game.player.row, game.player.col]]
    declined_moves = []
    action_map = {1: 'a', 2: 's', -1: 'd', -2: 'w', 3: 'e'}
    route = []
    met_fire = False

    while stack_moves[-1] != game_coords['Y'][0]:
        go_back = False
        if not stack_moves:
            return 0, 0, 0

        if len(route) > 3 and route[-1] == 3 and route[-2] == 3 and route[-3] == 3:
            return 0, 0, 0

        player_coords = [game.player.row, game.player.col]

        if left(player_coords) not in stack_moves and left(player_coords) not in declined_moves:
            will_move = left(player_coords)
            action = 1
        elif down(player_coords) not in stack_moves and down(player_coords) not in declined_moves:
            will_move = down(player_coords)
            action = 2
        elif right(player_coords) not in stack_moves and right(player_coords) not in declined_moves:
            will_move = right(player_coords)
            action = -1
        elif up(player_coords) not in stack_moves and up(player_coords) not in declined_moves:
            will_move = up(player_coords)
            action = -2
        elif search_coords(game_coords, stack_moves[-1]) in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            action = 3
            will_move = stack_moves[-1]

        else:
            declined_moves.append(stack_moves[len(stack_moves)-1])
            stack_moves.pop()
            if not stack_moves:
                return 0, 0, 0
            will_move = stack_moves[-1]
            action = -route[-1]
            go_back = True

        item = search_coords(game_coords, will_move)

        if item == '*' or item == -1:
            declined_moves.append(will_move)
            continue

        elif item == 'W':
            game.player.num_water_buckets += 1
            if met_fire:
                stack_moves = []
                declined_moves = []
            met_fire = False

            for i in range(len(game_coords['W'])):
                if game_coords['W'][i] == will_move:
                    game_coords['W'].pop(i)
                    game_coords[' '].append(will_move)
                    break

        elif item == 'F':
            if game.player.num_water_buckets < 1:
                declined_moves.append(will_move)
                met_fire = True
                continue
            game.player.num_water_buckets -= 1
        elif item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            for coords in game_coords[item]:
                if coords != will_move:
                    will_move = coords
                    break

        if not go_back:
            stack_moves.append(will_move)

        # # *** move the player ***
        game.player.row = will_move[0]
        game.player.col = will_move[1]

        route.append(action)

    trace = ''
    for action in route:
        trace += action_map[action] + ', '

    return 1, len(route), trace


def bfs(game, game_coords):

    queue_moves = [[game.player.row, game.player.col]]
    last_steps = [[game.player.row, game.player.col]]
    cost_moves = [0]
    declined_moves = []
    cost = 1

    while queue_moves[-1] != game_coords['Y'][0]:
        if not last_steps:
            return 0, 0, 0

        potential_steps = []
        for step in last_steps:
            potential_steps.append(left(step))
            potential_steps.append(down(step))
            potential_steps.append(right(step))
            potential_steps.append(up(step))

            if search_coords(game_coords, step) in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                potential_steps.append(step)

        current_steps = []
        for step in potential_steps:
            if step in declined_moves:
                continue
            elif step in queue_moves:
                if cost >= cost_moves[queue_moves.index(step)]:
                    if step != queue_moves[-1]:
                        continue

            will_move = step
            item = search_coords(game_coords, will_move)

            if item == '*' or item == -1:
                declined_moves.append(will_move)
                continue

            elif item == 'W':
                game.player.num_water_buckets += 1

                for i in range(len(game_coords['W'])):
                    if game_coords['W'][i] == will_move:
                        game_coords['W'].pop(i)
                        game_coords[' '].append(will_move)
                        break

            elif item == 'F':
                if game.player.num_water_buckets < 1:
                    declined_moves.append(will_move)
                    continue
                game.player.num_water_buckets -= 1
            elif item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                for coords in game_coords[item]:
                    if coords != will_move:
                        will_move = coords
                        break

            current_steps.append(will_move)
            queue_moves.append(will_move)
            cost_moves.append(cost)

            if will_move == game_coords['Y'][0]:
                break

        last_steps = []
        last_steps.extend(current_steps)
        cost += 1

    cost -= 1

    route = []
    action_map = {(1, 0): 'w', (-1, 0): 's', (0, 1): 'a', (0, -1): 'd'}
    recall_moves = queue_moves[::-1]
    recall_cost = cost_moves[::-1]
    cursor = recall_moves[0]

    for i in range(len(recall_moves)):
        if recall_cost[i] == cost - 1:

            x, y = coords_sub(recall_moves[i], cursor)
            if abs(x) + abs(y) == 1:
                cursor = recall_moves[i]
                cost -= 1
                route.insert(0, action_map[(x, y)])

            elif teleport_pair(cursor, game_coords) != -1:
                pair = teleport_pair(cursor, game_coords)

                x, y = coords_sub(recall_moves[i], pair)
                if abs(x) + abs(y) == 1:
                    cursor = recall_moves[i]
                    cost -= 1
                    route.insert(0, action_map[(x, y)])
                elif abs(x) + abs(y) == 0:
                    cursor = recall_moves[i]
                    cost -= 1
                    route.insert(0, 'e')

    trace = ''
    for action in route:
        trace += action + ', '

    return 1, cost_moves[-1], trace


def main():
    file = sys.argv[1]
    game = Game(file)

    grid = read_lines(file)
    game_coords = game.collect_coords(grid)

    game.player.row = game_coords['X'][0][0]
    game.player.col = game_coords['X'][0][1]

    if sys.argv[2] == "DFS":
        result, count, trace = dfs(game, game_coords)
    elif sys.argv[2] == "BFS":
        result, count, trace = bfs(game, game_coords)

    return result, count, trace


if __name__ == "__main__":
    solution_found = False
    result, count, trace = main()

    if result == 1:
        solution_found = True

    if solution_found:
        print("Path has " + str(count) + " moves.")
        print("Path: " + trace[:-2])
    else:
        print("There is no possible path.")