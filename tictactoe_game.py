#Tic Tac Toe Game - Final Project Application Development
#@authors Ryan Carney, Harrison Bruce, Ethan Pyles

#----------Structure-----------

#disp_selections - Prints available selections
#disp_board - Prints the game board
#play - Starts the game
#make_turn - Allows the player to make a selection on the board
#change_turn - Changes which player's turn it is
#check_end - Checks to see if the game has ended
#check_win - Checks to see if a player has won
#check_tie - Checks to see if the game has tied
#check_row - Checks to see if a player has 3 in a row
#check_col - Checks to see if a player has 3 in a column
#check_diag - Checks to see if a player has 3 in a diagonal

#-----------Gloabls------------

#Basic Board that shows which numbers will select which spots on the board
sel_board =["7", "8", "9",
            "4", "5", "6",
            "1", "2", "3"]
#Initialization of the game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#Variable testing whether the game is still going
game_prog = True

#Variable that is set to the game winner
winner = None

#Variable that is set to the player who is currently playing
player = "X"

#Prints available selections
def disp_selections():
    print(sel_board[0] + " | " + sel_board[1] + " | " + sel_board[2])
    print(sel_board[3] + " | " + sel_board[4] + " | " + sel_board[5])
    print(sel_board[6] + " | " + sel_board[7] + " | " + sel_board[8])

#Prints the game board
def disp_board():
    print(board[6] + " | " + board[7] + " | " + board[8])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[0] + " | " + board[1] + " | " + board[2])

#Starts the game
def play():
    #initialize board
    print("These are your board locations.")
    print("Please use your keyboard numbers to make your turns.")
    disp_selections()
    print("")
    print("")
    
    disp_board()
    while game_prog:
        make_turn(player)
        check_end()
        change_turn()
    if winner == "X" or winner == "O":
        print(winner + " won the game!")
    elif winner == None:
        print("Tie Game!")

#Allows the player to make a selection on the board
def make_turn(player):
    print(player + "'s Turn.")
    spot = input("Make a selection 1-9:")
    valid = False
    while not valid:
        #Catching invalid positions on board
        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("Invalid place on board. Please make a selection 1-9:")
        spot = int(spot) - 1
        if board[spot] == "-":
            valid = True
        else:
            print("This place has already been taken.")
    
    board[spot] = player
    disp_board()

#Changes which player's turn it is
def change_turn():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

#Checks to see if the game has ended
def check_end():
    check_win()
    check_tie()
    
#Checks to see if a player has won
def check_win():
    #Set globals
    global winner
    
    # check rows
    r_win = check_row()
    
    # check columns
    c_win = check_col()
    
    # check diagonals
    d_win = check_diag()
    
    #Declaring the Winner
    if r_win:
        winner = r_win
    elif c_win:
        winner = c_win
    elif d_win:
        winner = d_win
    else:
        winner = None
    return


#Checks if all spots are full but there is no winner
def check_tie():
    global game_prog
    if "-" not in board:
        game_prog = False
    return

#Checks rows for three straight Xs or Os
def check_row():
    #Set gloabls
    global game_prog
    
    bot_row = board[0] == board[1] == board[2] != "-"
    mid_row = board[3] == board[4] == board[5] != "-"
    top_row = board[6] == board[7] == board[8] != "-"
    
    if bot_row or mid_row or top_row:
        game_prog = False
    if bot_row:
        return board[0]
    elif mid_row:
        return board[3]
    elif top_row:
        return board[6]
    

#Checks colums for three straight Xs or Os
def check_col():
    #Set gloabls
    global game_prog
    
    #Left Column
    l_col = board[0] == board[3] == board[6] != "-"
    #Middle Column
    m_col = board[1] == board[4] == board[7] != "-"
    #Right Column
    r_col = board[2] == board[5] == board[8] != "-"
    
    if l_col or m_col or r_col:
        game_prog = False
    if l_col:
        return board[0]
    elif m_col:
        return board[1]
    elif r_col:
        return board[2]
    
    
#Checks diagonals for three straight Xs or Os
def check_diag():
    #Set gloabls
    global game_prog
    
    #Diagonal with top left and bottom right spot
    tl_br = board[2] == board[4] == board[6] != "-"
    #Diagonal with top right and bottom left spot
    tr_bl = board[0] == board[4] == board[8] != "-"
    
    if tl_br or tr_bl:
        game_prog = False
    if tl_br:
        return board[6]
    elif tr_bl:
        return board[0]
    

play()