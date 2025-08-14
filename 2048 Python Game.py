#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import os

SIZE = 4

def init_board():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if not empty_cells:
        return
    r, c = random.choice(empty_cells)
    board[r][c] = 2 if random.random() < 0.9 else 4

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---- 2048 Game ----\nUse W/A/S/D to move, Q to quit\n")
    for row in board:
        print("\t".join(str(num) if num != 0 else "." for num in row))
    print()

def slide_and_merge(row):
    # Remove zeros
    filtered = [num for num in row if num != 0]
    merged = []
    skip = False
    for i in range(len(filtered)):
        if skip:
            skip = False
            continue
        if i + 1 < len(filtered) and filtered[i] == filtered[i + 1]:
            merged.append(filtered[i] * 2)
            skip = True
        else:
            merged.append(filtered[i])
    merged += [0] * (SIZE - len(merged))
    return merged

def move_left(board):
    new_board = [slide_and_merge(row) for row in board]
    return new_board

def move_right(board):
    new_board = [slide_and_merge(row[::-1])[::-1] for row in board]
    return new_board

def move_up(board):
    transposed = list(zip(*board))
    moved = [slide_and_merge(list(row)) for row in transposed]
    return [list(row) for row in zip(*moved)]

def move_down(board):
    transposed = list(zip(*board))
    moved = [slide_and_merge(list(row[::-1]))[::-1] for row in transposed]
    return [list(row) for row in zip(*moved)]

def can_move(board):
    for r in range(SIZE):
        for c in range(SIZE):
            if board[r][c] == 0:
                return True
            if c + 1 < SIZE and board[r][c] == board[r][c + 1]:
                return True
            if r + 1 < SIZE and board[r][c] == board[r + 1][c]:
                return True
    return False

def main():
    board = init_board()
    while True:
        print_board(board)
        move = input("Move (W/A/S/D): ").lower()
        if move == 'q':
            print("Thanks for playing!")
            break

        new_board = None
        if move == 'a':
            new_board = move_left(board)
        elif move == 'd':
            new_board = move_right(board)
        elif move == 'w':
            new_board = move_up(board)
        elif move == 's':
            new_board = move_down(board)

        if new_board and new_board != board:
            board = new_board
            add_new_tile(board)

        if not can_move(board):
            print_board(board)
            print("Game Over!")
            break

if __name__ == "__main__":
    main()

