'''
Andrew Habib
21 March 2021
Python Lucky Letters
Lucky Letters Program
'''

# Importing Randomizing related options 
# To be used during conditional looping to continuously generate random integers (Rolling the dice)
# Would also be used to generate random samples of ASCII values that don't repeat to then be converted to alphabetical characters and generate letters in a random order and with no duplicates
import random

# Import options from the bisect library to enable binary searches which will be essential for the function of the game in finding letters
from bisect import bisect_left


# Formatting Variables

# Declare a variable to center the title within 60 spaces
str_centerTitle = "{:^60s}".format

# Declare a variable to left justify the players' names within 35 spaces
# Variable will be used solely to enter the players' names at the commencing of the program. Other input will use the variable directly below this one.
str_formatUserInputName = "{:<35s}".format

# Declare a variable to left justify all user input except for their names within 45 spaces
'''
--> This variable will be used to format any input related data excluding names including
whether they would like to role again or quit along with whether they would like to play again.
''' 
str_formatUserInput = "{:<45s}".format

# Declare a formatting variable that would left justify the player's names 15 spaces when they are inputted at the beginning of the program
str_formatPlayerName = "{:<15s}".format

# Declare a formatting variable to left justify the players' letters within 2 spaces
# This will only be used to format the two lines containing the players' letters
str_formatPlayerLetters = "{:<2s}".format

# Declare a formatting variable that would left justify the letters located on the score board within 5 spaces
# This variable would aid in establishing organized columns of letters and numbers on the board to create an esthetically pleasing board 
str_formatScoreBoardLetters = "{:<5s}".format




# Declare, store and initialize a variable to enable the user to play again or quit after the game is over
# Initializing this variable would begin the conditional loop by matching its criteria
str_playAgain = "Y"

# Declare and initialize a variable to enable the user to roll the dice for his/ her turn
# Initializing this variable would enable the game to start and enables the players to commence their turns as well
str_userRoll = "R"



# Output a centered title that would greet the player when they first enter the program
# Output 27 dashes center justified to compliment the length of the title
print(str_centerTitle("WELCOME TO LUCKY LETTERS!"))
print(str_centerTitle("-" * 27))
print()

# Declare a variable as a string to store the first player's name
# Prompt Player 1 to enter their name
# The name would be stored and later used to address the player throughout the game
# The name will be capitalized if it is alphabetical
str_player1 = str(input(str_formatUserInputName("Player 1, please enter your name:")).capitalize())

# Declare a variable as a string to store the second player's name
# Prompt Player 2 to enter their name
# The name would be stored and used later to address the player throughout the game
# The name will be capitalized if it is alphabetical
str_player2 = str(input(str_formatUserInputName("Player 2, please enter your name:")).capitalize())
print()

# Main Program

