from copy import deepcopy

LOG = True


def find_in_2d_array(matrix: list, num: int = 0, error_log: bool = False) -> list or None:
    """
    Locate integer in 2-Dimensional array
    
    :param matrix: Given matrix of state
    :param num: Integer to find
    :return: Coordinates of i = [string][column] or None
    """

    try:
        for i in range(0, 3):
            for j in range(0, 3):
                if matrix[i][j] == num:
                    return [i, j]
    except:
        if error_log:
            print("- - -\n", matrix)
            print("Error. There is no %d in matrix... - - -", i)
        return None


def __noma__(matrix3) -> int:
    """
    Get number of available moves from the current 0 coordinate [string][column]

    :param matrix3: [string][column] coordinate of 0
    :return: Number of available moves from 2 to 4
    """
    null_pnt = find_in_2d_array(matrix3)

    if null_pnt[0] == null_pnt[1] == 1:
        return 4
    elif null_pnt[0] != 1 and null_pnt[1] != 1:
        return 2
    return 3


def gen_moves_in_matrix3(cur_state: list, pr_state: list = None) -> list:
    """
    Generates coordinates (list of [string][column]) of available moves, except previous state from parent node

    :param cur_state: Matrix of current state of puzzle
    :param pr_state: Matrix of parent state of puzzle
    :return: List of coordinates. Example: [[0, 1], [1, 2], [1, 1]]
    """
    moves_avail = list()
    n = __noma__(cur_state)
    cur_state_null_pnt = find_in_2d_array(cur_state)

    if n == 4:
        moves_avail.append([0, 1])
        moves_avail.append([1, 0])
        moves_avail.append([2, 1])
        moves_avail.append([1, 2])
    elif n == 3:
        moves_avail.append([1, 1])
        if cur_state_null_pnt[0] == 0 or cur_state_null_pnt[0] == 2:
            moves_avail.append([cur_state_null_pnt[0], 0])
            moves_avail.append([cur_state_null_pnt[0], 2])
        else:
            moves_avail.append([2, cur_state_null_pnt[1]])
            moves_avail.append([0, cur_state_null_pnt[1]])
    else:
        moves_avail.append([1, cur_state_null_pnt[1]])
        if cur_state_null_pnt[0] == 0:
            moves_avail.append([0, 1])
        else:
            moves_avail.append([2, 1])

    try:
        par_state_null_pnt = find_in_2d_array(pr_state, 0, False)
        moves_avail.remove(par_state_null_pnt)
    except:
        print("[gen_moves] Initial state?")

    # print("Current State: ")
    # for i in cur_state_null_pntte:
    #     print(i)
    # print("Available moves: ", end=" ")
    # for i in movesAvailable:
    #     print(i, end=" ")
    # print('\n')

    return moves_avail


class Node:
    def __init__(self, state, depth=0, parent_pointer=None):
        self.depth = depth
        self.pathCost = depth
        self.parent = parent_pointer
        self.matrix = state
        self.childList = list()

    def make_childs(self) -> list:
        if len(self.childList) != 0:
            return self.childList

        null_pnt = find_in_2d_array(self.matrix, 0)

        if self.parent is not None:
            move_list = gen_moves_in_matrix3(self.matrix, self.parent.matrix)
        else:
            move_list = gen_moves_in_matrix3(self.matrix)

        if LOG:
            print("- - - make_childs - - -")
            print("Parent:", self.matrix[0], self.matrix[1], self.matrix[2], sep = "\n")
            print("\nSucessors:")

        for move in move_list:
            x = move[0]
            y = move[1]
            x0 = null_pnt[0]
            y0 = null_pnt[1]

            new_matrix = deepcopy(self.matrix)
            new_matrix[x0][y0] = new_matrix[x][y]
            new_matrix[x][y] = 0

            self.childList.append(Node(new_matrix, self.depth + 1, self))

            if LOG:
                print(new_matrix[0])
                print(new_matrix[1])
                print(new_matrix[2], "\n")

        print("- - -")
        return self.childList