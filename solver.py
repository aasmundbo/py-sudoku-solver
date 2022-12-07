"""
Solve sudokus
"""
from time import perf_counter

# Easy
# the_puzzle = [
#     [0, 0, 4, 0, 0, 0, 0, 7, 0],
#     [7, 6, 2, 5, 0, 0, 3, 4, 9],
#     [0, 0, 9, 0, 4, 3, 2, 0, 6],
#     [0, 3, 1, 0, 5, 8, 0, 0, 0],
#     [0, 7, 8, 0, 3, 2, 9, 1, 5],
#     [0, 0, 0, 9, 0, 0, 6, 0, 0],
#     [0, 0, 0, 0, 0, 0, 1, 3, 0],
#     [0, 0, 0, 0, 7, 4, 5, 0, 8],
#     [5, 0, 3, 0, 0, 0, 7, 6, 4],
# ]

# Hard
# the_puzzle = [
#     [9, 1, 0, 0, 0, 0, 0, 6, 0],
#     [0, 0, 0, 0, 0, 5, 0, 0, 0],
#     [0, 5, 0, 0, 0, 3, 0, 9, 0],
#     [0, 0, 2, 0, 9, 0, 4, 0, 0],
#     [0, 7, 9, 0, 0, 0, 0, 0, 0],
#     [0, 3, 0, 0, 6, 4, 0, 0, 0],
#     [7, 0, 0, 0, 0, 0, 0, 5, 8],
#     [0, 0, 0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 2, 5, 0, 3, 0, 4],
# ]

# Hard++
the_puzzle = [
    [2, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 3, 0, 0],
    [0, 0, 3, 9, 0, 0, 4, 5, 0],
    [0, 0, 6, 1, 0, 0, 0, 9, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 8, 0, 0, 0, 6, 1, 0, 0],
    [0, 9, 2, 0, 0, 7, 8, 0, 0],
    [0, 0, 7, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 5],
]

num_iterations = 0


def next_unsolved(puzzle: list, row: int = 0, col: int = 0) -> tuple:
    """Returns (row,col) tuple of next empty cell."""
    for curr_row, row_list in enumerate(puzzle[row:]):
        for curr_col, value in enumerate(row_list[col:]):
            if value == 0:
                return (curr_row, curr_col)

    # No next found -> return special value
    return (10, 10)


def valid_puzzle(puzzle: list, row: int, col: int, number: int) -> bool:
    """
    Check if number in location (row,col) is valid.
    """
    # Valid for row
    if number in puzzle[row]:
        return False

    # Valid for col
    for current_row in puzzle:
        if number == current_row[col]:
            return False

    # Valid for box
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for row_list in puzzle[row_start : row_start + 3]:
        if number in row_list[col_start : col_start + 3]:
            return False

    return True


def solve(puzzle: list) -> bool:
    """
    Solves Sudoku. Returns true if solution is found, false otherwise
    """
    global num_iterations
    num_iterations += 1

    row, col = next_unsolved(the_puzzle)
    if row == 10:
        # Solved!
        return True

    # Guess a number
    for num in range(1, 10):
        if valid_puzzle(puzzle, row, col, num):
            puzzle[row][col] = num
            if solve(puzzle):
                return True
            else:
                # No solution found, mark cell empty
                puzzle[row][col] = 0

    return False


def print_sudoku(puzzle: list) -> None:
    """Print sudoku board

    Parameters
    ----------
    puzzle : list
        The sudoku board
    """
    for row_idx, row_list in enumerate(puzzle):
        if row_idx % 3 == 0:
            print("+-------+-------+-------+")
        for col_idx, value in enumerate(row_list):
            if value == 0:
                value = " "
            if col_idx == 0:
                print(f"| {value} ", end="")
            elif col_idx == 8:
                print(f"{value} |")
            elif col_idx % 3 == 0:
                print(f"| {value} ", end="")
            else:
                print(f"{value} ", end="")

    print("+-------+-------+-------+")


def app():
    """
    Main application
    """
    global num_iterations

    print("Board:")
    print_sudoku(the_puzzle)

    solve(the_puzzle)

    print("Solution:")
    print_sudoku(the_puzzle)

    print(f"Found using {num_iterations} iterations")


start = perf_counter()
app()
end = perf_counter()
print(f"Execution time: {end-start:.3f} us")
