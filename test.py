from copy import deepcopy
import utilLib as st

SHIFTS = 0

"""
00 01 02
10 11 12
20 21 22
"""


# print matrix
def showMatrix(matrix, beg=None, end=None):
    if beg:
        print(beg)

    for i in matrix:
        print(i)

    if end:
        print(end)


# Get number of available moves from the current *state*
def NumOfMoves(state):
    if state[0] == state[1] == 1:
        return 4
    elif state[0] != 1 and state[1] != 1:
        return 2
    return 3


# Generates coordinates of available moves, except previous
def GenMoves(curState, prState=[3, 3]):
    d = list()
    n = NumOfMoves(curState)

    if n == 4:
        d.append([0, 1])
        d.append([1, 0])
        d.append([2, 1])
        d.append([1, 2])
    elif n == 3:
        d.append([1, 1])
        if curState[0] == 0 or curState[0] == 2:
            d.append([curState[0], 0])
            d.append([curState[0], 2])
        else:
            d.append([2, curState[1]])
            d.append([0, curState[1]])
    else:
        d.append([1, curState[1]])
        if curState[0] == 0:
            d.append([0, 1])
        else:
            d.append([2, 1])

    try:
        d.remove(prState)
    except:
        pass

    print("Current State: ", curState, "\nAvailable moves:", end=" ")
    for i in d:
        print(i, end=" ")
    print('\n')

    return d


# Find 0 integer value in matrix
def FindNull(matrix):
    res = -1

    for i in range(0, st.nor):
        try:
            res = matrix[i].index(0, 0, st.noc)
        except:
            continue

        return list([i, res])

    raise Exception("Error. There is no 0 in matrix...")


# BFS-scan
def layerScan(matrixList, queueForEachMatrix, nullInEachMatrix, depth=1):
    # new matrixList, queueForEachMatrix, nullInEachMatrix
    # for the next layer
    listOfMatrixs = list()
    listOfQueues = list()
    listOfNulls = list()
    global SHIFTS

    for matrix, nodeQueue, nullPnt in zip(matrixList, queueForEachMatrix, nullInEachMatrix):
        # print("\n", matrixList)
        # print(matrix)
        # print(queueForEachMatrix)
        # print(nodeQueue)
        # print(nullInEachMatrix)
        # print(nullPnt, "\n")

        for i in nodeQueue:
            newMatrix = deepcopy(matrix)

            # print("\nBefore:")
            # showMatrix(newMatrix)

            newMatrix[nullPnt[0]][nullPnt[1]] = newMatrix[i[0]][i[1]]
            newMatrix[i[0]][i[1]] = 0
            SHIFTS += 1

            # print("After:")
            # showMatrix(newMatrix)

            if newMatrix == pointSet:
                print("\n\n - - -\nLA FINALE\n - - -\n\n")
                showMatrix(newMatrix)
                print("Depth: ", depth)
                return
            else:
                newNullPnt = [i[0], i[1]]
                newShiftQueue = GenMoves(newNullPnt, nullPnt)

                listOfMatrixs.append(newMatrix)
                listOfQueues.append(newShiftQueue)
                listOfNulls.append(newNullPnt)

    layerScan(listOfMatrixs, listOfQueues, listOfNulls, depth + 1)


'''
print("""
            Меню

1. Выполнение программы
2. Пошаговое выполнение программы""")
ans = input("\n>>> ")
'''

#
# initSet = st.bs8
# pointSet = st.ts1
# nullPos = list()
# shiftQueue = list()
#
# nullPos = FindNull(initSet)
# shiftQueue = GenMoves(nullPos)
# showMatrix(initSet)
#
# initMatrix = list()
# initMatrix.append(initSet)
# initQueue = list()
# initQueue.append(shiftQueue)
# initNullPos = list()
# initNullPos.append(nullPos)
#
# layerScan(initMatrix, initQueue, initNullPos)