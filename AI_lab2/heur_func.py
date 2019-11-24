from node import Node
from util import is_matrix

LOG = True


def count_match_places(current_state: list, target_state: list) -> int:
    """
    Count number of squares matches with target_state matrix
    :param current_state: A
    :param target_state: B
    :return: how_much(A == B)
    """
    matches = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if current_state[i][j] == target_state[i][j]:
                matches += 1

    if LOG:
        print("[count_match_places]", current_state, matches)
    return matches


def which_match_is_greater(target_matrix: list, nodes_to_check: list, matrix_history: list, other_unique_nodes: list = None) -> Node or None:
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
            matrix_history.append(matrix)
        elif other_unique_nodes is not None:
            other_unique_nodes.append(node)
        else:
            raise Exception("Error. Try put additional node list in which_match_is_greater as last argument")

    return res_node


def manhattan_dist1(current_state: list, target_state: list, square: int) -> int:
    if not is_matrix(current_state) or not is_matrix(target_state):
        raise Exception("Error. Null pointer as argument")

    current_coords = list([-1, -1])
    target_coords = list([-1, -1])
    i = j = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if current_state[i][j] == square:
                current_coords = [i, j]
            if target_state[i][j] == square:
                target_coords = [i, j]

    if current_coords == [-1, -1] or target_coords == [-1, -1]:
        raise Exception("Error. Matrix is invalid. There isn't %d square" % square)

    return abs(current_coords[0] - target_coords[0]) + abs(current_coords[1] - target_coords[1])


def manhattan_dist(current_node: Node, target_state: list, square: int) -> int:
    return manhattan_dist1(current_node.matrix, target_state, square)


def manhattan_dist_sum1(current_state: list, target_state: list, size: int = 3) -> int:
    if not is_matrix(current_state) or not is_matrix(target_state):
        raise Exception("Error. Null pointer as argument")

    res_sum = 0

    for i in range(0, size*size):
        res_sum += manhattan_dist1(current_state, target_state, i)

    return res_sum


def manhattan_dist_sum(current_node: Node, target_state: list, size: int = 3) -> int:
    return manhattan_dist_sum1(current_node.matrix, target_state, size)
