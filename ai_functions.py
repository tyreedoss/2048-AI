# this file contains all the tactic/decisions implemented by the main AI
# import the logic file to move elements in the matrix
import logic


# function to find the sum of the five highest values in the matrix
def mat_sum(mat):
    # create empty list
    rank = []
    # copy the matrix into rank, from highest to lowest value
    for x in range(4):
        for y in range(4):
            rank.append(mat[x][y])
            rank.sort(reverse=True)
    # add the first five numbers of rank together and return the sum
    total = 0
    for z in range(5):
        total = total + rank[z]
    return total


# function to find the highest 'total' of the six possible moves
def best_option(options):
    best = None
    for x in range(6):
        if best is None or options[x] > best:
            best = options[x]
    return best


# function to check if the top row contains a zero
# or if two adjacent numbers are equivalent
def check_row_zero(mat):
    # any zeros?
    for j in range(4):
        if mat[0][j] == 0:
            return False
    # two adjacent numbers equal?
    for j in range(3):
        if mat[0][j] == mat[0][j+1]:
            return False
    else:
        return True


# this tactic will move up if two numbers are found to be equal in the same column
def tactic_one(mat):
    # create counter variable for traversing columns
    col = 3
    # set the total of tactic one to 0
    total1 = 0
    while col >= 0:
        for i in range(3):
            # if two adjacent numbers in the same column are equal and nonzero, move up
            if mat[i][col] == mat[i + 1][col] and mat[i][col] != 0:
                mat, flag = logic.move_up(mat)
                status = logic.get_current_state(mat)
                # if the move up does not result in the game ending, then add
                # a new 2 and return the sum of five highest values
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total1 = mat_sum(mat)
                    return total1
                # if game ends as result of move, return 0
                else:
                    return 0
            # if in the same column, a number in the first row equals a number in the fourth row
            # and both are nonzero, and the numbers in the first and second rows are zero, move up
            elif mat[0][col] == mat[3][col] and mat[1][col] == 0 and mat[2][col] == 0 and mat[0][col] != 0:
                mat, flag = logic.move_up(mat)
                status = logic.get_current_state(mat)
                if status == "GAME NOT OVER":
                    logic.add_new_2(mat)
                    total1 = mat_sum(mat)
                    return total1
                else:
                    return 0
            # if number in first row equals number in third row, separated by a zero, move up
            elif mat[0][col] == mat[2][col] and mat[1][col] == 0 and mat[0][col] != 0:
                mat, flag = logic.move_up(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total1 = mat_sum(mat)
                    return total1
                else:
                    return 0
            # if number in second row equals number in fourth row separated by zero, move up
            elif mat[1][col] == mat[3][col] and mat[2][col] == 0 and mat[1][col] != 0:
                mat, flag = logic.move_up(mat)
                status = logic.get_current_state(mat)
                if status == "GAME NOT OVER":
                    logic.add_new_2(mat)
                    total1 = mat_sum(mat)
                    return total1
                else:
                    return 0
            # if none of these conditions are true, continue to next column (right to left)
            else:
                continue
        col -= 1
    return total1


# this tactic will move right if two numbers are equal in the same row
def tactic_two(mat):
    # counter variable to traverse rows
    row = 0
    total2 = 0
    while row <= 3:
        for j in range(3):
            # if two adjacent, nonzero numbers in the same row are equal, move right
            if mat[row][j] == mat[row][j + 1] and mat[row][j] != 0:
                mat, flag = logic.move_right(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total2 = mat_sum(mat)
                    return total2
                else:
                    return 0
            # nonzero numbers in the first and third column separated by zero
            elif mat[row][0] == mat[row][2] and mat[row][1] == 0 and mat[row][0] != 0:
                mat, flag = logic.move_right(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total2 = mat_sum(mat)
                    return total2
                else:
                    return 0
            # numbers in first and fourth column separated by two zeros
            elif mat[row][0] == mat[row][3] and mat[row][1] == 0 and mat[row][2] == 0 and mat[row][0] != 0:
                mat, flag = logic.move_right(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total2 = mat_sum(mat)
                    return total2
                else:
                    return 0
            # number in second and fourth column separated by zero
            elif mat[row][1] == mat[row][3] and mat[row][2] == 0 and mat[row][1] != 0:
                mat, flag = logic.move_right(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total2 = mat_sum(mat)
                    return total2
                else:
                    return 0
            else:
                continue

        row += 1
    return total2


# tactic three will move left if a number to the far left is the sum
# of two equal numbers to the right of it
def tactic_three(mat):
    # this function will only execute if there are no zeros
    # in the top row or equal/adjacent numbers
    green = check_row_zero(mat)
    # if there are no zeros or equal/adjacent #'s:
    if green:
        # will iterate over the bottom three rows, and specify the columns
        for i in range(1, 3):
            # if a nonzero number in the second column equals a number in the third
            # and the number in the first column is the sum of both numbers
            # move left
            if mat[i][2] == mat[i][1] and mat[i][2] != 0 and mat[i][0] == 2 * mat[i][2]:
                mat, flag = logic.move_left(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total3 = mat_sum(mat)
                    return total3
                else:
                    return 0
                # number in fourth column equal to number in third, second column number
                # is the sum, move left
            elif mat[i][3] == mat[i][2] and mat[i][3] != 0 and mat[i][1] == 2 * mat[i][2]:
                mat, flag = logic.move_left(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total3 = mat_sum(mat)
                    return total3
                else:
                    return 0
                # number in fourth column equals number in third, number in second column is zero,
                # number in first column is sum, move left
            elif mat[i][3] == mat[i][2] and mat[i][1] == 0 and mat[i][3] != 0 and mat[i][0] == 2 * mat[i][2]:
                mat, flag = logic.move_left(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total3 = mat_sum(mat)
                    return total3
                else:
                    return 0
            # if no conditions are true, will return zero
            else:
                return 0
    # if green is not True, will return zero
    else:
        return 0


# this tactic will move the matrix left and then up if there is a number
# in the first row equal to a number in the second row, one column to the
# right of it (diagonal)
def tactic_four(mat):
    # will only execute if there are no zeros or adjacent/equal
    # numbers in the top row
    green = check_row_zero(mat)
    if green:
        # count the number of zeroes in second row
        zeros_row_one = 0
        for j in range(3):
            if mat[1][j] == 0:
                zeros_row_one += 1
        # will iterate through columns 2-4 (1-3), and specify rows
        # one and two (0 and 1)
        for j in range(1, 3):
            # if a number in the second row is equal to a number one space
            # to the left and one space upward, and there is one zero
            # in the second row, first move left:
            if mat[1][j] == mat[0][j - 1] and zeros_row_one == 1:
                mat, flag = logic.move_left(mat)
                status = logic.get_current_state(mat)
                # check that the game is not over
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                else:
                    return 0
                # then move up
                new_mat4a, flag = logic.move_up(mat)
                status = logic.get_current_state(new_mat4a)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(new_mat4a)
                    total4 = mat_sum(new_mat4a)
                    return total4
                else:
                    return 0
            # will return zero if condition does not occur
            else:
                return 0
    # returns 0 if zeroes in top row or adjacent/equal numbers
    else:
        return 0


# this tactic is similar to tactic four, except it looks for matching numbers
# in the second and third rows
def tactic_five(mat):
    # will only run if no zeroes or adjacent/equal numbers in the top row
    green = check_row_zero(mat)
    if green:
        # count zeroes in row two and three
        zeroes_row_one = 0
        zeroes_row_two = 0
        for j in range(3):
            if mat[1][j] == 0:
                zeroes_row_one += 1
            if mat[2][j] == 0:
                zeroes_row_two += 1
        # will iterate through columns 2-4
        for j in range(1, 3):
            # if number in third row equals number in second row one space up and to the left
            # and there are no zeroes in the first or second row, and one zero in the third,
            # then first move left
            if mat[2][j] == mat[1][j - 1] and mat[2][j] >= 16 and mat[2][0] == 0 and zeroes_row_two == 1 and zeroes_row_one == 0:
                mat, flag = logic.move_left(mat)
                status = logic.get_current_state(mat)
                # check if game ended
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                else:
                    return 0
                # then move up
                mat, flag = logic.move_up(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    total5 = mat_sum(mat)
                    return total5
                else:
                    return 0
            else:
                return 0
    else:
        return 0


# this tactic looks if there is a number in the second row third column
# equal to a number in the first row, second column. there are two
# zeros to the left of the bottom number, then swiping up and left
# will line the numbers up
def tactic_six(mat):
    green = check_row_zero(mat)
    if green:
        # count number of zeros in first and second column
        zeros_column_zero = 0
        zeros_column_one = 0
        for i in range(3):
            if mat[i][0] == 0:
                zeros_column_zero += 1
            if mat[i][1] == 0:
                zeros_column_one += 1
        # if number in second row third column == num in first row second column,
        # there are at least three zeroes in first column, and at most two
        # zeroes in the second column
        if mat[1][2] == mat[0][1] and zeros_column_zero >= 3 and zeros_column_one <= 2:
            # first, if space next to bottom number
            # is zero, then move up
            if mat[1][1] == 0:
                mat, flag = logic.move_up(mat)
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                else:
                    return 0
            # left
            new_mat6a, flag = logic.move_left(mat)
            status = logic.get_current_state(new_mat6a)
            if status == 'GAME NOT OVER':
                logic.add_new_2(new_mat6a)
            else:
                return 0
            # up again to merge with number in top row
            new_mat6b, flag = logic.move_up(new_mat6a)
            status = logic.get_current_state(new_mat6b)
            if status == 'GAME NOT OVER':
                logic.add_new_2(new_mat6b)
                total6 = mat_sum(new_mat6b)
                return total6
            else:
                return 0
        else:
            return 0
    else:
        return 0
