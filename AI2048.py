# import the logic functions and AI tactics
import logic
import ai_functions

if __name__ == '__main__':
    # initialize
    mat = logic.start_game()
    print(*mat, sep='\n')
    print('\n')

    # function to print matrix and direction swiped
    def print_mat(mat, dir):
        print(*mat, sep='\n')
        if dir == 'down':
            print('moved down \n')
        elif dir == 'up':
            print('moved up \n')
        elif dir == 'right':
            print('moved right \n')
        elif dir == 'left':
            print('moved left \n')

    # function to print matrix and status
    def lost(mat, status):
        print(*mat, sep='\n')
        print(status)
        print(f'Moves: {moves}')

    # count number of swipes
    moves = 0
    # begin by moving up and to the right fifteen times
    for i in range(15):
        mat, flag = logic.move_up(mat)
        logic.add_new_2(mat)
        moves += 1
        print(*mat, sep='\n')
        print('\n')
        mat, flag = logic.move_right(mat)
        logic.add_new_2(mat)
        moves += 1
        print(*mat, sep='\n', )
        print('\n')

    # main decisions of AI
    status = logic.get_current_state(mat)
    # will run until all spaces filled
    # and no equal/adjacent num's
    while status == 'GAME NOT OVER':
        # set variables for the total values from each tactic
        total1 = ai_functions.tactic_one(mat)
        total2 = ai_functions.tactic_two(mat)
        total3 = ai_functions.tactic_three(mat)
        total4 = ai_functions.tactic_four(mat)
        total5 = ai_functions.tactic_five(mat)
        total6 = ai_functions.tactic_six(mat)
        # declare list of values for each tactic
        options = [total1, total2, total3, total4, total5, total6]
        # move indicates the best tactic found with best_option
        move = ai_functions.best_option(options)
        # the matrix will change according to the value of move
        # it will complete the same movements detailed in
        # ai_functions
        # moves up
        if move == total1:
            mat, flag = logic.move_up(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'up')
                print('tactic 1')
            else:
                lost(mat, status)
                break
        # moves right
        elif move == total2:
            mat, flag = logic.move_right(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'right')
                print('tactic 2')
            else:
                lost(mat, status)
                break
        # moves left
        elif move == total3:
            mat, flag = logic.move_left(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'left')
                print('tactic 3')
            else:
                lost(mat, status)
                break
        # moves left then up
        elif move == total4:
            mat, flag = logic.move_left(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'left')
            else:
                lost(mat, status)
                print('tactic 4')
                break
            mat, flag = logic.move_up(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'up')
                print('tactic 4')
            else:
                lost(mat, status)
                print('tactic 4')
                break
        # moves left then up
        elif move == total5:
            mat, flag = logic.move_left(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'left')
            else:
                lost(mat, status)
                print('tactic 5')
                break
            mat, flag = logic.move_up(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'up')
                print('tactic 5')
            else:
                lost(mat, status)
                print('tactic 5')
                break
        # moves up, left, then up
        elif move == total6:
            if mat[1][1] == 0:
                mat, flag = logic.move_up(mat)
                moves += 1
                status = logic.get_current_state(mat)
                if status == 'GAME NOT OVER':
                    logic.add_new_2(mat)
                    print_mat(mat, 'up')
                else:
                    lost(mat, status)
                    print('tactic 6')
                    break
            mat, flag = logic.move_left(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'left')
            else:
                lost(mat, status)
                print('tactic 6')
                break
            mat, flag = logic.move_up(mat)
            moves += 1
            status = logic.get_current_state(mat)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
                print_mat(mat, 'up')
                print('tactic 6')
            else:
                lost(mat, status)
                print('tactic 6')
                break
        # if none of the conditions are true
        # or equal to zero will go right then up
        elif move == 0:
            mat, flag = logic.move_right(mat)
            status = logic.get_current_state(mat)
            moves += 1
            for i in range(4):
                for j in range(4):
                    if mat[i][j] == 0:
                        logic.add_new_2(mat)
            if status == 'GAME NOT OVER':
                print_mat(mat, 'right')
            else:
                lost(mat, status)
                break

            mat, flag = logic.move_up(mat)
            status = logic.get_current_state(mat)
            moves += 1
            for i in range(4):
                for j in range(4):
                    if mat[i][j] == 0:
                        logic.add_new_2(mat)
                        break
            if status == 'GAME NOT OVER':
                print_mat(mat, 'up')
            else:
                lost(mat, status)
                break

