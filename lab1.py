from copy import deepcopy
import utilLib as lib
from test import FindNull, NumOfMoves, GenMoves


class node:
    depth = 0
    parent = None
    matrix = list()
    nodeList = list()

    def __init__(self, depth, parentPointer, matrix):
        self.depth = depth
        self.parent = parentPointer
        self.matrix = matrix
        self.nodeList = list()

    def addDescendant(self, matrix):
        childNode = node(self.depth + 1, self, matrix)
        self.nodeList.append(childNode)
        return childNode

    def showDescendants(self):
        print("\t", self)
        for i in range(0, self.nodeList.__len__()):
            print("Node %d | Depth %d" % (i, self.nodeList[i].depth))


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