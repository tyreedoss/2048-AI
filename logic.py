# logic.py contains all functions necessary for game
# import random package to generate random numbers
import random


# function to initialize game/grid at start
def start_game():
    # declare empty list then append 4 lists
    # each with 4 elements (0)
    mat = []
    for i in range(4):
        mat.append([0] * 4)
    # call function to add a new 2
    # after every step
    add_new_2(mat)
    return mat


# function to add a new 2 in grid at any
# random empty cell
def add_new_2(mat):
    # choosing random index for
    # row and column
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    # while loop breaks as the
    # random cell chosen will be empty
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    # place a 2 at that random empty cell
    mat[r][c] = 2


# function to get current state of game
def get_current_state(mat):
    # if any cell contains 2048, player wins
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
    # if there is still at least one empty cell, game continues
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'

    # or if no cell is empty, but moving in any direction causes two cells to merge
    # and create an empty cell, game continues
    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i + 1][j] or mat[i][j] == mat[i][j + 1]:
                return 'GAME NOT OVER (swipe)'
    for j in range(3):
        if mat[3][j] == mat[3][j + 1]:
            return 'GAME NOT OVER (swipe)'
    for i in range(3):
        if mat[i][3] == mat[i + 1][3]:
            return 'GAME NOT OVER (swipe)'
    # else, the player loses
    return 'LOST'


# function to compress the grid after every step
def compress(mat):
    # bool variable to determine whether anything changed
    changed = False
    # empty grid
    new_mat = []
    # with all cells empty
    for i in range(4):
        new_mat.append([0] * 4)
    # shift entries of each cell to its extreme left row by row
    # loop to traverse rows
    for i in range(4):
        pos = 0
        # loop to traverse each column in its respective row
        for j in range(4):
            if mat[i][j] != 0:
                # if cell is not empty then shift its number to previous
                # empty cell in that row (denoted by pos)
                new_mat[i][pos] = mat[i][j]

                if j != pos:
                    changed = True
                pos += 1
    # returns the new compressed matrix and flag variable
    return new_mat, changed


# function to merge the cells in matrix after compressing
def merge(mat):
    changed = False

    for i in range(4):
        for j in range(3):
            # if current cell has same value as next cell in the row and they
            # are not empty then
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                # double current cell value and
                # empty the next cell
                mat[i][j] = mat[i][j] * 2
                mat[i][j + 1] = 0
                # make bool variable True indicating the
                # new grid after merging is different
                changed = True

    return mat, changed


# function to reverse the sequence of the content in each row
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat


# function to get the transpose of matrix
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat


# function to update the matrix if moved left
def move_left(grid):
    # first compress grid
    new_grid, changed1 = compress(grid)
    # then merge cells
    new_grid, changed2 = merge(new_grid)
    changed = changed1 or changed2
    # compress again after merging
    new_grid, temp = compress(new_grid)
    # return new matrix and bool changed telling
    # whether the grid is the same or different
    return new_grid, changed


# function to update the matrix if moved right
def move_right(grid):
    # reverse matrix
    new_grid = reverse(grid)
    # move left
    new_grid, changed = move_left(new_grid)
    # reverse again
    new_grid = reverse(new_grid)
    return new_grid, changed


# function to update the matrix if moved up
def move_up(grid):
    # take the transpose of the matrix
    new_grid = transpose(grid)
    # move left
    new_grid, changed = move_left(new_grid)
    # take transpose again
    new_grid = transpose(new_grid)
    return new_grid, changed


# function to update the matrix if moved down
def move_down(grid):
    # take transpose
    new_grid = transpose(grid)
    # move right
    new_grid, changed = move_right(new_grid)
    # transpose again
    new_grid = transpose(new_grid)

    return new_grid, changed


# this file only contains all the logic functions to be called
# in the main function present in other file
