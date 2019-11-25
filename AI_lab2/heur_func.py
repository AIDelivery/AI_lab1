from node import Node, find_in_2d_array

LOG = True

""" Matrix numeration:
00 01 02
10 11 12
20 21 22
"""


def is_matrix(matrix: list, size: int=3) -> bool:
    res = False
    try:
        str = len(matrix)
        col = len(matrix[0])

        if str == col == size:
            res = True
    except: print(matrix, "IS NOT A MATRIX")

    return res


def count_match_places(current_state: list, target_state: list) -> int:
    """
    Count number of squares matches with target_state matrix
    :param current_state: A
    :param target_state: B
    :return: how_much(A == B)
    """
    matches = 0

    for i in range(3):
        for j in range(3):
            if current_state[i][j] == target_state[i][j]:
                matches += 1

    # if LOG:
    #     print("[count_match_places]", current_state, matches)
    return matches

def count_nomatch_places(current_state: list, target_state: list) -> int:
    return 9 - count_match_places(current_state, target_state)

def which_match_is_greater(target_matrix: list, nodes_to_check, matrix_history: list) -> Node:
    """
    IF nodes_to_check ISN'T None, THERE WILL BE NODE IN RETURN
    :param target_matrix:
    :param nodes_to_check:
    :param matrix_history:
    :param other_unique_nodes:
    :return:
    """
    res_node = None
    maxim = 0

    for node in nodes_to_check:
        matrix = node.matrix
        match_count = count_match_places(matrix, target_matrix)

        if matrix in matrix_history:
            continue
        elif match_count > maxim:
            res_node = node
            maxim = match_count
        # elif other_unique_nodes is not None:
        #     other_unique_nodes.append(node)
        # else:
        #     raise Exception("Error. Try put additional node list in which_match_is_greater as last argument")

    if res_node:
        matrix_history.append(res_node.matrix)

    # try:
    #     # other_unique_nodes.remove(res_node)
    #     matrix_history.append(res_node.matrix)
    # except:
    #     print("Error. matrix_history is None\nOR\nchildList is Empty \nOR\n other_unique_nodes is None")

    return res_node


def manhattan_dist(current_state: list, target_state: list, square: int) -> int:
    if not is_matrix(current_state) or not is_matrix(target_state):
        raise Exception("Error. Null pointer as argument")

    current_coords = find_in_2d_array(current_state, square)
    target_coords = find_in_2d_array(target_state, square)

    # print("[manhattan_dist] matrix: ", current_state)
    # print("[manhattan_dist] square: ", square)
    # print("[manhattan_dist] current_coords: ", current_coords)
    # print("[manhattan_dist] target_coords: ", target_coords)
    # print("[manhattan_dist] difference: ", abs(current_coords[0] - target_coords[0]) + abs(current_coords[1] - target_coords[1]))

    if current_coords is None or target_coords is None:
        raise Exception("[manhattan_dist] Error. Matrix is invalid. There isn't %d square" % square)

    return abs(current_coords[0] - target_coords[0]) + abs(current_coords[1] - target_coords[1])


# Heuristic Functions
def hf1(matrix_to_check: list, target_matrix: list) -> int:
    res = 0

    if not is_matrix(matrix_to_check):
        raise Exception("[eightPuzzleProblemExt.hh1] is not a matrix")

    return count_nomatch_places(matrix_to_check, target_matrix)


def hf2(matrix_to_check: list, target_matrix: list) -> int:
    res = 0

    for i in range(0, 9):
        res += manhattan_dist(matrix_to_check, target_matrix, i)

    print("[eightPuzzleProblemExt.hh2] Manhattan destination sum: ", res)
    print("[eightPuzzleProblemExt.hh2] of matrix: ", matrix_to_check)
    return res
