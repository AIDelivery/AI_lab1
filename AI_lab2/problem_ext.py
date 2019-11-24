from collections import deque

from node import Node
from problem import eightPuzzleProblem
from AI_lab2.heur_func import *


class eightPuzzleProblemExt(eightPuzzleProblem):
    heuristic_func = int()
    queue_if_cut = deque()

    def __init__(self, initState, winState, how: int = 0):
        eightPuzzleProblem.__init__(self, initState, winState)
        heuristic_func = how

    def h1(self, parent_node: Node, target_state: list):
        """
        Heuristic function considering number of squares in the right places
        :param parent_node: Node to check which child is better to reveal
        :param target_state: Final state of the puzzle to compare with
        :return: The best node if there is one. Any node if they're equal. None if there aren't any child nodes
        """
        if parent_node is None or target_state is None or not is_matrix(target_state):
            raise Exception("Error. Null pointer as argument")

        great_node = which_match_is_greater(self.winState, parent_node.childList, self.cutoffStates, self.queue_if_cut)
        print("[H1: GREAT NODE:]", great_node)

        if great_node is None:
            print("There's none \"great\" nodes")
            great_node = self.queue_if_cut[-1]

        return great_node

    def h2(self, parent_node: Node, target_state: list):
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


    def do_greedy(self, current_node: Node) -> Node:
        """
        :param current_node:
        :return: Perfect node in current_node.childList OR in opened_nodes queue
        """

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


    def greedy_search(self):
        root = Node(self.initState)
        opened_nodes = deque(root)
        checked_nodes = deque(root)

        print("Begin")
        # checkQueue = deque()
        # checkQueue.append(root)

        current_node = root

        while current_node is not None:
            print("Step %d" % self.steps)
            current_node.makeChilds()
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