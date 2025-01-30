from nqueens import nqueens

def solves(solver, n):
    """
    Returns true if the function solver, when passed the number n, returns a legal solution to the n-queens puzzle.
    A legal solution should be an iterable (e.g., a list or tuple) of the integers 0 through n - 1. Each indicates
    the row of the queen in that column. A solution is legal if n queens are placed such that no two are on the same
    row, column, or diagonal.
    """
    solution = solver(n)
    if len(solution) != n:
        return False  # Solution wrong length
    if sorted(list(solution)) != list(range(n)):
        return False  # Solution doesn't contain each number exactly once
    for i in range(n):
        for j in range(i + 1, n):
            if solution[i] == solution[j]:
                return False  # Two queens in same row
            if abs(solution[i] - solution[j]) == j - i:
                return False  # Two queens on same diagonal
    return True


def test_3_queens():
    assert not nqueens(3)  # There is no solution

def test_5_queens():
    assert solves(nqueens, 5)

def test_8_queens():
    assert solves(nqueens, 8)

def test_20_queens():
    assert solves(nqueens, 20)
