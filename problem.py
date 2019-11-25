from collections import *
from node import Node
from AI_lab2.heur_func import hf1, hf2

LOG = True


class EightPuzzleProblem:
    checked_states = deque()
    opened_nodes = deque()
    initState = []
    winState = []
    how = 0

    steps = 0
    mem = 0

    def __init__(self, init_state, win_state):
        self.initState = init_state
        self.winState = win_state

    def answer(self, state: list):
        if state == self.winState:
            return True
        return False

    def unique(self, state: list):
        if state in self.checked_states:
            print("[State repeat detected]")
            return False
        return True

    # Breadth-First-Search
    def run_bfs(self):
        # root init
        node_to_check = Node(self.initState)

        while not self.answer(node_to_check.matrix):
            self.checked_states.append(node_to_check.matrix)
            self.opened_nodes.extend(node_to_check.make_childs())

            if LOG:
                self.steps += 1
                self.mem = len(self.opened_nodes) + len(self.checked_states)
                print("[Steps: %d]" % self.steps)
                print("[Memory units used: %d]" % self.mem)
                # input()

            node_to_check = self.opened_nodes.popleft()

            # while not self.unique(node_to_check.matrix):
            #     node_to_check = self.opened_nodes.popleft()
            #     self.mem -= 1
            # if len(self.opened_nodes) == 0:
            #     print("UNEXPECTED TERMINATION")

        print(node_to_check.matrix, "Success")
        return 0

    # Depth-Limited-Search
    def __rec_dls(self, current_node: Node, limit):

        if self.answer(current_node.matrix):
            return 1
        elif current_node.depth == limit:
            return 0

        self.checked_states.append(current_node.matrix)
        current_node.make_childs()

        if LOG:
            self.steps += 1
            self.mem += len(current_node.childList) - 1
            print("[Steps: %d]" % self.steps)
            print("[Memory units used: %d]" % self.mem)
            # input()

        for node in current_node.childList:
            # Match!
            if self.__rec_dls(node, limit) == 1:
                return 1

    def __dls(self, limit):
        root = Node(self.initState)
        return self.__rec_dls(root, limit)

    def run_dls(self, max_limit: int):
        for i in range(1, max_limit+1):
            print("Level", i)
            if self.__dls(i) == 1:
                print("\n\n[SUCCESS on level %d]" % i)
                print("[Steps: %d]" % self.steps)
                print("[Memory units used: %d]" % self.mem)
                return 0

        print("\n\n[NOT SUCCESS on level %d]" % max_limit)
        print("[Steps: %d]" % self.steps)
        print("[Memory units used: %d]" % self.mem)

        return 0

    # Greedy-Search. If astar_arg = node.depth = 0 - Astar Search
    def __do_greedy(self, node_to_execute: Node, mode: int) -> Node:
        self.opened_nodes.extendleft(node_to_execute.make_childs())

        if LOG:
            self.steps += 1
            self.mem += len(node_to_execute.childList)
            print("[Steps: %d]" % self.steps)
            print("[Memory units used: %d]" % self.mem)
            # input()

        best_node = None
        min_h = 100

        def hf(matrix: list, mode: int) -> int:
            if mode == 0:
                return hf1(matrix, self.winState)
            else:
                return hf2(matrix, self.winState)

        for node in node_to_execute.childList:
            if hf(node.matrix, mode) < min_h and node.matrix not in self.checked_states:
                best_node = node
                min_h = hf(node.matrix, mode)

        try: self.opened_nodes.remove(node_to_execute)
        except: pass

        try: self.checked_states.append(best_node.matrix)
        except: pass

        return best_node

    def run_greedy(self, mode: int):
        current_node = Node(self.initState)

        try:
            while not self.answer(current_node.matrix):
                current_node = self.__do_greedy(current_node, mode)

                while current_node is None:
                    current_node = self.__do_greedy(self.opened_nodes.popleft(), mode)
        except:
            print("\n\n[NOT SUCCESS (somehow)]")
            print("[Steps: %d]" % self.steps)
            print("[Memory units used: %d]" % (self.mem + 1))
            return 0

        print("\n\n[SUCCESS]")
        print("[Steps: %d]" % self.steps)
        print("[Memory units used: %d]" % (self.mem + 1))
        return 0

    #????????????
    # def __findmin_h(self, queue: list, mode: int, pop: bool=True):
    #     min_h = 1000
    #     min_node = None
    #
    #     for node in queue:
    #         if mode == 0 and hf1(node.matrix, self.winState) + node.depth < min_h:
    #             min_h = hf1(node.matrix, self.winState) + node.depth
    #             min_node = node
    #
    #     if pop:
    #         queue.remove(min_node)
    #     return min_node
    #
    #
    # def run_astar(self, mode: int):
    #     current_node = Node(self.initState)
    #
    #     try:
    #         while not self.answer(current_node.matrix):
    #             current_node = self.__do_greedy(current_node, mode)
    #
    #             while current_node is None:
    #                 current_node = self.__do_greedy(self.opened_nodes.popleft(), mode)
    #     except:
    #         print("\n\n[NOT SUCCESS (somehow)]")
    #         print("[Steps: %d]" % self.steps)
    #         print("[Memory units used: %d]" % (self.mem + 1))
    #         return 0
    #
    #     print("\n\n[SUCCESS]")
    #     print("[Steps: %d]" % self.steps)
    #     print("[Memory units used: %d]" % (self.mem + 1))
    #     return 0