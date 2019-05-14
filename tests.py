from solver import *


def test1():
    C = [[1, 1, 0, 0, 0],
         [1, 1, 1, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 1, 1, 1],
         [0, 0, 0, 1, 1]]

    F = [1, 1, 1, 1, 1]

    solution = ForwardSolver(C, F).count()
    print(solution)

if __name__ == '__main__':
    test1()
