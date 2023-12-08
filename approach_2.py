# Second idea how to do a SUDOKU project better

""" 
    >>>> General overview of the game <<<<

    - Player input: 
        1. Prefilled/generated numbers can not be edited.
        2.Player will have a list of indexes, that he will need to enter in order to start filling in the desired number.
            Example:
                1 2 3
                4 5 6
                7 8 9
            Players enters 1, so now if the number was not pre-generated he will be able to write what number he wants to put there (only digits 1 to 9).

    - Random generation:
        - It will generate for 2 states. One for pre-filling numbers and another one for storing the solution of the game, to which we will compare if the game is won/completed.

    - Difficulty sellection :
        - It will enable different switches, that will be used for generation of the game board size.
            Expected game difficulties:
                Easy -> 1 big square(9 small)
                Medium -> 4 big squares(36 small)
                Hard -> 9 big squares(81 small)

    - Board printing:
        board_printing():
            check_how_many_digits in board_state_list
            print accordingly
    
    - Game Start:
        - Picking where to pre-fill/generate numbers:
            1. Program will keep the track of all indexes where the each line starts.
            2. Random number from 1 to 9 will be pick.
            3. Random line start index will be picked.
            4. Random index of the line will be picked.
            5. Number availability will be checked:
                1. Square checking
                2. Line checking
                3. Column checking
            6. If all checks are passed, number is placed in.

    - Square availability checking:
        ?. Hardcode what are the indexes of each square???
            Example:
                0  1  2  3  4  5
                6  7  8  9  10 11
                12 13 14 15 16 17

                Sqaure_1 = 0,1,2,6,7,8,12,13.14
        ?. Another solution is to have multiple lists for each square, where each list would have 9 spots and when checking lines/clomumn - combine them/check specific spots of each. This approach will require to still keep one Main_Board_State and each square would mirror a designated part of it.
        
    - Line availability checking:
        1. Each line will have to have unique numbers (1 to 9).
        2. Selected line will be checked, by addings digits to the starting digit.
            Example:
                1. Line with an index "0" has been selected
                2. so we check (0),(0+1),(0+2)... 
        3. If desired number does not exist, it can be placed in.

    - Column availability checking:
        1. Each column will have to have unique numbers (1 to 9).
        2. A dictionary will be used to select the column to be checked. Dictionary KEYS will be indexes of the selected line, and VALUES will be coresponding column start indexes.
            Example:
                0 1 3
                4 5 6
                7 8 9

                1. picked line index = 4
                2. dictionary contains = {4:0, 4+1:0+1,...}

        >> Posibility to combine line and column checking into one???

    - Main Menu options:
        1. New Game:
            1.Easy
            2.Normal
            3.Hard
            4.Back
        2. Rules of Sudoku:
            1.Prints out the rule set
            2.Back
        3. Exit Game:
            1.Are you sure you want to exit?
            2.Y/N
 """
