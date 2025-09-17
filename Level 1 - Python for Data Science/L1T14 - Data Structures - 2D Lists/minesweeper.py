# write a minesweeper program using a random sized square matrix
# the program should ask the user for the size of the matrix and then create a random matrix of that size
# use character - to represent a clear space and # to represent a mine
# write functions to:
#  create the playing board
#  determine the number of mines in the surrounding cells
# the program should output the playing board showing the mines and the number of mines in the surrounding cells

# request user input for the size of the square game board
num_rows = int(input("Please enter the size of the game board you wish to play: "))
num_cols = num_rows
print()

import random
import copy

# create the playing board with random placement of mines
def generate_game_board(num_rows, num_cols):
    return [[random.choice(['-', '#']) for j in range(num_cols)] for i in range(num_rows)]

# create the game board in a fixed variable to avoid calling the function again
game_board = generate_game_board(num_rows, num_cols)

# create a copy of the game board whilst leaving the original unchanged
display_board = copy.deepcopy(game_board)

# loop through the display board and either
#  leave unchanged if there is a mine in the cell
#  OR
#  print the number of mines in the surrounding cells

for row in range(num_rows):
    for col in range(num_cols):
        if display_board[row][col] == '#':
            continue
        count = 0
        if row > 0 and col > 0 and display_board[row - 1][col - 1] == '#':  # Top-left
            count += 1
        if row > 0 and display_board[row - 1][col] == '#':  # Top
            count += 1
        if row > 0 and col < num_cols - 1 and display_board[row - 1][col + 1] == '#':  # Top-right
            count += 1
        if col > 0 and display_board[row][col - 1] == '#':  # Left
            count += 1
        if col < num_cols - 1 and display_board[row][col + 1] == '#':  # Right
            count += 1
        if row < num_rows - 1 and col > 0 and display_board[row + 1][col - 1] == '#':  # Bottom-left
            count += 1
        if row < num_rows - 1 and display_board[row + 1][col] == '#':  # Below
            count += 1
        if row < num_rows - 1 and col < num_cols - 1 and display_board[row + 1][col + 1] == '#':  # Bottom-right
            count += 1
        display_board[row][col] = str(count)

# print the game board displaying - for no mine and # for a mine
print('Game Board:')
for row in game_board:
    print(' '.join(row))
print()

# print the game displaying the mines and the empty cells containing the number of mines in the surrounding cells
print("Solution: ")
for row in display_board:
    print(' '.join(row))