# Sudoku game

# TODO What I need: TODO
# + Draw a board
# Each sq can have only 1 unique number
# Each column and row can have only 1 unique number
# Ability to edit numbers that you wrote
# Ability to choose difficulty levels, with dif. level will pre-write less numbers on the board.
# Every new game board numbers are randomised
# Victory is when each sq, column and row has unique numbers 1 to 9

import random


game_board_state = [0 for _ in range(36)]
# Splitting game_board_state into two lists of lists
board_state_1_of_2 = [game_board_state[i*6:i*6+6] for i in range(3)]
board_state_2_of_2 = [game_board_state[i*6:i*6+6] for i in range(3, 6)]
print(game_board_state)


def board_printing():
    # Game board printing function
    print("_____________________________")
    print("|---|---|---| - |---|---|---|")
    for i in board_state_1_of_2:
        i.insert(3, "|")
        print('|', ' | '.join(map(str, i)), '|')
        print("|---|---|---| - |---|---|---|")
    print("|SUDOKU SUDOKU SUDOKU SUDOKU|")
    print("|---|---|---| - |---|---|---|")
    for i in board_state_2_of_2:
        i.insert(3, "|")
        print('|', ' | '.join(map(str, i)), '|')
        print("|---|---|---| - |---|---|---|")
    print("=============================")

# >>> Randomisation <<<

# each square will have 4 numbers filled in
# each line, column and square can have only 1 same number

# checking if the first line can have that number


def new_game_board_state_randomisation(board_state_1, board_state_2, which_square):
    rng_number = random.randint(1, 9)
    rng_spot_in_a_line = random.randint(0, 6)
    rng_line_spot_up_to_2 = random.randint(0, 2)
    rng_line_spot_from_4 = random.randint(4, 6)
    if (
        board_state_1_of_2[0][rng_spot_in_a_line] == 0 and
        rng_number not in board_state_1_of_2[0] and
        rng_number not in board_state_1_of_2[1][:3] and
        rng_number not in board_state_1_of_2[2][:3] and
        rng_number not in (board_state_2_of_2[0][rng_spot_in_a_line], board_state_2_of_2[1]
                           [rng_spot_in_a_line], board_state_2_of_2[2][rng_spot_in_a_line])
    ):
        board_state_1_of_2[0][rng_spot_in_a_line] = rng_number
    # -- board_state_1
    else:
        print("fail")
        print(rng_number)


def checking_if_new_game_board_state_is_generated():
    # Checking if all squares have been prefilled with 4 numbers that are != 0

    # Count the occurrences of values not equal to 0
    first_square_numbers = sum(1 for value in (
        board_state_1_of_2[0][:3] + board_state_1_of_2[1][:3] + board_state_1_of_2[2][:3]) if value != 0)

    second_square_numbers = sum(1 for value in (
        board_state_1_of_2[0][3:] + board_state_1_of_2[1][3:] + board_state_1_of_2[2][3:]) if value != 0)

    third_square_numbers = sum(1 for value in (
        board_state_2_of_2[0][:3] + board_state_1_of_2[1][:3] + board_state_2_of_2[2][:3]) if value != 0)

    forth_square_numbers = sum(1 for value in (
        board_state_2_of_2[0][3:] + board_state_1_of_2[1][3:] + board_state_2_of_2[2][3:]) if value != 0)

    # Check if at least 4 numbers are not equal to 0 in each square
    if first_square_numbers and second_square_numbers and third_square_numbers and forth_square_numbers >= 4:
        # TODO need a switch to turn off randomisation
        pass


def test(picked_line_index, every_index_of_a_current_line, posible_lines):
    if picked_line_index in posible_lines:
        # Sqaure 1:
        if every_index_of_a_current_line[:(picked_line_index+3)]:
            if all(game_board_state[i] != 0 for i in sq_1) >= 4:
                return True
            else:
                return False
        # Sqaure 2:
        elif every_index_of_a_current_line[(picked_line_index+3):(picked_line_index[+6])]:
            if all(game_board_state[i] != 0 for i in sq_2) >= 4:
                return True
            else:
                return False
        # Sqaure 3:
        elif every_index_of_a_current_line[:(picked_line_index+3)]:
            if all(game_board_state[i] != 0 for i in sq_3) >= 4:
                return True
            else:
                return False
        # Sqaure 4:
        elif every_index_of_a_current_line[(picked_line_index+3):(picked_line_index[+6])]:
            if all(game_board_state[i] != 0 for i in sq_4) >= 4:
                return True
            else:
                return False
# >>> Line checking:
# 1. +, randomly pick a line (0,3,6,18,21 or 24)
# 2. +, check if in any possition of that line already has a number that we want to add to Sudoku (exmaple: line 3 picked, check if possitionsalready have that number (3, 3+1, 3+2, 3+9, 3+10, 3+11))
# 3. give True/False
# 4. -- ONLY for generating new game!: pick one position of a line 3 (example: randomly from a list [3,3+1,3+2,3+9,3+10,3+11]), return that positions number.


