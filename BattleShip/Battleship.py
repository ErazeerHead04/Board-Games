import random
import os

os.system('clear')

# Global constant variables:
NUM_ROW = 1
NUM_COL = 15

# Initialization of the board:
board = []
for col in range(NUM_COL):
    board.append(" ")

# Displaying initial board:
os.system('clear')

print('\n')
print('                     ⚓BATTLESHIP⚓                         \n')
print(" ", end="")
for col in range(NUM_COL):
    print(f' {chr(65 + col)} ', end=" ")
print('\n#' + '---#' * NUM_COL)
print('|', end="")
for col in board:
    print(f' {col} |', end="")
print('\n#' + '---#' * NUM_COL)

# Position of the ship
random_integer = random.randint(NUM_ROW, NUM_COL)

ship_start = random_integer
while ship_start == NUM_COL: #For make sure that the position of the ship is within the range of the columns
    random_integer = random.randint(NUM_ROW, NUM_COL)

ship_end = (ship_start + 1)

#print("Ship position:", ship_start, ship_end) [For testing the code if needed]

# Number of attempts allowed
attempts_left = 3

# Main game loop
while attempts_left <4:    
    attempt_list=['Third','Second','First']
    
    # Getting user input for the guess and input validation:
    valid_input = False

    while not valid_input:

        guess_start = input(f"Attempt {4 - attempts_left}: Enter the coordinate for your {attempt_list[attempts_left-1]} attempt ({chr(NUM_ROW + 65 - 1)}-{chr(NUM_COL + 65 - 1)}): ")
        
        # Input validation:
        if len(guess_start) == 1 and guess_start.isupper() and chr(64+NUM_ROW) <= guess_start <= chr(64 + NUM_COL):
            guess_start_index = ord(guess_start) - ord('A') + 1

            # If the user gives the same input:
            if board[guess_start_index - 1] != ' ':
                print('You have entered this value before. Please enter a new position.')
            else:
                valid_input = True
        else:
            print(f"Please enter a one-character valid input ({chr(NUM_ROW + 65 - 1)}-{chr(NUM_COL + 65 - 1)})")

    os.system('clear')    

    # Check if the guess is correct
    if guess_start_index == ship_start or guess_start_index == ship_end:        
        board[guess_start_index - 1] = 'O'
        
        # Display the updated board

        print('\n')
        print('                     ⚓BATTLESHIP⚓                            \n')

        print(" ", end="")
        for col in range(NUM_COL):
            print(f' {chr(65 + col)} ', end=" ")
        print('\n#' + '---#' * NUM_COL)

        print('|', end="")
        for col in board:
            print(f' {col} |', end="")
        print('\n#' + '---#' * NUM_COL)
        print("Hit!💥")

        # Check if both positions are guessed correctly
        if board[ship_start - 1] == 'O' and board[ship_end - 1] == 'O':
            print("YOU WON! The ship is destroyed!")
            break
    else:
        
        board[guess_start_index - 1] = 'X'
        attempts_left -= 1        

        # Display the updated board with radar information
        print('\n')
        print('                     ⚓BATTLESHIP⚓                         \n')
        print(" ", end="")
        for col in range(NUM_COL):
            print(f' {chr(65 + col)} ', end=" ")
        print('\n#' + '---#' * NUM_COL)

        print('|', end="")
        for col in board:
            print(f' {col} |', end="")
        print('\n#' + '---#' * NUM_COL)
        print("Miss!")
        print(f"Attempts left: {attempts_left}")

        #Displaying radar information
        
        if guess_start_index> ship_start and ship_end:
            print(f"Radar🚨: The ship is positioned to the LEFT of your last input.")
        elif guess_start_index< ship_start and ship_end:
            print(f"Radar🚨: The ship is positioned to the RIGHT of your last input.")

    if attempts_left == 0:
        
        print("The position of the ship was:", chr(ship_start+64), chr(ship_end+64))
        print("Sorry, you've run out of attempts. The ship remains afloat.")
        print("GAME OVER!")
        break

