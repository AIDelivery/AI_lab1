from copy import deepcopy
from util import find_null, gen_moves


class Node:
    def __init__(self, state, depth = 0, parent_pointer = None):
        self.depth = depth
        self.pathCost = depth
        self.parent = parent_pointer
        self.matrix = state
        self.childList = list()

    def makeChilds(self):
        nullPnt = find_null(self.matrix)
        moveList = list()

        # print("\n\n", nullPnt, "\n\n")
        # print("\n\n", self.matrix, "\n\n")

        if self.parent == None:
            moveList = gen_moves(self.matrix)
        else:
            moveList = gen_moves(self.matrix, self.parent.matrix)

        for move in moveList:
            x = move[0]
            y = move[1]
            x0 = nullPnt[0]
            y0 = nullPnt[1]

            newMatrix = deepcopy(self.matrix)

            newMatrix[x0][y0] = newMatrix[x][y]
            newMatrix[x][y] = 0

            self.childList.append(Node(newMatrix, self.depth + 1, self))

        return self.childList