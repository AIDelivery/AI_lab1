from copy import deepcopy

nor = 3
noc = 3
SHIFTS = 0

"""
00 01 02
10 11 12
20 21 22
"""


# Get number of available moves from the current *state*
def NumOfMoves(state):
    if state[0] == state[1] == 1:
        return 4
    elif state[0] != 1 and state[1] != 1:
        return 2
    return 3


# Generates coordinates of available moves, except previous
def GenMoves(curState, prState):
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
def FindNull(matrix: list):
    res = -1

    for i in range(0, nor):
        try:
            res = matrix[i].index(0, 0, noc)
        except:
            continue

        return list([i, res])

    raise Exception("Error. There is no 0 in matrix...")


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