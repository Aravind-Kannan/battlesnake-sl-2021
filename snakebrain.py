def getNext(current_head, direction):
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


def avoid_snakes(future_head, snakeBodies):
    for snake in snakeBodies:
        if future_head in snake["body"][:-1]:
            return False
    return True


def get_safe_moves(possible_moves, body, board, squadMates=None, mySnake=None):
    safe_moves = []

    for guess in possible_moves:
        guess_coord = getNext(body[0], guess)
        if avoid_walls(guess_coord, board["height"], board["width"]) and avoid_snakes(guess_coord, board["snakes"]):
            safe_moves.append(guess)
        elif len(body) > 1 and guess_coord == body[-1] and guess_coord not in body[:-1]:
            safe_moves.append(guess)
        # if squadMates and mySnake:
        #     for snake in squadMates:
        #         if guess_coord in snake["body"][1:] and guess_coord not in mySnake["body"][:-1]:
        #             safe_moves.append(guess)
    return safe_moves


# def avoid_body(future_head, body):
#     if future_head in body:
#         return False
#     return True
#
#
# def avoidHazards(future_head, hazards):
#     return future_head not in hazards
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
# def getAllMoves(coord):
#     return [
#         {'x': coord['x'], 'y': coord['y'] + 1},
#         {'x': coord['x'], 'y': coord['y'] - 1},
#         {'x': coord['x'] + 1, 'y': coord['y']},
#         {'x': coord['x'] - 1, 'y': coord['y']}
#     ]
#
#
# def avoid_consumption(future_head, snakeBodies, mySnake):
#     if len(snakeBodies) < 2:
#         return True
#     myLength = mySnake["length"]
#     for snake in snakeBodies:
#         if snake == mySnake:
#             continue
#         if future_head in getAllMoves(snake["head"]) and future_head not in snake["body"][1:-1] and myLength <= \
#                 snake["length"]:
#             return False
#     return True
