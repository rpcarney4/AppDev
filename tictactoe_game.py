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


#-------------Game Setup--------------


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
    #Display instructions
    print("These are your board locations.")
    print("Please use your keyboard numbers to take your turns.")
    disp_selections()
    print("")
    print("")
    
    #initialize board
    disp_board()
    
    #Loop to check game logic
    while game_prog:
        make_turn(player)
        check_end()
        change_turn()
    if winner == "X" or winner == "O":
        print(winner + " won the game!")
    elif winner == None:
        print("Tie Game!")



#-------------Game Logic---------------
        
        
#Allows the player to make a selection on the board
#@param player - contains either player "X" or "O"
def make_turn(player):
    print(player + "'s Turn.")
    
    #Receiving user input
    spot = input("Make a selection 1-9:")
    
    #Catching invalid moves on board
    valid = False
    while not valid:
        
        #Checking that input is between 1 and 9
        while spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            spot = input("Invalid place on board. Please make a selection 1-9:")
        spot = int(spot) - 1
        
        #checking that input has not already been taken.
        if board[spot] == "-":
            valid = True
        else:
            print("This place has already been taken.")
    
    #Placing an X or O on the chosen location
    board[spot] = player
    disp_board()

#Changes which player's turn it is
def change_turn():
    
    #Retrieving global variable
    global player
    
    #Changing which player has the current turn
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"

#Checks to see if the game has ended
def check_end():
    
    #Calling functions check_win and check_tie
    check_win()
    check_tie()
    
#Checks to see if a player has won
def check_win():
    
    #Retrieving global variable
    global winner
    
    # Calling check rows
    r_win = check_row()
    
    # Calling Check columns
    c_win = check_col()
    
    # Calling check diagonals
    d_win = check_diag()
    
    #Setting the Winner
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



#------------Win Parameters-------------
    
    
#Checks rows for three straight Xs or Os
def check_row():
    #Set gloabls
    global game_prog
    
    #Retrieving values in bottom row
    bot_row = board[0] == board[1] == board[2] != "-"
    #Retrieving values in middle row
    mid_row = board[3] == board[4] == board[5] != "-"
    #Retrieving values in top row
    top_row = board[6] == board[7] == board[8] != "-"
    
    #Checking if a win parameter is met
    if bot_row or mid_row or top_row:
        game_prog = False
        
    #Returning "X" or "O" from board to determine winner
    if bot_row:
        return board[0]
    elif mid_row:
        return board[3]
    elif top_row:
        return board[6]
    

#Checks columns for three straight Xs or Os
def check_col():
    
    #Retrieving global variable
    global game_prog
    
    #Retrieving values in left column
    l_col = board[0] == board[3] == board[6] != "-"
    #Retrieving values in middle column
    m_col = board[1] == board[4] == board[7] != "-"
    #Retrieving values in right column
    r_col = board[2] == board[5] == board[8] != "-"
    
    #Checking if a win parameter is met
    if l_col or m_col or r_col:
        game_prog = False
        
    #Returning "X" or "O" from board to determine winner
    if l_col:
        return board[0]
    elif m_col:
        return board[1]
    elif r_col:
        return board[2]
    
    
#Checks diagonals for three straight Xs or Os
def check_diag():
    
    #Retrieving global variable
    global game_prog
    
    #Retrieving values in diagonal with top left and bottom right spot
    tl_br = board[2] == board[4] == board[6] != "-"
    #Retrieving values in diagonal with top right and bottom left spot
    tr_bl = board[0] == board[4] == board[8] != "-"
    
    #Checking if a win parameter is met
    if tl_br or tr_bl:
        game_prog = False
        
    #Returning "X" or "O" from board to determine winner
    if tl_br:
        return board[6]
    elif tr_bl:
        return board[0]
    
#Calling play function to start the game
play()