# While loop #1: Continuously loop while str_playAgain is equivalent to Y and the str_userRoll is equivalent to R
# Any other values will end the loop and the game altogether
'''
This specific while loop would mainly come into play when the game is over and
one of the 2 players has removed all of the letters from their list of letters.
-For now, it only commences the program and initializes all critical variables
-The program will keep looping until one decides not to roll (Quit the game)
or not play again after the game is complete.
- The program will restart if the user enters Y and all variables listed below
will re-initialize to start the commence a brand new game.
'''
# Case sensitivity will be ignored in this loop so the user could enter the lower case versions of the letters below to keep the loop going
while str_playAgain.upper() == "Y" and str_userRoll.upper() == "R":
    
    # Declare a variable that would store exactly 26 random yet non-repeating numbers from 65 to 91
    # This variable will generate integers that will correspond to the ASCII values of the capital letters of the alphabet
    # These will be the letters that will be evenly but randomly distributed among each of the players
    int_asciiValueList = random.sample(range(65, 91), 26)
    
    # Declare and initialize a list that will eventually contain a list of the first players' letters
    str_letterListP1 = []
    
    # Declare and initialize a list that will eventually contain a list of the second players' letters
    str_letterListP2 = []
    
    # Declare and initialize a list that will eventually contain a list of the letters that will be displayed on the score board
    # These letters will used when performing a binary search as the value being searched for
    str_scoreBoardLetters = []
    
    # Declare and initialize a list that will eventually contain a list of the first players' letters
    # This list is the same as the prior one but will never be updated when the dice is rolled in order to avoid index issues when performing binary searches
    str_letterListUnalteredP1 = []
    
    # Declare and initialize a list that will eventually contain a list of the second players' letters
    # This list is the same as the prior one but will never be updated when the dice is rolled in order to avoid index issues when performing binary searches
    str_letterListUnalteredP2 = []
    
    # Declare and initialize a variable that would serve as a counter that will be responsible for ending the game once the first player's list of letters is empty
    # Every time a letter is removed from the first player's list, 1 will be added to the counter until the counter reaches 13 in which case the 1st player would win
    int_counterP1 = 0
    
    # Declare and initialize a variable that would serve as a counter that will be responsible for ending the game once the second player's list of letters is empty
    # Every time a letter is removed from the second player's list, 1 will be added to the counter until the counter reaches 13 in which case the 2nd player would win
    int_counterP2 = 0
    
    # Declare a variable that would generate a random integer between 1 and 2 inclusively 
    # This variable will decide which of the players will go first
    int_firstTurnDecider = random.randint(1, 2)
    
    # Check if the random integer rolled is a 1 (Is player 1 going to go first?)
    if int_firstTurnDecider == 1:
        
        # Declare a boolean that stores the first player's turn as true
        # This means that player 1 will go first
        bool_turnPlayer1 = True
        
        # Declare a boolean that stores the second player's turn as false
        # This means that player 2 will not go first
        bool_turnPlayer2 = False 
    
    # Check if the random integer rolled is a 2 (Is player 2 going to go first?)   
    elif int_firstTurnDecider == 2:
        
        # Declare a boolean that stores the first player's turn as false
        # This means that player 1 will not go first
        bool_turnPlayer1 = False
        
        # Declare a boolean that stores the second player's turn as true
        # This means that player 2 will go first
        bool_turnPlayer2 = True
    
    
    # Part 1 - Generating each player's list of letters
    '''
    --> For loop (Counted Loop #1) - Purpose is to cycle through each random ASCII Value sample in the list, convert it to 
    its correspondent letter, and give each player a letter one at a time by taking turns (All even indexes starting at
    the index 0 will go to the first player and then all odd index starting at 1 will go to the second player).
    This will replicate the idea of generating a random letter then passing it to the first player then doing the same
    for the second and so on until both players have been assigned with their 13 letters in which case each players' letters
    will be sorted in ascending order.
    '''
    # Enumerate will be used as an automatic counter mainly for the if statement to give all even indexes of letters to the first player and the rest to the second.
    for int_listIndex, number in enumerate(int_asciiValueList):
        
        # Declare a variable that would convert and store each integer from the list of capital letter ASCII Values as its designated upper case letter
        str_playerLetter = chr(number)
        
        # This code of if statements will ensure each player gets a letter one a time to randomize which players get which letters
        
        # Check if the current index of the list is an even number
        if int_listIndex % 2 == 0:
            
            # Add the currently formed letter to the end of the first player's list of letters
            str_letterListP1.append(str_playerLetter)
        
        # Otherwise, the current index of the list is an odd number   
        else:
            
            # Add the currently formed letter to the end of the second player's list of letters
            str_letterListP2.append(str_playerLetter)
        
        # After cycling through each randomly generated non-repeating letter, sort each of the players' lists in ascending order 
        str_letterListP1.sort(key=str.upper)
        str_letterListP2.sort(key=str.upper)
        
    # Update the 2 lists with the lists of the players' letters
    # These lists are the same as the prior ones but will never be updated when the dice is rolled in order to avoid index issues when performing binary searches later in the program
    str_letterListUnalteredP1 = str_letterListUnalteredP1 + str_letterListP1
    str_letterListUnalteredP2 = str_letterListUnalteredP2 + str_letterListP2
    
    
    
    # Update the ASCII Value List to store exactly 36 random yet non-repeating numbers from 65 to 101
    # This variable will generate integers that will correspond to the ASCII values of the capital letters of the alphabet except in the case of numbers 91 - 100
    # These will be the letters that will be generated on random places on the board
    # Each of the integers will be converted to their corresponding letter except 91 - 100 which will just resemble a "-" on the board or a blank
    int_asciiValueList = random.sample(range(65, 101), 36)
    
    # Part 2 - Generate the initial score board
    '''
    --> for loop (Counted loop #2) - Purpose is to cycle through each random ASCII Value sample in the list, convert it to its correspondent 
    letter (unless the number is between 91 and 101 (non-inclusive) in which case a "-" symbol will be used in its place) and add it (append) 
    to the end of the list of letters for the game board.
    '''
    for number in int_asciiValueList:
        
        # Check if each number is greater than or equal to 65 and less than or equal to 90 (ASCII Values for capital letters)
        if number >= 65 and number <= 90:
            
            # Declare a variable that would convert and store each integer from the list of capital letter ASCII Values as its designated upper case letter
            # This will be used to generate the letters for the game board itself
            str_boardLetter = chr(number)
            
            # Add the currently formed letter to the end of the list of letters for the game board
            str_scoreBoardLetters.append(str_boardLetter)
            
        # Otherwise, the number is an integer between 91 and 100
        else:
            
            # The rest of the 36 characters must be blanks (10 blanks) if the integer is not between 65 and 90.
            str_boardLetter = "-"
            
            # Add the blank to the end of the list of letters for the game board
            str_scoreBoardLetters.append(str_boardLetter)
    
    
    # While loop #2 (While loop within while loop #1): Continuously loop whilestr_userRoll is equivalent to R and both players' counters are below 13 (Decides the winner)
    # Any other values will end the loop and the game altogether
    '''
    This specific while loop would mainly come into play when a player has completed 
    their turn and the new player's turn starts
    -The program will keep looping until one decides not to roll (Quit the game).
    '''
    # Case sensitivity will be ignored in this loop so the user could enter the lower case versions of the letters below to keep the loop going
    while str_userRoll.upper() == "R" and int_counterP1 < 13 and int_counterP2 < 13:
        
        '''
        Ouputting Player letters
        Output each player's letters in an organized fashion after they each enter their names
        Every time the turns switch, values outputted in player's letters will be updated regularly and re-outputted after each turn
        '''
        
        # Output 42 lines as a border on the top to compliment the spacing and the amount of letters each player has
        print("-" * 42)
        
        # Output the first player's name followed by a colon 
        # end =.. will be used to ensure that all of the player's letters are organized horizontally side-by-side
        print(str_formatPlayerName(str_player1 + ":"), end="")
        
        
        # Output each of the first players' letters contained in their list of letters
        '''
        --> for loop (Counted loop #3) - Purpose is to cycle through each letter in the first player's list of letters
        and output them side-by-side horizontally using end function and evenly yet slightly spaced apart until
        all 13 of the letters in the list have been outputted.
        '''
        for letter in str_letterListP1:
            print(str_formatPlayerLetters(letter), end="")
        print()   
        
        # Output the second player's name followed by a colon 
        # end =.. will be used to ensure that all of the player's letters are organized horizontally side-by-side
        print(str_formatPlayerName(str_player2 + ":"), end="")
        
        # Output each of the second players' letters contained in their list of letters
        '''
        --> for loop (Counted loop #4) - Purpose is to cycle through each letter in the second player's list of letters
        and output them side-by-side horizontally using end function and evenly yet slightly spaced apart until
        all 13 of the letters in the list have been outputted.
        '''
        for letter in str_letterListP2:
            print(str_formatPlayerLetters(letter), end="")
        print()   
        
        # Output 42 lines as a border on the bottom to compliment the spacing and the amount of letters each player has
        print("-" * 42) 
        print()
        
        '''
        --> Ouputting board letters
        Output each board letters in an organized fashion after the each players' letters are outputted
        IMPORTANT: The board is a 6 by 6 character board (Containing 36 characters --> 6x6) filled with randomly placed 26 upper case characters and 10 randomly placed blanks ("-")
        Every time the turns switch, the board will be updated regularly based on the turn or what values were landed on and re-outputted after each turn
        '''
        
        # Output nothing at the top left of the board so numbers may be placed to the right and below
        # End function will ensure that the 6 numbers resembling the column numbers will be outputted horizontally with ideal spacing in between (According to formatting option set)
        print(str_formatScoreBoardLetters(""), end="")
        
        
        # Output 6 numbers from 1 - 6 to resemble numbered columns placed horizontally side-by-side
        '''
        --> for loop (Counted loop #5) - Purpose is to formulate numbers that would label the columns for the game board.
        Counted loop will have a counter that will update by increasing by 1 with every iteration as the range is from
        1 to 7 non inclusive.
        '''
        for counter in range(1, 7):
            
            # Output column numbers from 1 - 6 evenly spaced out and horizontally
            print(str_formatScoreBoardLetters(str(counter)), end="")

        print()
        
        # Declare a variable as an integer that would resemble the number of rows which will be outputted on the left side of the board
        int_rowNumber = 1
        
        # Print the first row and use end function to enable the first row of letters to be outputted to its right
        print(str_formatScoreBoardLetters(str(int_rowNumber)), end="")
        
        # Output 6 numbers from 1 - 6 to resemble numbered rows placed vertically side-by-side
        # Also output every 6 characters on each row for each of the 6 rows
        '''
        --> for loop (Counted loop #5) - Purpose is to formulate numbers that would label the rows for the game board but
        also to output the letters of the game board (6 rows of 6 letters in each column).
        '''
        # Index of the list will help to determine whether or not a new row will need to be added (Based on whether the 6 columns have been filled)
        for int_listIndex, letter in enumerate(str_scoreBoardLetters):
            
            # Check if the current index of the list plus one modulus 6 will not equal 0 (1 must be added as indexes start at 0 which would set a runtime error in this case)
            # This would suggest that the index has not yet reached a multiple of six so a new row will not need to be added yet
            if (int_listIndex + 1) % 6 != 0:
                
                # Output the letter on the same row evenly spaced out and perfectly aligning with the column numbers
                print(str_formatScoreBoardLetters(letter), end="")
            
            # Otherwise, the current index of the list plus one modulus 6 is equal to 0   
            else:  
                
                # Output the 6th character in the row (In the 6th column) but without the end function so that the next row may be formed  
                print(str_formatScoreBoardLetters(letter))
                
                # Update the row number variable by adding 1 to it so that the next row number may be outputted
                int_rowNumber = int_rowNumber + 1    
                
                # Check if the row number is less than or equal to 6 to ensure that not more than 6 rows are outputted on the game board
                if int_rowNumber <= 6:
                    
                    # Ouput the row number along with the end funtion to ensure that the next row of letters are outputted side-by-side
                    print(str_formatScoreBoardLetters(str(int_rowNumber)), end="")    
            
        print()
        
        
        
        
        # Check if it is player 1's turn
        # This will vary based on whether the turn deciding dice rolls a 1 or not
        if bool_turnPlayer1 == True:
            
            # Declare and initialize a variable that will store the index of the list of letters for the board
            int_boardListIndex = 0
            
            # Declare a variable as a string to store the user's choice of whether to role again or quit (lower case r should also work - case insensitive)
            # Prompt the user to choose whether they would like to roll again or quit the game (Enter a letter other than R)
            str_userRoll = str(input(str_formatUserInput(str_player1 + "," + " press R to roll (Q to quit):")))
            
            # Check if the user entered R to roll again (R or r - case insensitive)
            if str_userRoll.upper() == "R":
                
                # Generate a random integer ranging from 1-6 to represent the first player rolling the first dice
                int_Dice1 = random.randint(1, 6)
                
                # Generate a random integer ranging from 1-6 to represent the first player rolling the second dice
                int_Dice2 = random.randint(1, 6)
                
                # Update the variable for the index of the list of letters with the board with an integer resulting from the following formula
                # This formula ensures that the first dice gives the row number and the second dice gives the column number
                # The formula will give the specific index on the board list that corresponds with the dice values 
                int_boardListIndex = ((int_Dice1 * 6) - 6) + (int_Dice2 - 1)
                
                # Output for the first player what the values that the dice they have rolled are
                print("You rolled [" + str(int_Dice1) + "] [" + str(int_Dice2) + "]")
                
                
                # Matching the players' characters with the values on the board
                # Check if player 1 landed on a blank (not a letter)
                if str_scoreBoardLetters[int_boardListIndex] == "-":
                    
                    # Inform the user that they landed on a blank and there is no match with any of the letters in any of the players' lists
                    print("Sorry...you landed on '" + str_scoreBoardLetters[int_boardListIndex] + "'. No match.")
                
                # Otherwise, player 1 has landed on an actual letter on the board
                else:
                    
                    # Perform a binary search (using bisect left) to search for the score board letter at the specified index decided by the dice within the first player's unaltered list
                    int_indexBisection = bisect_left(str_letterListUnalteredP1, str_scoreBoardLetters[int_boardListIndex])
                    '''
                    Check if the index found does not equal the length of the list so that the binary search does not return the index where a value would be found and
                    check if the first player's unaltered list at the index of the binary search is equivalent to the score board letter at the index rolled by the dice.
                    '''
                    if int_indexBisection != len(str_letterListUnalteredP1) and str_letterListUnalteredP1[int_indexBisection] == str_scoreBoardLetters[int_boardListIndex]:
                        
                        # Inform the player that they have removed a letter from their own list
                        print("Congratulations...'" + str_scoreBoardLetters[int_boardListIndex] + "' was removed!")
                        
                        # Update the letter landed on on player 1's actual list with a blank to ensure that it is removed and not used again
                        str_letterListP1[int_indexBisection] = " "
                        
                        # Update the first player's counter as they are 1 point closer to 13 (win)
                        int_counterP1 = int_counterP1 + 1
                    
                    # Otherwise, the letter landed on by the first player on the board is not their letter (The other player's letter)   
                    else:
                        
                        # Perform a binary search (using bisect left) to search for the score board letter at the specified index decided by the dice within the second player's unaltered list
                        # This will always return something
                        int_indexBisection = bisect_left(str_letterListUnalteredP2, str_scoreBoardLetters[int_boardListIndex])
                        
                        # Inform player 1 that they have landed on one of player 2's letters which will be removed from their list
                        print("Ouch...you landed on '" + str_scoreBoardLetters[int_boardListIndex] + "', which will be removed from " + str_player2 + "'s list.")
                        
                        # Update the letter landed on on player 2's actual list with a blank to ensure that it is removed and not used again
                        str_letterListP2[int_indexBisection] = " "
                        
                        # Update the second player's counter as they are 1 point closer to 13 (win)
                        int_counterP2 = int_counterP2 + 1
    
                # Replace the letter landed on on the score board letters with a blank so the letter is not used again
                str_scoreBoardLetters[int_boardListIndex] = "-"
                
                # Switch the turns of the 2 players by updating their boolean values
                bool_turnPlayer1 = False
                bool_turnPlayer2 = True
            
            # Otherwise, the first player has chosen not to roll again but potentially quit    
            else:
                print()
                
                # Declare a variable that verifies if the user actually wants to quit or not
                # Prompt the user asking them if they are sure that they want to quit
                str_verifyQuit = str(input(str_formatUserInput("Are you sure you want to quit (Y or N)?")))
                
                # Check if the verify variable is equivalent to Y or y (Yes)
                if str_verifyQuit.upper() == "Y":
                    
                    # Set the user roll variable to Q to quit
                    str_userRoll = "Q"
                   
                # Otherwise, the verify variable is not equivalent to Y or y so the user will keep playing
                else:
                    
                    # Allow the current player to be prompted again and continue their turn
                    str_userRoll = "R"

            print()
            
            
        # Otherwise, check if it is player 2's turn
        # This will vary based on whether the turn deciding dice rolls a 1 or not
        elif bool_turnPlayer2 == True:
            
            # Re-initialize the variable that will store the index of the list of letters for the board
            int_boardListIndex = 0
            
            # Declare a variable as a string to store the user's choice of whether to role again or quit (lower case r should also work - case insensitive)
            # Prompt the user to choose whether they would like to roll again or quit the game (Enter a letter other than R)
            str_userRoll = str(input(str_formatUserInput(str_player2 + "," + " press R to roll (Q to quit):")))
            
            
            # Check if the user entered R to roll again (R or r - case insensitive)
            if str_userRoll.upper() == "R":
                
                # Generate a random integer ranging from 1-6 to represent the second player rolling the first dice
                int_Dice1 = random.randint(1, 6)
                
                # Generate a random integer ranging from 1-6 to represent the second player rolling the second dice
                int_Dice2 = random.randint(1, 6)
                
                # Update the variable for the index of the list of letters with the board with an integer resulting from the following formula
                # This formula ensures that the first dice gives the row number and the second dice gives the column number
                # The formula will give the specific index on the board list that corresponds with the dice values 
                int_boardListIndex = ((int_Dice1 * 6) - 6) + (int_Dice2 - 1)
                
                # Output for the second player what the values that the dice they have rolled are
                print("You rolled [" + str(int_Dice1) + "] [" + str(int_Dice2) + "]")
                
                # Matching the players' characters with the values on the board
                # Check if player 2 landed on a blank (not a letter)
                if str_scoreBoardLetters[int_boardListIndex] == "-":
                    
                    # Inform the user that they landed on a blank and there is no match with any of the letters in any of the players' lists
                    print("Sorry...you landed on '" + str_scoreBoardLetters[int_boardListIndex] + "'. No match.")
                
                # Otherwise, player 2 has landed on an actual letter on the board
                else:
                    
                    # Perform a binary search (using bisect left) to search for the score board letter at the specified index decided by the dice within the second player's unaltered list
                    str_indexBisection = bisect_left(str_letterListUnalteredP2, str_scoreBoardLetters[int_boardListIndex])
                    
                    '''
                    Check if the index found does not equal the length of the list so that the binary search does not return the index where a value would be found and
                    check if the second player's unaltered list at the index of the binary search is equivalent to the score board letter at the index rolled by the dice.
                    '''
                    if str_indexBisection != len(str_letterListUnalteredP2) and str_letterListUnalteredP2[str_indexBisection] == str_scoreBoardLetters[int_boardListIndex]:
                        
                        # Inform the player that they have removed a letter from their own list
                        print("Congratulations...'" + str_scoreBoardLetters[int_boardListIndex] + "' was removed!")
                        
                        # Update the letter landed on on player 2's actual list with a blank to ensure that it is removed and not used again
                        str_letterListP2[str_indexBisection] = " "
                        
                        # Update the second player's counter as they are 1 point closer to 13 (win)
                        int_counterP2 = int_counterP2 + 1
                    
                    # Otherwise, the letter landed on by the second player on the board is not their letter (The other player's letter)   
                    else:
                        
                        # Perform a binary search (using bisect left) to search for the score board letter at the specified index decided by the dice within the first player's unaltered list
                        # This will always return something
                        str_indexBisection = bisect_left(str_letterListUnalteredP1, str_scoreBoardLetters[int_boardListIndex])
                        
                        # Inform player 2 that they have landed on one of player 1's letters which will be removed from their list
                        print("Ouch...you landed on '" + str_scoreBoardLetters[int_boardListIndex] + "', which will be removed from " + str_player1 + "'s list.")
                        
                        # Update the letter landed on on player 1's actual list with a blank to ensure that it is removed and not used again
                        str_letterListP1[str_indexBisection] = " "
                        
                        # Update the first player's counter as they are 1 point closer to 13 (win)
                        int_counterP1 = int_counterP1 + 1
                
                # Replace the letter landed on on the score board letters with a blank so the letter is not used again
                str_scoreBoardLetters[int_boardListIndex] = "-"
                
                # Switch the turns of the 2 players by updating their boolean values
                bool_turnPlayer1 = True
                bool_turnPlayer2 = False
                
            # Otherwise, the second player has chosen not to roll again but potentially quit    
            else:
                print()
                
                # Declare a variable that verifies if the user actually wants to quit or not
                # Prompt the user asking them if they are sure that they want to quit
                str_verifyQuit = str(input(str_formatUserInput("Are you sure you want to quit (Y or N)?")))
                
                # Check if the verify variable is equivalent to Y or y (Yes)
                if str_verifyQuit.upper() == "Y":
                    
                    # Set the user roll variable to Q to quit
                    str_userRoll = "Q"
                   
                # Otherwise, the verify variable is not equivalent to Y or y so the user will keep playing
                else:
                    
                    # Allow the current player to be prompted again and continue their turn
                    str_userRoll = "R"
               
        print()
    
    # Ending of one game
    # Check if the first player has reached 13 on their counter (All their letters have been hit)
    if int_counterP1 >= 13:
        
        # Output a message that informs player 1 that they have won the game.
        print("GAME OVER!", str_player1 + ", wins the game!") 
        
        # Declare a variable as a string to store the user's choice of whether to play again or terminate the program
        # Prompt the user to choose whether they would like to play again or not
        str_playAgain =  str(input(str_formatUserInput("Would you like to play again (Y or N)?"))) 
        print()
    
    # Otherwise, check if the second player has reached 13 on their counter (All their letters have been hit)     
    elif int_counterP2 >= 13:
        
        # Output a message that informs player 2 that they have won the game.    
        print("GAME OVER!", str_player2 + ", wins the game!")
        
        # Declare a variable as a string to store the user's choice of whether to play again or terminate the program
        # Prompt the user to choose whether they would like to play again or not
        str_playAgain =  str(input(str_formatUserInput("Would you like to play again (Y or N)?")))      
        print()

# If the user chooses not to roll or not to play again but quit, end the loop and thank the user for playing before terminating the program
print("Thank you for playing Lucky Letters. Goodbye!")








