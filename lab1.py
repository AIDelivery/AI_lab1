from copy import deepcopy
import utilLib as lib
from test import FindNull as FindNullN, NumOfMoves, GenMovesN
from collections import deque

initMatrix = lib.bs8
targetMatrix = lib.ts1
LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4
MOVE_COST = 1

class node: pass

class node:
    def __init__(self, state, depth = 0, parentPointer = None, parentMove = None):
        self.depth = depth
        self.pathCost = depth
        self.parent = parentPointer
        self.parentMove = parentMove
        self.matrix = state
        self.childList = list()


    def addSuccessor(self, matrix):
        childNode = node(self.depth + 1, self, matrix)
        self.childList.append(childNode)
        return childNode

    def showSuccessors(self):
        print("\t", self)
        for i in range(0, self.childList.__len__()):
            print("Node %d | Depth %d" % (i, self.childList[i].depth))


    def makeChilds(self):
        nullPnt = FindNullN(self.matrix)
        moveList = list()

        # print("\n\n", nullPnt, "\n\n")
        # print("\n\n", self.matrix, "\n\n")

        if self.parent == None:
            moveList = GenMovesN(self.matrix)
        else:
            moveList = GenMovesN(self.matrix, self.parent.matrix)

        for move in moveList:
            x = move[0]
            y = move[1]
            x0 = nullPnt[0]
            y0 = nullPnt[1]

            newMatrix = deepcopy(self.matrix)

            newMatrix[x0][y0] = newMatrix[x][y]
            newMatrix[x][y] = 0

            self.childList.append(node(newMatrix, self.depth + 1, self, None))

        return self.childList

    def isEqual(self, state : node):
        if self.matrix == state.matrix:
            return True
        else:
            return False


class eightPuzzleProblem:
    cutoffStates = deque()
    steps = 0

    def __init__(self, initState, winState):
        self.initState = initState
        self.winState = winState

    # def isFinishState(self, state):
    #     return state == self.winState

    def BFS(self, currentNode : node, checkQueue):
        if self.winState == currentNode.matrix:
            print("Ready")
            return 1

        self.steps += 1
        checkQueue.extend(currentNode.makeChilds())
        return 0

    def runBFS(self):
        root = node(self.initState)
        checkQueue = deque()
        checkQueue.append(root)

        while True:
            nodeToCheck = checkQueue.popleft()

            # if nodeToCheck in self.cutoffStates:
            #     continue
            # else:
            #     self.cutoffStates.append(nodeToCheck)

            if self.BFS(nodeToCheck, checkQueue) == 1:
                print("Success")
                return 0

    # Depth-Limited-Search subfunction
    def recursiveDLS(self, currentNode : node, limit):

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
        root = node(self.initState, 0)
        return self.recursiveDLS(root, limit)

    def iterativeDLS(self, maxLimit):
        for i in range(1, maxLimit):
            self.cutoffStates.clear()
            print("Level", i)
            if self.DLS(i) == 1:
                print("Success\n", "Steps:", self.steps)
                return 1

        return 0

tempMatrix = [[1, 2, 3],[4, 6, 0],[7, 5, 8]]
problem = eightPuzzleProblem(initMatrix, targetMatrix)
print(problem.iterativeDLS(100))