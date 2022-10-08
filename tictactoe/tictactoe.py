# Import random module so that the program can randomly choose who goes first 
import random
"""
A function which takes a list of 9 values and outputs those values in a 3x3 grid with | seperating the values
"""
def art(list):
    # Set a temporary integer varaible to 0
    t = 0
    # Run a loop 3 times, this is used to output the 3 rows
    for i in range(3):
        # Run a loop 3 times, this is used to output the 3 columns
        for j in range(3):
            # Check if the loop is not in its last stage
            if j != 2:
                # If loop is not in its last stage output the lists varaible with | at the end
                print(list[t+j] ,end="|")
            else:
                # If loop is in its last stage then output the list with an empty ending
                print(list[t+j] ,end="")
        # Add three to t so that in the next iteration of the loop the code knows to skip the three already used variables
        t = t + 3
        # Check if the loop is not in its last stage 
        if i != 2:
            # If loop is not in its last stage output a new line along with a straight horizontal line
            print("\n------" )
        else :
            # If loop is in its last stage then only output a new line
            print("\n")
"""
A function which takes two list parameters and check which elements of the second list index an empty space in the first list.
Output which element in the second list constitutes an empty space along with True
"""
def isEmpty(board,list1:list):
    # A variable which stores what is considered an empty space
    emptySpace = [1,2,3,4,5,6,7,8,9]
    # Run a loop as long the second list
    for i in range(len(list1)):
        # Store the value of the second list at index i in a temporary varaible
        tempInt  = list1[i]
        # Check if board at index tempInt is a part of empty space
        if board[tempInt] in emptySpace:
            # Create a variable output which will store the tempInt along with a boolean True
            output = [tempInt,True]
            # Return output
            return output
"""
A function which takes a list and outputs a boolean as to whether or not that list has any empty spaces or not
Outputs True if there are no empty spaces, False if there are empty spaces
"""
def checkTie(list1):
    # A counter variable
    count = 0
    # A loop which runs as long as the list
    for i in range(len(list1)):
        # Checks if list at index is empty
        if list1[i] in [1,2,3,4,5,6,7,8,9]:
            # Add 1 to count
            count = count + 1
    # Return whether count is equal to 0 or not
    return count == 0
"""
A function which takes in a 9 element list and a character and checks if the given character results in a win in the given list
"""
def checkWin(list,character):
    # Returns True if any of the possible 3 in a rows is present in the list
    return ((list[0] == character and list[1] == character and list[2] == character) or (list[3] == character and list[4] == character and list[5] == character) or (list[6] == character and list[7] == character and list[8] == character)or

    (list[0] == character and list[3] == character and list[6] == character) or (list[1] == character and list[4] == character and list[7] == character) or (list[2] == character and list[5] == character and list[8] == character) or

    (list[0] == character and list[4] == character and list[8] == character) or (list[2] == character and list[4] == character and list[6] == character))


"""
A function which takes in the current state of the board as a list, the users character and the computers character and calculates 
the best possible move for the computer
"""
def compMove(board,charC,charU):
    """
    This for loop looks one step ahead to see if the  computer can win
    """    
    # A loop which runs as long as the length of the given board
    for i in range (len(board)):
        # Create a temporary copy of the board
        tempC = list(board)
        # Check if the board at index i is an empty space
        if isEmpty(board,[i]):
            # Add to the temporary copy the computers character
            tempC[i] = charC
            # Check if the computer won
            if  checkWin(tempC,charC):
                # If the computer won return the index at which the computer would win
                return i
    """
    This for loop looks one step ahead to see if user can win
    """
    # A loop which runs as long as the length of the given board
    for i in range (len(board)):
        # Create a temporary copy of the board
        tempU = list(board)
        # Check if the board at index i is an empty space
        if isEmpty(board,[i]):
            # Add to the temporary copy the users character
            tempU[i] = charU
            # Check if the user won
            if  checkWin(tempU,charU):
                # If the user won return the index at which the user would win
                return i
            
    
                                        
    
    else:
        """
        This for loop looks two steps ahead for the computer to see if any winning forks can be created
        """
        # A loop which runs as long as the length of the given board
        for i in range (len(board)):
            # Create a temporary copy of the board
            tempC = list(board)
            # Check if the board at index i is an empty space
            if isEmpty(board,[i]):
                # Add to the temporary copy the computers character
                tempC[i] = charC   
                # Check if the computer didnt win
                if not checkWin(tempC,charC):
                    # A loop which runs as long as the length of the given board
                    for j in range (len(board)):
                        # Check if the board at index j is an empty space
                        if isEmpty(board,[j]):
                            # Add to the temporary copy the computers character
                            tempC[j] = charC 
                            # Check if the computer won
                            if checkWin(tempC,charC):
                                # If the computer won return the index at which the computer would win
                                return j 
        """
        This for loop looks two steps ahead for the user to see if any winning forks can be stopped
        """
        # A loop which runs as long as the length of the given board
        for i in range (len(board)):
            # Create a temporary copy of the board
            tempU = list(board)
            # Check if the board at index i is an empty space
            if isEmpty(board,[i]):
                # Add to the temporary copy the users character
                tempU[i] = charU  
                # Check if the computer didnt win
                if not checkWin(tempU,charU):
                    for j in range (len(board)):
                        # Check if the board at index j is an empty space
                        if isEmpty(board,[j]):
                            # Add to the temporary copy the users character 
                            tempU[j] = charU 
                            # Check if the user won
                            if checkWin(tempU,charU):
                                # If the user won return the index at which the user would win
                                return j
        
        # If no winning forks are availble then have the computer choose an open corner spot
        if isEmpty(board,[0,2,6,8])[1]:
            return isEmpty(board,[0,2,6,8])[0]
        # If no corner spots are availble then have the computer choose an open middle spot
        elif isEmpty(board,[4])[1]:
            return isEmpty(board,[4])[0]
        # If no middle spots are availble then have the computer choose an open side spot
        elif isEmpty(board,[1,3,5,7])[1]:
            return isEmpty(board,[1,3,5,7])[0]

