from copy import deepcopy
import utilLib as lib
from test import FindNull, NumOfMoves, GenMoves

initMatrix = lib.bs8
targetMatrix = lib.ts1

class node: pass

class node:
    depth = 0
    parent: node
    matrix = list()
    childList = list()
    parentMove = list()

    def __init__(self, depth, parentPointer, matrix, parentMove):
        self.depth = depth
        self.parent = parentPointer
        self.matrix = matrix
        self.parentMove = parentMove

    def _d_addSuccessor(self, matrix):
        childNode = node(self.depth + 1, self, matrix)
        self.childList.append(childNode)
        return childNode

    def _d_showSuccessors(self):
        print("\t", self)
        for i in range(0, self.childList.__len__()):
            print("Node %d | Depth %d" % (i, self.childList[i].depth))

    def makeChilds(self):
        nullPnt = FindNull(self.matrix)
        moveList = list()
        if self.parent == None:
            moveList = GenMoves(nullPnt, [3, 3])
        else:
            moveList = GenMoves(nullPnt, FindNull(self.parent.matrix))

        for move in moveList:
            x = move[0]
            y = move[1]
            x0 = nullPnt[0]
            y0 = nullPnt[1]

            newMatrix = deepcopy(self.matrix)

            newMatrix[x0][y0] = newMatrix[x][y]
            newMatrix[x][y] = 0

            self.childList.append(node(self.depth + 1, self, newMatrix, nullPnt))


# recursive Depth-Limited-Search
def recursiveDLS(currentNode, limit):
    if currentNode.matrix == targetMatrix:
        print(currentNode.matrix)
        return 1
    elif node.depth == limit:
        return 0

    currentNode.makeChilds()

    for childNode in currentNode.childList:
        res = recursiveDLS(childNode, limit)
        # Match!
        if res == 1:
            print("\n\n- - - Finally! - - -")
            return 1
        # Not match
        elif res == 0:
            pass

rootNode = node(0, None, initMatrix, [3, 3])

for i in range(0, 10):
    recursiveDLS(rootNode, i)
"""
class tree:
    treeDepth = None
    root = None
    beginState = list()
    targetState = list()
    nodeQueue = list()

    def __init__(self, bs, ts) -> None:
        self.treeDepth = 0
        self.root = node(0, None, bs)
        self.nodeQueue.append(self.root)
        self.beginState = bs
        self.targetState = ts

    def showPath(self) -> None:
        print("Start:", self.beginState)
        print("Finish:", self.targetState)

    def showQueue(self) -> None:
        for i in self.nodeQueue:
            print(i)

    def showTree(self, nodesInLayer, layer = 0):
        if layer == 0:
            print("- - - Tree root - - -")

        n = nodesInLayer.__len__()
        lst = list()

        if n == 0:
            print("\n\n- - - End of tree - - -")
            return

        print("\n[%d]: " % layer, end=None)

        for i in nodesInLayer:
            print("| ", end=' ')
            lst.extend(i.nodeList)

        self.showTree(lst, layer + 1)

    # run through deepest layer of the tree
    # check for finish
    # build new descendants for all deepest nodes
    def doLayer(self):
        newNodeQueue = list()

        for curNode in self.nodeQueue:
            if curNode == self.targetState:
                print("RDY:", curNode.matrix)
                exit(0)

            nullCoord = FindNull(curNode.matrix)
            if curNode == self.root:
                parentNullCoord = [3, 3]
            else:
                parentNullCoord = FindNull(curNode.parent.matrix)

            #
            print(parentNullCoord)
            #

            for toSwitchCoord in GenMoves(nullCoord, parentNullCoord):
                newMatrix = deepcopy(curNode.matrix)

                x = toSwitchCoord[0]
                y = toSwitchCoord[1]
                x0 = nullCoord[0]
                y0 = nullCoord[1]

                newMatrix[x0][y0] = newMatrix[x][y]
                newMatrix[x][y] = 0

                curNode.addDescendant(newMatrix)

            newNodeQueue.extend(curNode.nodeList)

        self.nodeQueue = newNodeQueue
        self.treeDepth += 1

    def doJob(self):
        for i in range(0, 50):
            self.doLayer()
        lst = list()
        lst.append(self.root)
        self.showTree(lst)


myTree = tree(lib.bs1, lib.ts1)
myTree.showPath()
myTree.doJob()

"""