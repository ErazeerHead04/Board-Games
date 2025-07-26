import random
import os
import time

#Global constant varibles:
MiN_DIMENSION=4
MAX_DIMENSION=9
MAX_PLAYERS=5

NUM_PLAYERS=2 #We can change the value to set the number of players

CHECKERS=['X','O','M','N','P'][:NUM_PLAYERS]

NUM_ROW = 6
NUM_COL = 6

# Initiate the board:
def initialize_board():
    board = []
    for row in range(NUM_ROW):
        row_list = []
        for col in range(NUM_COL):
            row_list.append(' ')
        board.append(row_list)
    return board

# Print the board:
def print_board(board):
	print('\n'+ ' '*NUM_COL+' OBSTRUCTION\n')
	print('  ', end='')
	for char in range(NUM_COL):
		print(' '+chr(char+65)+' ', end=' ')
	print('\n +'+ '---+'*NUM_COL)

	for row in range(NUM_ROW):
		print(str(row)+'|', end=' ')
		for col in range(NUM_COL):
			print(f'{board[row][col]} |', end=' ')
		print('\n +'+'---+'*NUM_COL)

# Create the board
board = initialize_board()
# Print the board
print_board(board)

#Coordinate validation:
def is_valid_coordinate(coord):
	if len(coord)!=2 or not coord[0].isalpha() or not coord[0].isupper() or not coord[1].isdigit():
		return False
	col, row = ord(coord[0])-65, int(coord[1])
	return 0 <= col <NUM_COL and 0<= row <NUM_ROW


def is_cell_free(coord,board):
	col, row = ord(coord[0])-65, int(coord[1])
	return board[row][col]== ' '

#Turns and their updates:

def block_neighboring_cells(coord, board):
	col=ord(coord[0])-65
	row=int(coord[1])
	directions=[[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]

	for direction in directions:
		dx, dy= direction
		new_col, new_row= col+dx, row+dy
		if 0<= new_col < NUM_COL and 0<= new_row <NUM_ROW:
			board[new_row][new_col] = '#'

def are_possible_turns(board):
	return any(' ' in row for row in board)

def player_wins(player, board):
	for i in range(NUM_ROW):
		for j in range(NUM_COL):
			if board[i][j]==' ':
				return False
	return True

#Game function
def play_game():
	global NUM_PLAYERS
	global CHECKERS

	board= initialize_board()
	current_player=random.choice(CHECKERS)

	#Game loop
	while True:
		os.system('clear')
		print_board(board)
		print(f"\nPlayer '{current_player}', it's your turn!")

		while True:
			coord=input('Enter the coordinates (e.g., A1): ')

			if not is_valid_coordinate(coord):
				
				os.system('clear')
				print_board(board)
				print(f"\nPlayer '{current_player}', it's your turn!")
				print('Invalid coordinate. Please give a valid coordinate (i.g. A1)')
				time.sleep(1)
				continue
			if not is_cell_free(coord, board):
				
				os.system('clear')
				print_board(board)
				print(f"\nPlayer '{current_player}', it's your turn!")
				print('Selected cell is already occupied. Please try again.')
				time.sleep(1)
				continue

			break

		col, row= ord(coord[0])-65, int(coord[1])
		board[row][col] = current_player
		block_neighboring_cells(coord,board)

		if player_wins(current_player,board):
			os.system('clear')
			print_board(board)
			print(f"\nPlayer '{current_player}' wins!\nGAME OVER.")
			break

		# Find the index of the current player in the CHECKERS list
		player_index = CHECKERS.index(current_player)

		# Increment the index by 1 to get the next player
		next_player_index = (player_index + 1) % NUM_PLAYERS

		# Update current_player with the player at the new index
		current_player = CHECKERS[next_player_index]


#Calling the play_game function directly
play_game()


