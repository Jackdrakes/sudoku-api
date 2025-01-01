import random
import numpy as np

# Function to check if placing a number at a position is valid
def is_valid(board, row, col, num) -> bool:
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def fill_board(board, max_depth=1000, depth=0) -> bool:
    # Avoid deep recursion by limiting the depth
    if depth > max_depth:
        return False  # Terminate if we exceed the max depth

    empty = find_empty_cell(board)
    if not empty:
        return True  # Puzzle is solved

    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)  # Shuffle the numbers to avoid deterministic solutions

    for num in nums:
        if is_valid(board, row, col, num):
            board[row][col] = num
            if fill_board(board, max_depth, depth + 1):
                return True
            board[row][col] = 0  # Reset if no valid number is found

    return False


# Function to find an empty cell (represented by 0)
def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Function to generate a Sudoku puzzle
def generate_sudoku(difficulty: str):
    # Start with an empty board
    board = np.zeros((9, 9), dtype=int)

    # Fill the board with a valid solution
    fill_board(board)

    # Define number of clues based on difficulty
    if difficulty == "easy":
        clues = 36 
    elif difficulty == "intermediate":
        clues = 30  
    elif difficulty == "hard":
        clues = 24  
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'intermediate', or 'hard'.")

    # Remove cells to create the puzzle
    puzzle = board.copy()
    cells_to_remove = 81 - clues

    while cells_to_remove > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:  # Ensure that the cell has a value to remove
            puzzle[row][col] = 0
            cells_to_remove -= 1

    return puzzle.tolist()
