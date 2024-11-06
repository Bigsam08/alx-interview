#!/usr/bin/python3
''' n queens '''
import sys


def correct_move(board, row, col):
    ''' check if queen movement on board is correct'''
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j, in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def get_output(board):
    ''' display on the board'''
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def backtracking(board, col):
    ''' backtracking to solve nqueen problem'''
    if col >= len(board):
        get_output(board)
        return True

    result = False
    for i in range(len(board)):
        if correct_move(board, i, col):
            board[i][col] = 1
            result = backtracking(board, col + 1) or result
            board[i][col] = 0
    return result


def solve_nqueens(N):
    ''' solve N queen puzzle and get solutions'''
    board = [[0] * N for _ in range(N)]
    if not backtracking(board, 0):
        print("No solution exists")
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
