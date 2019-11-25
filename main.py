import states
from problem import EightPuzzleProblem

initMatrix = states.bs8
targetMatrix = states.ts1
# tempMatrix = [[1, 2, 3],[4, 6, 0],[7, 5, 8]]


def main():

    problem = EightPuzzleProblem(initMatrix, targetMatrix)
    problem.run_greedy(0)
    # problem.run_bfs()


if __name__ == "__main__":
    main()