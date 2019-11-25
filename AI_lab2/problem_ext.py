from collections import deque

from node import Node
from problem import eightPuzzleProblem
from AI_lab2.heur_func import *

tempBound = 3000

class eightPuzzleProblemExt(eightPuzzleProblem):
    heuristic_mode = 0
    checked_states = list()
    opened_nodes = deque()

    def __init__(self, initState, winState, how: int = 3):
        eightPuzzleProblem.__init__(self, initState, winState)

    def hh1(self, matrix_to_check: list) -> int:
        res = 0

        if not is_matrix(matrix_to_check):
            raise Exception("[eightPuzzleProblemExt.hh1] is not a matrix")

        return count_match_places(matrix_to_check, self.winState)

    def hh2(self, matrix_to_check: list) -> int:
        res = 0

        for i in range(0, 9):
            res += manhattan_dist(matrix_to_check, self.winState, i)

        print("[eightPuzzleProblemExt.hh2] Manhattan distanation sum: ", res)
        return res

    def remove_doubles(self, nodes_to_clear: list):
        for node in nodes_to_clear:
            if node.matrix in self.checked_states:
                nodes_to_clear.remove(node)

        return nodes_to_clear

    def find_max_in_heur(self, nodes_to_check: list) -> (Node, int) or None:
        max_node = None
        max_h = 0

        for node in nodes_to_check:
            temp = 0
            if self.heuristic_mode == 0:
                print("\n\n1\n\n")
                temp = self.hh1(node.matrix)
            else:
                print("\n\n2\n\n")
                temp = self.hh2(node.matrix)

            if temp > max_h:
                max_h = temp
                max_node = node

        if max_node is None and len(self.opened_nodes) != 0:
            print("ISSUE")
            max_node = self.find_max_in_heur(self.opened_nodes.popleft())

        return max_node, max_h

    def do_greedy(self, current_node: Node):
        """
        Check childList of current_node. Find the best of them or best in upper level (if cut issue)
        :param current_node:
        :return: Perfect node in current_node.childList OR in opened_nodes queue
        """

        self.steps += 1

        # for node in current_node.childList:
        #
        #
        # best_node = not None
        # while best_node is not None:
        #     best_node = self.find_max_in_heur(current_node.childList)
        #     best_node.make_childs()

        if current_node.matrix == self.winState:
            print("[SUCCESS!]", current_node.matrix, "is", self.winState, sep="\n")
            return None
        elif self.steps > tempBound:
            print("[NOT SUCCESS...]", current_node.matrix, "is not", self.winState, sep="\n")
            return None

        nodes_to_check = self.remove_doubles(current_node.childList)

        while len(nodes_to_check) == 0:
            nodes_to_check = self.opened_nodes.popleft()
            nodes_to_check = self.remove_doubles(nodes_to_check)

        res, n = self.find_max_in_heur(nodes_to_check)

        # ???
        try:
            res.matrix
        except:
            res = res[0]

        try:
            res.matrix
        except:
            res = res[0]

        if LOG:
            print("[do_greedy] Max of h-function is %d" % n)
            print(res.matrix)

        self.checked_states.append(res.matrix)
        return res

    def greedy_search(self):
        root = Node(self.initState)

        print("Begin")
        # checkQueue = deque()
        # checkQueue.append(root)

        current_node = root
        self.opened_nodes = deque([[root]])

        while current_node is not None:
            print("Step %d" % self.steps)
            self.opened_nodes.appendleft(current_node.make_childs())
            current_node = self.do_greedy(current_node)

        print("Finish")

    def do_astar(self, current_node: Node) -> Node:
        self.steps += 1

        if current_node.matrix == self.winState:
            print("[Success!]")
            print(current_node.matrix)
            print(self.winState)
            return None
        elif self.steps > 10000:
            print("[Not success...]")
            return None

        if self.heuristic_func == 0:
            return self.h1(current_node, self.winState)
        else:
            return self.h2(current_node, self.winState)

    def astar_search(self):
        root = Node(self.initState)

        print("Begin")
        # checkQueue = deque()
        # checkQueue.append(root)

        current_node = root

        while current_node is not None:
            print("Step %d" % self.steps)
            current_node.makeChilds()
            current_node = self.do_astar(current_node)

        print("Finish")


    def h1(self, parent_node: Node, target_state: list):
        """
        Heuristic function considering number of squares in the right places
        :param parent_node: Node to check which child is better to reveal
        :param target_state: Final state of the puzzle to compare with
        :return: The best node if there is one. Any node if they're equal. None if there aren't any child nodes
        """
        if parent_node is None or target_state is None or not is_matrix(target_state):
            raise Exception("Error. Null pointer as argument")

        # nodes_to_check_list = deque(parent_node.childList) + self.opened_nodes
        great_node = which_match_is_greater(self.winState, parent_node.childList, self.checked_states)
        print("[H1: GREAT NODE:]", great_node)

        if great_node is None:
            print("There's none \"great\" nodes")
            great_node = self.checked_states[-1]

        return great_node

    def h2(self, parent_node: Node, target_state: list) -> Node:
        """
        Heuristic function considering sum of manhattan distances of each square in puzzle
        :param parent_node: Node to check which child is better to reveal
        :param target_state: Final state of the puzzle to compare with
        :return: The best node if there is one. Any node if they're equal. None if there aren't any child nodes
        """
        if parent_node is None or target_state is None or not is_matrix(target_state):
            raise Exception("Error. Null pointer as argument")

        max_node = None
        man_sum_memory = 0

        for child_node in parent_node.childList:
            # print("[PARENT NODE]", parent_node, "[PARENT MATRIX]", parent_node.matrix)
            man_dist = manhattan_dist_sum(child_node, target_state)
            if max_node is None or man_dist > man_sum_memory:
                max_node = child_node
                man_sum_memory = man_dist

        if max_node is None:
            raise Exception("Error. Max_node is None")

        return max_node