#Game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-',]

#Game still going
game_still_going = True

#Who win or tie?
winner = None

#Whos turn is it?
current_player = "X"

#------------------------------------

#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#Handle a single turn
def turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9 ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Incorrect. Choose a position from 1 to 9 again ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Choose another position.")

    board[position] = player
    display_board()


def play_game():
    # Display the board
    display_board()

    while game_still_going:
        # Make a move
        turn(current_player)

        check_if_game_over()

        flip_player()

    #End of the game
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie. ")


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #Global variable
    global winner
    #Check rows
    row_winner = check_rows()

    #Check columns
    column_winner = check_columns()

    #Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    global game_still_going
    #Check if any of these rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If any row has match, flag there's a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    #Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_still_going
    #Check if any of these columns have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #If any column has match, flag there's a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    #Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going
    #Check if any of these diagonals have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    #If any diagonal has match, flag there's a win
    if diagonal_1 or diagonal_2 :
        game_still_going = False
    #Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player
    #Changing players from X to O
    if current_player == "X":
        current_player = "O"
    #Changing players from O to X
    elif current_player == "O":
        current_player = "X"
    return






play_game()
