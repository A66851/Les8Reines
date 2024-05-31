import time
import sys


def isValide(combination, value):
    len_combination = len(combination)
    for i, v in enumerate(combination):
        if len_combination - i == abs(value -v):
            return False
    return True


def solve(possibleValues, combination=[], solutions=[]):
    if len(combination) == nQueens:
        solutions.append(combination)
    else:
        for value in possibleValues:
            if isValide(combination, value):
                solve(possibleValues - {value}, combination + [value], solutions)
    return solutions


if __name__ == '__main__':
    nQueens = 8 if len(sys.argv) == 1 else int(sys.argv[1])    
    possibleValues = set(range(nQueens))
    startTime = time.time()
    solutions = solve(possibleValues)
    elapsedTime = time.time() - startTime
    for i, sol in enumerate(solutions):
        print('Solution %2d: %s' % (i+1, sol))
    print('%10s => %8.2f msec. (%d solutions)' % (solve.__name__, 1000*elapsedTime, len(solutions)))
    