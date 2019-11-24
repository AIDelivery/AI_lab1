import states
from problem import eightPuzzleProblem

# LAB2
from AI_lab2.problem_ext import eightPuzzleProblemExt

initMatrix = states.bs8
targetMatrix = states.ts1
# tempMatrix = [[1, 2, 3],[4, 6, 0],[7, 5, 8]]

def main():

    # problem = eightPuzzleProblem(initMatrix, targetMatrix)
    # print(problem.iterativeDLS(100))
    # print(problem.runBFS())

    # LAB2
    problemExt = eightPuzzleProblemExt(initMatrix, targetMatrix, 0)
    problemExt.greedy_search()


if __name__ == "__main__":
    main()