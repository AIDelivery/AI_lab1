from collections import deque
from node import Node

class eightPuzzleProblem:
    cutoffStates = deque()
    steps = 0

    def __init__(self, initState, winState):
        self.initState = initState
        self.winState = winState

    # def isFinishState(self, state):
    #     return state == self.winState

    def BFS(self, currentNode : Node, checkQueue):
        if self.winState == currentNode.matrix:
            print("Ready")
            return 1

        self.steps += 1
        checkQueue.extend(currentNode.makeChilds())
        return 0

    def runBFS(self):
        root = Node(self.initState)
        checkQueue = deque()
        checkQueue.append(root)

        while True:
            NodeToCheck = checkQueue.popleft()

            # if NodeToCheck in self.cutoffStates:
            #     continue
            # else:
            #     self.cutoffStates.append(NodeToCheck)

            if self.BFS(NodeToCheck, checkQueue) == 1:
                print("Success")
                return 0

    # Depth-Limited-Search subfunction
    def recursiveDLS(self, currentNode : Node, limit):

        # if currentNode in self.cutoffStates:
        #     return 0
        # else:
        #     self.cutoffStates.append(currentNode)

        self.steps += 1

        if currentNode.matrix == self.winState:
            return 1
        elif currentNode.depth == limit:
            return 0

        currentNode.makeChilds()

        # print("CHILDLIST")
        # for i in currentNode.childList:
        #     print(i.matrix[0])
        #     print(i.matrix[1])
        #     print(i.matrix[2])
        # print("/CHILDLIST")

        for childNode in currentNode.childList:
            res = self.recursiveDLS(childNode, limit)

            # Match!
            if res == 1:
                return 1
            # Not match
            elif res == 0:
                pass

    def DLS(self, limit):
        root = Node(self.initState, 0)
        return self.recursiveDLS(root, limit)

    def iterativeDLS(self, maxLimit):
        for i in range(1, maxLimit):
            self.cutoffStates.clear()
            print("Level", i)
            if self.DLS(i) == 1:
                print("Success\n", "Steps:", self.steps)
                return 1

        return 0
