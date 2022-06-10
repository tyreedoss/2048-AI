# importing the logic.py file where
# all the logic functions are
import logic
# setting a variable to 'GAME NOT OVER' to compress code
cont = 'GAME NOT OVER'
cont2 = 'GAME NOT OVER (swipe)'
# Driver code
if __name__ == '__main__':
    # call start_game function to initialize matrix
    mat = logic.start_game()
    # print the matrix as a list containing four lists
    # each list on its own line
    print(*mat, sep='\n')

    while True:
        # take the user input for next step
        x = input("Press the command: ")
        # 'w' or 'W' means move up
        if x.upper() == 'W':
            # call move up function
            mat, flag = logic.move_up(mat)
            # get the current state and print it
            status = logic.get_current_state(mat)
            print(status)
            # if at least one zero, then continue and add a new 2
            if status == cont:
                logic.add_new_2(mat)
            # if adjacent/equal numbers, game continues
            elif status == cont2:
                pass
            # else, break the loop and print matrix and status
            else:
                print(status)
                print(*mat, sep='\n')
                break
        # 'S' or 's' means move down
        elif x.upper() == 'S':
            mat, flag = logic.move_down(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == cont:
                logic.add_new_2(mat)
            elif status == cont2:
                pass
            else:
                print(status)
                print(*mat, sep='\n')
                break
        # move left
        elif x.upper() == 'A':
            mat, flag = logic.move_left(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == cont:
                logic.add_new_2(mat)
            elif status == cont2:
                pass
            else:
                print(status)
                print(*mat, sep='\n')
                break
        # move right
        elif x.upper() == 'D':
            mat, flag = logic.move_right(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == cont:
                logic.add_new_2(mat)
            elif status == cont2:
                pass
            else:
                print(status)
                print(*mat, sep='\n')
                break
        # if character other than w, a, s, or d, then input another value
        else:
            print('Invalid key pressed')
        # print matrix after every move
        print(*mat, sep='\n')