"""
A function which randomly decides whether the computer or player should go first
Returns "c" if computer goes first
Returns "u" if player goes first
"""
def whoFirst():
    # A temporary variable which stores a random integer either 1 or 0
    temp = random.randint(0,1)
    # Check if the random integer is 1
    if temp == 1:
        # The computer goes first
        return "c"
    # Check if the random integer is not 1
    else :
        # The user goes first 
        return "u"
"""
A function which takes the board as a paramter and checks if the users input is valid
This function will run over and over agian untill the user inputs a valid input
"""
def playerTurn(board):
    # A temporary counter variable
    count = 0
    # A infinite loop
    while True:
        # Check if this iteration of the loop is not the first one
        if count > 0 :
            # Output that the users input is an invalid spot
            print("This spot is taken. Try again")
        # Ask the user for their desired move
        move = int(input("What is your move(1-9)"))
        # Check if the users move is in an empty space
        if board[move-1] in [1,2,3,4,5,6,7,8,9]:
            # return the users move, this ends the infinite loop
            return move         
# A variable which will store the users choice over whether they continue playing.
# Starts as yes so that the game starts the first time the code is run
game = "yes"
# A loop which runs as long as the user wishes to cintinue to play
while game == "yes":
    # Output a greeting to te user
    print("Welcome to Tic Tac Toe")
    # Ask the user which character they wish to be
    character_U = input("Do you wish to be X or O:")
    # Check if user chose X or x
    if character_U == "X" or character_U == "x":
        # Then the computers character shall be O
        character_C = "O"
    else:
        # Check if user chose O or o
        if character_U == "O" or character_U == "o":
            # Then the computers character shall be X 
            character_C = "X"
    # The list which holds all the moves that will happen
    # Starts as 1,2,3,4,5,6,7,8,9 so that when it is printed out the user will know where their input is going
    moves = [1,2,3,4,5,6,7,8,9]
    # Output the board with the current moves
    art(moves)
    # If the computer decided the computer will go first
    if whoFirst() == "c":
        # Output that the cmputer will go first
        print("Computer will go first")
        # Get the first move for the computer
        firstMove = compMove(moves,character_C,character_U)
        # Add the first move to the moves
        moves[firstMove ] = character_C
        # Output the board with the current moves
        art(moves)
    # An infnite loop 
    while True :
        # The users move is equal to the valid inout from the user
        move_U = playerTurn(moves)
        # Add the users move to moves
        moves[move_U - 1] = character_U
        # Output the board with the current moves
        art(moves)
        # Check if the user won
        if checkWin(moves,character_U):
            # If the user won. Output the user won
            print("Yay!, you have won")
            # End the loop
            break
        # Check if the user tied the game
        elif checkTie(moves):
            # If the user tied. Output the game tied
            print("It's a tie")
            # End the loop
            break
        # Output its now the computers turn
        print("It is now the computers turn")
        # Get the computers move frm the A.I.
        move_C = compMove(moves,character_C,character_U)
        # Add the computers move to moves
        moves[move_C ] = character_C
        # Output the board with the current moves
        art(moves)
        # Check if the computer won
        if checkWin(moves,character_C):
            # If the computer won. Output the computer won
            print("Oh No!, the computer has won")    
            # End the loop
            break
        # Check if the game tied
        elif checkTie(moves):
            # If the game tied. Output the game tied
            print("It's a tie")
            # End the loop
            break
    # Ask if the user wishes to play again
    game = input("Do you wish to play again? (yes or no)").lower()

