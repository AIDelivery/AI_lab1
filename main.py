import states
from problem import eightPuzzleProblem

initMatrix = states.bs8
targetMatrix = states.ts1
# tempMatrix = [[1, 2, 3],[4, 6, 0],[7, 5, 8]]

def main():

    problem = eightPuzzleProblem(initMatrix, targetMatrix)
    print(problem.iterativeDLS(100))
    # print(problem.runBFS())


if __name__ == "__main__":
    main()