def line_and_square_checking(desired_number, game_board_state):
    posible_lines = [0, 6, 12, 18, 25, 30]
    picked_line_index = random.choice(posible_lines)
    # Indexes of the current line:
    every_index_of_a_current_line = [picked_line_index, picked_line_index+1,
                                     picked_line_index+2, picked_line_index+3, picked_line_index+4, picked_line_index+5]
    # Sqaures checking variabals:
    state = [game_board_state[picked_line_index], game_board_state[picked_line_index+1], game_board_state[picked_line_index+2],
             game_board_state[picked_line_index+3], game_board_state[picked_line_index+4], game_board_state[picked_line_index+5]]
    sq_1_indexes = [game_board_state[0], game_board_state[1], game_board_state[2], game_board_state[6],
                    game_board_state[7], game_board_state[8], game_board_state[12], game_board_state[13], game_board_state[14]]
    sq_2_indexes = [game_board_state[3], game_board_state[4], game_board_state[5], game_board_state[9],
                    game_board_state[10], game_board_state[11], game_board_state[15], game_board_state[16], game_board_state[17]]
    sq_3_indexes = [game_board_state[18], game_board_state[19], game_board_state[20], game_board_state[24],
                    game_board_state[25], game_board_state[26], game_board_state[30], game_board_state[31], game_board_state[32]]
    sq_4_indexes = [game_board_state[21], game_board_state[22], game_board_state[23], game_board_state[27],
                    game_board_state[28], game_board_state[29], game_board_state[33], game_board_state[34], game_board_state[35]]
    is_square_full = test(
        picked_line_index, every_index_of_a_current_line, posible_lines)
    if is_square_full == False:
        # >>> LINE CHECKING: <<<
        # Checking if the desired number IS NOT already in that line:
        if desired_number not in state:
            # Generating a random idex on the choosen line:
            picked_index_from_rng_line = random.choice(
                every_index_of_a_current_line)

            # >>> SQAURE CHECKING: <<<
            # Sqaure 1
            if picked_index_from_rng_line in range(0, 3) or picked_index_from_rng_line in range(6, 9) or picked_index_from_rng_line in range(12, 15):
                if desired_number not in sq_1_indexes:
                    # it is possible to write desired_number in that square.
                    column_checking(desired_number, game_board_state,
                                    picked_index_from_rng_line)
                    return game_board_state
            # Sqaure 2
            elif picked_index_from_rng_line in range(3, 6) or picked_index_from_rng_line in range(9, 12) or picked_index_from_rng_line in range(15, 18):
                if desired_number not in sq_2_indexes:
                    # it is possible to write desired_number in that square.
                    column_checking(desired_number, game_board_state,
                                    picked_index_from_rng_line)
                    return game_board_state
            # Sqaure 3
            elif picked_index_from_rng_line in range(18, 21) or picked_index_from_rng_line in range(24, 27) or picked_index_from_rng_line in range(30, 33):
                if desired_number not in sq_3_indexes:
                    # it is possible to write desired_number in that square.
                    column_checking(desired_number, game_board_state,
                                    picked_index_from_rng_line)
                    return game_board_state
            # Sqaure 4
            elif picked_index_from_rng_line in range(21, 24) or picked_index_from_rng_line in range(27, 30) or picked_index_from_rng_line in range(33, 36):
                if desired_number not in sq_4_indexes:
                    # it is possible to write desired_number in that square.
                    column_checking(desired_number, game_board_state,
                                    picked_index_from_rng_line)
                    return game_board_state


def column_checking(desired_number, game_board_state, picked_index_from_rng_line):
    column_1_indexes = [0, 6, 12, 18, 24, 30]
    column_1_ready_for_checking = []
    for i in column_1_indexes:
        column_1_ready_for_checking.append(game_board_state[i])

    column_2_indexes = [1, 7, 13, 19, 25, 31]
    column_2_ready_for_checking = []
    for i in column_2_indexes:
        column_2_ready_for_checking.append(game_board_state[i])

    column_3_indexes = [2, 8, 14, 20, 26, 32]
    column_3_ready_for_checking = []
    for i in column_3_indexes:
        column_3_ready_for_checking.append(game_board_state[i])

    column_4_indexes = [3, 9, 15, 21, 27, 33]
    column_4_ready_for_checking = []
    for i in column_4_indexes:
        column_4_ready_for_checking.append(game_board_state[i])

    column_5_indexes = [4, 10, 16, 22, 28, 34]
    column_5_ready_for_checking = []
    for i in column_5_indexes:
        column_5_ready_for_checking.append(game_board_state[i])

    column_6_indexes = [5, 11, 17, 23, 29, 35]
    column_6_ready_for_checking = []
    for i in column_6_indexes:
        column_6_ready_for_checking.append(game_board_state[i])

    if picked_index_from_rng_line in column_1_indexes:
        if desired_number not in column_1_ready_for_checking:
            game_board_state[picked_index_from_rng_line] = desired_number
            return game_board_state

    elif picked_index_from_rng_line in column_2_indexes:
        if desired_number not in column_2_ready_for_checking:
            game_board_state[picked_index_from_rng_line] = desired_number
            return game_board_state

    elif picked_index_from_rng_line in column_3_indexes:
        if desired_number not in column_3_ready_for_checking:
            game_board_state[picked_index_from_rng_line] = desired_number
            return game_board_state

    elif picked_index_from_rng_line in column_4_indexes:
        if desired_number not in column_4_ready_for_checking:
            game_board_state[picked_index_from_rng_line] = desired_number
            return game_board_state

    elif picked_index_from_rng_line in column_5_indexes:
        if desired_number not in column_5_ready_for_checking:
            game_board_state[picked_index_from_rng_line] = desired_number
            return game_board_state

    elif picked_index_from_rng_line in column_6_indexes:
        if desired_number not in column_6_ready_for_checking:
            game_board_state[picked_index_from_rng_line] = desired_number
            return game_board_state


# While loop for pre-filling the board with nubmers
switch = True
while switch:
    desired_number = random.randint(1, 9)
    if sum(num != 0 for num in game_board_state) >= 16:
        board_printing()
        switch = False
        print(game_board_state)
        break
    line_and_square_checking(
        desired_number, game_board_state)
    board_state_1_of_2 = [game_board_state[i*6:i*6+6] for i in range(3)]
    board_state_2_of_2 = [game_board_state[i*6:i*6+6] for i in range(3, 6)]
