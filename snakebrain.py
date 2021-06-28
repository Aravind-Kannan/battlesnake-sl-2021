def get_next(current_head, direction):
    """
    :return the co-ordinate of head as per :param direction
    """
    future_head = current_head.copy()
    if direction == "left":
        future_head['x'] = current_head['x'] - 1
    if direction == "right":
        future_head['x'] = current_head['x'] + 1
    if direction == "up":
        future_head['y'] = current_head['y'] + 1
    if direction == "down":
        future_head['y'] = current_head['y'] - 1
    return future_head


def avoid_walls(future_head, height, width):
    result = True
    x = int(future_head["x"])
    y = int(future_head["y"])

    if x < 0 or y < 0 or x >= width or y >= height:
        result = False

    return result


def avoid_snakes(future_head, snake_bodies):
    for snake in snake_bodies:
        if future_head in snake["body"][:-1]:
            return False
    return True


def get_all_moves(coord):
    return [
        {'x': coord['x'], 'y': coord['y'] + 1},
        {'x': coord['x'], 'y': coord['y'] - 1},
        {'x': coord['x'] + 1, 'y': coord['y']},
        {'x': coord['x'] - 1, 'y': coord['y']}
    ]


def avoid_consumption(future_head, snake_bodies, my_snake):
    if len(snake_bodies) < 2:
        return True
    my_length = my_snake["length"]
    for snake in snake_bodies:
        if snake == my_snake:
            continue
        if future_head in get_all_moves(snake["head"]) and future_head not in snake["body"][1:-1] and \
                my_length <= snake["length"]:
            return False
    return True


def avoid_hazards(future_head, hazards):
    return future_head not in hazards


def at_wall(coord, board):
    return coord['x'] <= 0 or coord['y'] <= 0 or coord['x'] >= board['width'] - 1 or coord['y'] >= board['height'] - 1


def get_minimum_moves(start_coord, targets):
    moves = []
    for coord in targets:
        moves.append(abs(coord['x'] - start_coord['x']) + abs(coord['y'] - start_coord['y']))
    return moves


def get_safe_moves(possible_moves, body, board, squad_mates=None, my_snake=None):
    safe_moves = []

    for guess in possible_moves:
        guess_coord = get_next(body[0], guess)
        if avoid_walls(guess_coord, board["height"], board["width"]) and avoid_snakes(guess_coord, board["snakes"]):
            safe_moves.append(guess)
        elif len(body) > 1 and guess_coord == body[-1] and guess_coord not in body[:-1]:
            safe_moves.append(guess)
        # if squad_mates and my_snake:
        #     for snake in squad_mates:
        #         if guess_coord in snake["body"][1:] and guess_coord not in my_snake["body"][:-1]:
        #             safe_moves.append(guess)
    return safe_moves


def get_future_head_positions(body, turns, board):
    turn = 0
    explores = {}
    explores[0] = [body[0]]
    while turn < turns:
        turn += 1
        explores[turn] = []
        for explore in explores[turn - 1]:
            next_path = get_safe_moves(['left', 'right', 'up', 'down'], [explore], board)
            for path in next_path:
                explores[turn].append(get_next(explore, path))

    return explores[turns]


# def avoid_body(future_head, body):
#     if future_head in body:
#         return False
#     return True
#
#
# def getClosestEnemy(headCoord, snakes):
#     ans = []
#     li = []
#     for snake in snakes:
#         li.append(abs(snake["head"]["x"] - headCoord["head"]["x"]) + abs(snake["head"]["y"] - headCoord["head"]["y"]))
#     distance = min(li)
#     for snake in snakes:
#         if abs(snake["head"]["x"] - headCoord["head"]["x"]) + abs(
#                 snake["head"]["y"] - headCoord["head"]["y"]) == distance:
#             ans.append(snake)
#
#     return ans
#
#
