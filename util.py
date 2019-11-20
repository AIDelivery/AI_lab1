from copy import deepcopy

""" Matrix numeration:
00 01 02
10 11 12
20 21 22
"""


def find_null(matrix: list) -> list or None:
    """
    Locate 0 in puzzle

    :param matrix: Given matrix of state
    :return: Coordinates of zero = [string][column]
    """
    if matrix == None:
        return None


    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == 0:
                return [i, j]

    raise Exception("Error. There is no 0 in matrix...")


def num_of_moves(state) -> int:
    """
    Get number of available moves from the current 0 coordinate [string][column]

    :param state: [string][column] coordinate of 0
    :return: Number of available moves from 2 to 4
    """
    stateNull = find_null(state)

    if stateNull[0] == stateNull[1] == 1:
        return 4
    elif stateNull[0] != 1 and stateNull[1] != 1:
        return 2
    return 3


def gen_moves(curState, prState = None) -> list:
    """
    Generates coordinates (list of [string][column]) of available moves, except previous state from parent node

    :param curState: Matrix of current state of puzzle
    :param prState: Matrix of parent state of puzzle
    :return: List of coordinates. Example: [[0, 1], [1, 2], [1, 1]]
    """
    movesAvailable = list()
    curStateNull = find_null(curState)
    prStateNull = find_null(prState)
    n = num_of_moves(curState)

    if n == 4:
        movesAvailable.append([0, 1])
        movesAvailable.append([1, 0])
        movesAvailable.append([2, 1])
        movesAvailable.append([1, 2])
    elif n == 3:
        movesAvailable.append([1, 1])
        if curStateNull[0] == 0 or curStateNull[0] == 2:
            movesAvailable.append([curStateNull[0], 0])
            movesAvailable.append([curStateNull[0], 2])
        else:
            movesAvailable.append([2, curStateNull[1]])
            movesAvailable.append([0, curStateNull[1]])
    else:
        movesAvailable.append([1, curStateNull[1]])
        if curStateNull[0] == 0:
            movesAvailable.append([0, 1])
        else:
            movesAvailable.append([2, 1])

    try:
        movesAvailable.remove(prStateNull)
    except:
        pass

    # print("Current State: ")
    # for i in curState:
    #     print(i)
    # print("Available moves: ", end=" ")
    # for i in movesAvailable:
    #     print(i, end=" ")
    # print('\n')

    return movesAvailable
