# Sudoku game

# --- What I need: ---
# + Draw a board
# Each sq can have only 1 unique number
# Each column and row can have only 1 unique number
# Ability to edit numbers that you wrote
# Ability to choose difficulty levels, with dif. level will pre-write less numbers on the board.
# Every new game board numbers are randomised
# Victory is when each sq, column and row has unique numbers 1 to 9

import random

# Preset of how the game will be printed line 1 to 6
line_1 = [0, 0, 0, "|", 0, 0, 0]
# line_2 = [0, 0, 0, "|", 0, 0, 0]
# line_3 = [0, 0, 0, "|", 0, 0, 0]
# line_4 = [0, 0, 0, "|", 0, 0, 0]
# line_5 = [0, 0, 0, "|", 0, 0, 0]
# line_6 = [0, 0, 0, "|", 0, 0, 0]


game_board_state = [0 for _ in range(36)]
# Presets split into two lists, each one prints 2 squares or 3 lines.
board_state_1_of_2 = [line_1.copy() for _ in range(3)]
board_state_2_of_2 = [line_1.copy() for _ in range(3)]


def board_printing():
    # Game board printing function
    print("_____________________________")
    print("|---|---|---| - |---|---|---|")
    for i in board_state_1_of_2:
        print('|', ' | '.join(map(str, i)), '|')
        print("|---|---|---| - |---|---|---|")
    print("|SUDOKU SUDOKU SUDOKU SUDOKU|")
    print("|---|---|---| - |---|---|---|")
    for i in board_state_2_of_2:
        print('|', ' | '.join(map(str, i)), '|')
        print("|---|---|---| - |---|---|---|")
    print("=============================")


# Resets board_state to zeros (line_1 integers to 0)
for i in range(len(line_1)):
    if isinstance(line_1[i], int):
        line_1[i] = 0

# --- Randomisation ---

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
        # need a switch to turn of randomisation
        pass

# >>> Line checking:
# 1. + randomly pick a line (0,3,6,18,21 or 24)
# 2. + check if in any possition of that line already has a number that we want to add to Sudoku (exmaple: line 3 picked, check if possitions (3, 3+1, 3+2, 3+9, 3+10, 3+11))
# 3. give True/False
# 4. -- ONLY for generating new game!: pick one position of a line 3 (example: randomly from a list [3,3+1,3+2,3+9,3+10,3+11]), return that positions number.


def line_checking(desired_number, game_board_state):
    posible_lines = [0, 3, 6, 18, 21, 24]
    picked_line_index = random.choice(posible_lines)
    every_index_of_a_current_line = [picked_line_index, picked_line_index+1,
                                     picked_line_index+2, picked_line_index+9, picked_line_index+10, picked_line_index+11]
    # Line checking variable:
    state = [game_board_state[picked_line_index], game_board_state[picked_line_index+1], game_board_state[picked_line_index+1],
             game_board_state[picked_line_index+2], game_board_state[picked_line_index+9], game_board_state[picked_line_index+10], game_board_state[picked_line_index+11]]
    # >>> LINE CHECKING: <<<
    # If a desired line does not already have desired_number, pick a random spot in that line:
    if desired_number not in state:
        picked_index_from_rng_line = random.choice(
            every_index_of_a_current_line)

        # >>> SQAURE CHECKING: <<<
        # Sqaure 1
        if picked_index_from_rng_line == (all(0 <= num <= 8 for num in picked_index_from_rng_line)):
            if desired_number not in game_board_state[:9]:
                # it possible to write desired_number in that square.
                pass
        # Sqaure 2
        elif picked_index_from_rng_line == (all(9 <= num <= 14 for num in picked_index_from_rng_line)):
            if desired_number not in game_board_state[8:18]:
                # it possible to write desired_number in that square.
                pass
        # Sqaure 3
        elif picked_index_from_rng_line == (all(18 <= num <= 26 for num in picked_index_from_rng_line)):
            if desired_number not in game_board_state[18:27]:
                # it possible to write desired_number in that square.
                pass
        # Sqaure 4
        elif picked_index_from_rng_line == (all(27 <= num <= 35 for num in picked_index_from_rng_line)):
            if desired_number not in game_board_state[27:]:
                # it possible to write desired_number in that square.
                pass


def column_checking(desired_number, game_board_state, picked_index_from_rng_line):
    start_index = picked_index_from_rng_line
    negative_index = -6
    positive_index = +6
    column_up_free = False
    column_down_free = False
    # checking column backwards/up:
    for i in range(start_index, len(my_list), negative_index):
        if game_board_state[i] == desired_number:
            break
        else:
            column_up_free = True

    # checking column forwards/down:
    for i in range(start_index, len(my_list), positive_index):
        if game_board_state[i] == desired_number:
            break
        else:
            column_down_free = True

    if (column_up_free and column_down_free) == True:
        pass
