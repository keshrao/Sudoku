# -*- coding: utf-8 -*-

import random
import time
from IPython import get_ipython

ipython = get_ipython()
cont_viz = False

def generate_sudoku(n=3):
    """ Generate a complete Sudoku board """
    N = n**2
    
    def create_board():
        return [[0 for _ in range(N)] for _ in range(N)]

    def is_valid(board, row, col, num):
        # Check row
        if num in board[row]:
            return False
        
        # Check column
        if num in [board[i][col] for i in range(N)]:
            return False
        
        # Check 3x3 box
        box_row, box_col = (row // n) * n, (col // n) * n
        if num in [board[i][j] 
                   for i in range(box_row, box_row + n) 
                   for j in range(box_col, box_col + n)]:
            return False
        
        return True

    def solve(board):
        for row in range(N):
            for col in range(N):
                if board[row][col] == 0:
                    for num in random.sample(range(1, N+1), N):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            
                            if cont_viz: 
                                visualize_board(board)
                                time.sleep(0.25)
                                
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    board = create_board()
    solve(board)
    return board


def print_board(board):
    ipython.magic('clear')
    n = int(len(board)**0.5)
    for i, row in enumerate(board):
        if i % n == 0 and i != 0:
            print("-" * (len(board) * 2 + 2 * n - 1))
        print(" ".join(
            "".join(str(num) if num != 0 else "." for num in row[j:j+n]) 
            for j in range(0, len(row), n)
        ))

def visualize_board(board):
    ipython.magic('clear')    
    print("+" + "---+" * 7)
    for i, row in enumerate(board):
        print("|", end="")
        for j, num in enumerate(row):
            if num == 0:
                print(" . ", end="")
            else:
                print(f" {num} ", end="")
            if (j + 1) % 3 == 0:
                print("|", end="")
        print()
        if (i + 1) % 3 == 0:
            print("+" + "---+" * 7)
        else:
            print("+" + "   +" * 7)


# Generate and print a Sudoku board
sudoku_board = generate_sudoku()
visualize_board(sudoku_board)