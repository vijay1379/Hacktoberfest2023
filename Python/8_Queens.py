def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0

    return False

def print_board(board):
    for row in board:
        print(" ".join(["Q" if cell else "." for cell in row]))

def solve_eight_queens():
    board = [[0 for _ in range(8)] for _ in range(8)]

    if not solve_n_queens(board, 0):
        print("Solution does not exist.")
        return

    print_board(board)

solve_eight_queens()
