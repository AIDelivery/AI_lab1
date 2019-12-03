from collections import *
from node import Node
from AI_lab2.heur_func import hf1, hf2

LOG = True


class EightPuzzleProblem:
    checked_states = deque()
    opened_nodes = deque()
    initState = []
    winState = []

    steps = 0
    mem = 0

    def __init__(self, init_state, win_state):
        self.initState = init_state
        self.winState = win_state

    def is_answer(self, state: list):
        if state == self.winState:
            return True
        return False

    def is_unique(self, state: list):
        if state in self.checked_states:
            if LOG:
                print("[State repeat detected]")
            return False
        return True

    # Breadth-First-Search
    def run_bfs(self):
        self.checked_states.clear()
        self.opened_nodes.clear()

        node_to_check = Node(self.initState)
        self.steps = 1
        self.mem = 1

        while not self.is_answer(node_to_check.matrix):
            self.checked_states.append(node_to_check.matrix)
            self.opened_nodes.extend(node_to_check.make_childs())

            if LOG:
                self.steps += 1
                self.mem += len(node_to_check.childList)
                print("[Step: %d]" % self.steps)
                print("[Memory units used: %d]" % self.mem)
                # input()

            node_to_check = self.opened_nodes.popleft()

            while not self.is_unique(node_to_check.matrix):
                node_to_check = self.opened_nodes.popleft()
            if len(self.opened_nodes) == 0:
                print("[Can't figure out how to get state", self.winState, "]\n[TERMINATION]", sep=" ")
                return -1

        print(node_to_check.matrix, "Success!")
        return 0

    # Depth-Limited-Search
    def __rec_dls(self, current_node: Node, limit):

        if self.is_answer(current_node.matrix):
            return 1
        elif current_node.depth == limit:
            return 0

        self.checked_states.append(current_node.matrix)
        current_node.make_childs()

        if LOG:
            self.steps += 1
            self.mem += len(current_node.childList)
            print("[Steps: %d]" % self.steps)
            print("[Memory units used: %d]" % self.mem)
            # input()

        for node in current_node.childList:
            # Match!
            if self.__rec_dls(node, limit) == 1:
                return 1

        return 0

    def __dls(self, limit):
        root = Node(self.initState)

        self.steps += 1
        self.mem = 1

        return self.__rec_dls(root, limit)

    def run_dls(self, max_limit: int):
        self.opened_nodes.clear()
        self.checked_states.clear()
        self.steps = 0
        self.mem = 0

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

    # Greedy-Search
    def __do_greedy(self, node_to_execute: Node, mode: int) -> Node or None:
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
        self.checked_states.clear()
        self.opened_nodes.clear()

        current_node = Node(self.initState)
        self.steps = 1
        self.mem = 1

        try:
            while not self.is_answer(current_node.matrix):
                current_node = self.__do_greedy(current_node, mode)

                while current_node is None:
                    current_node = self.__do_greedy(self.opened_nodes.popleft(), mode)
        except:
            print("\n\n[NOT SUCCESS (somehow)]")
            print("[Steps: %d]" % self.steps)
            print("[Memory units used: %d]" % (self.mem))
            return 0

        print("\n\n[SUCCESS]")
        print("[Steps: %d]" % self.steps)
        print("[Memory units used: %d]" % (self.mem))
        print("[Path cost: %d]" % (current_node.depth))
        return 0

    # AStar-Search
    def __do_astar(self, node_to_execute: Node, mode: int) -> Node:
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
            if hf(node.matrix, mode) + node.depth < min_h and node.matrix not in self.checked_states:
                best_node = node
                min_h = hf(node.matrix, mode) + node.depth
        for node in self.opened_nodes:
            if hf(node.matrix, mode) + node.depth < min_h and node.matrix not in self.checked_states:
                best_node = node
                min_h = hf(node.matrix, mode) + node.depth
        try:
            self.opened_nodes.remove(node_to_execute)
        except:
            pass

        try:
            self.checked_states.append(best_node.matrix)
        except:
            pass

        return best_node

    def run_astar(self, mode: int):
        self.opened_nodes.clear()
        self.checked_states.clear()

        current_node = Node(self.initState)
        self.steps = 1
        self.mem = 1

        try:
            while not self.is_answer(current_node.matrix):
                current_node = self.__do_astar(current_node, mode)

                while current_node is None:
                    current_node = self.__do_astar(self.opened_nodes.popleft(), mode)
        except:
            print("\n\n[NOT SUCCESS (somehow)]")
            print("[Steps: %d]" % self.steps)
            print("[Memory units used: %d]" % (self.mem))
            return 0

        print("\n\n[SUCCESS]")
        print("[Steps: %d]" % self.steps)
        print("[Memory units used: %d]" % (self.mem))
        print("[Path cost: %d]" % (current_node.depth))
        return 0
