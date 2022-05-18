#!/usr/local/bin/python3

import os

DEBUG	= False

CLEAR="clear"
MARGIN_WIDTH = 0
PLAYING	= True
WINNER	= False

TITLE = "Tic Tac Toe (Python3)"
EMPTY_BOARD	= ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
TEST_BOARD	= ['#','X','O','X','O','X','O','X','O','X']
NUM_BOARD	= ['#', 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
PLAY_BOARD	= EMPTY_BOARD
PROMPTS		= { 
		0: 'Player #: Use numbers to specify square to place "%": ',
		1: '',
		2: '',
		3: 'Select X or O for Player 1 ([X]|O): ',
		"CONGRATS": 'Congratulations Player # (%). You won!'
		}


LABELS_ENABLED = True

## Good (H,W) values are (1,3), (3,7), (5,11) (odd Height, W=(H*2)+1)
CELL_HEIGHT	= 3
CELL_WIDTH	= (CELL_HEIGHT*2)+1
NUM_COLS	= 3
NUM_ROWS	= 3

ALL_MARK_CHOICES = ["X", "O"]
PLAYER_MARKS_POS = { 0: "?", 1: None, 2: None }
PLAYER_MARKS_STR = { "Unknown": "?", "Player 1": None, "Player 2": None }
PLAYER_MARKS = PLAYER_MARKS_POS

def clear():
	os.system(CLEAR)

def toggle_labels():
	global LABELS_ENABLED
	LABELS_ENABLED = not LABELS_ENABLED

def get_term_width():
	return os.get_terminal_size().columns

def set_margin(arg):
	global MARGIN_WIDTH
	if type(arg) is int:
		string_width = arg
	else:
		string_width = len(arg)
	MARGIN_WIDTH = int((os.get_terminal_size().columns - string_width)/2)

def print_margin():
	for i in range(MARGIN_WIDTH):
		print(" ", end='')

def set_player_marks():
	global PLAYER_MARKS
	global PROMPTS
	global PLAYING
	options = ALL_MARK_CHOICES.copy()
	prompt_len = max(map(len,PROMPTS.values()))
	set_margin(prompt_len + 1)
	print_margin()
	choice = input("Select X or O for Player 1 ([X]|O): ").upper()
	if DEBUG:
		print(f'DEBUG: (set_player_marks)[0]: options = "{options}"')
		print(f'DEBUG: (set_player_marks)[0]: choice  = "{choice}"')
	if choice in options:
		if DEBUG:
			print(f'DEBUG: (set_player_marks)[1]: options = "{options}"')
			print(f'DEBUG: (set_player_marks)[1]: choice  = "{choice}"')
		PLAYER_MARKS[1] = choice
		del options[options.index(choice)]
		PLAYER_MARKS[2] = options[0]
	elif choice == "Q":
		if DEBUG:
			print(f'DEBUG: (set_player_marks)[2]:  options = "{options}"')
			print(f'DEBUG: (set_player_marks)[2]:  choice  = "{choice}"')
			print(f'DEBUG: (set_player_marks)[2a]: PLAYING = "{PLAYING}"')
		PLAYING = False
		if DEBUG:
			print(f'DEBUG: (set_player_marks)[2b]: PLAYING = "{PLAYING}"')
		return False
	else:
		if DEBUG:
			print(f'DEBUG: (set_player_marks)[3]:  options = "{options}"')
			print(f'DEBUG: (set_player_marks)[3]:  choice  = "{choice}"')
			print(f'DEBUG: (set_player_marks)[3]:  PLAYING = "{PLAYING}"')
		PLAYER_MARKS[1] = options[0]
		PLAYER_MARKS[2] = options[1]
	PROMPTS[1] = PROMPTS[0].replace("#","1").replace("%",PLAYER_MARKS[1])
	PROMPTS[2] = PROMPTS[0].replace("#","2").replace("%",PLAYER_MARKS[2])


def make_move(player):
	global PLAY_BOARD
	global PLAYING
	move = 0
	mark = PLAYER_MARKS[player]
	prompt_len = max(map(len,PROMPTS.values()))
	set_margin(prompt_len + 1)
	print_margin()
	rawmove = input(PROMPTS[player])
	if DEBUG:
		print(f'DEBUG: (make_move)[0]:   PLAYING = "{PLAYING}"')
		print(f'DEBUG: (make_move)[0]:   rawmove = "{rawmove}"')
		print(f'DEBUG: (make_move)[0]:   type(rawmove)       = "{type(rawmove)}"')
		print(f'DEBUG: (make_move)[0]:   rawmove.isalpha()   = "{rawmove.isalpha()}"')
		print(f'DEBUG: (make_move)[0]:   rawmove.isnumeric() = "{rawmove.isnumeric()}"')
		print(f'DEBUG: (make_move)[0]:   rawmove.upper() = "{rawmove.upper()}"')
	if rawmove.isalpha() and rawmove.upper() == "Q":
		if DEBUG:
			print(f'DEBUG: (make_move)[1]:   type(rawmove)       = "{type(rawmove)}"')
			print(f'DEBUG: (make_move)[1]:   rawmove = "{rawmove}"')
			print(f'DEBUG: (make_move)[1]:   rawmove.upper() = "{rawmove.upper()}"')
		PLAYING = False
		return False
	if rawmove.isnumeric():
		if DEBUG:
			print(f'DEBUG: (make_move)[2]:   type(rawmove)       = "{type(rawmove)}"')
			print(f'DEBUG: (make_move)[2]:   rawmove = "{rawmove}"')
			print(f'DEBUG: (make_move)[2]:   rawmove.isnumeric() = "{rawmove.isnumeric()}"')
		move = int(rawmove)
		if move in range(1,len(PLAY_BOARD)) and PLAY_BOARD[move] == ' ':
			if DEBUG:
				print(f'DEBUG: (make_move)[3]:   type(rawmove)       = "{type(rawmove)}"')
				print(f'DEBUG: (make_move)[3]:   rawmove             = "{rawmove}"')
				print(f'DEBUG: (make_move)[3]:   rawmove.isnumeric() = "{rawmove.isnumeric()}"')
				print(f'DEBUG: (make_move)[3]:   type(move)          = "{type(move)}"')
				print(f'DEBUG: (make_move)[3]:   move                = "{move}"')
			PLAY_BOARD[move] = mark
			return True
	if DEBUG:
		print(f'DEBUG: (make_move)[4]:   PLAYING = "{PLAYING}"')
		print(f'DEBUG: (make_move)[4]:   rawmove = "{rawmove}"')
		print(f'DEBUG: (make_move)[4]:   rawmove.isalpha()   = "{rawmove.isalpha()}"')
		print(f'DEBUG: (make_move)[4]:   rawmove.isnumeric() = "{rawmove.isnumeric()}"')
	return False


## Checking board:
## num % 3 == 0, num-1, num-2
#1, 2, 3
#4, 5, 6
#7, 8, 9
## num < 4, num+3, num+6
#1, 4, 7
#2, 5, 8
#3, 6, 9
## 5, 5-2, 5+2
## 5, 5-4, 5+4
#1, 5, 9
#3, 5, 7

def three_equal(trio):
	B = PLAY_BOARD
	if DEBUG >= 3:
		print(f'DEBUG: (three_equal): B[trio[0]] = B[{trio[0]}] = "{B[trio[0]]}"')
		print(f'DEBUG: (three_equal): B[trio[1]] = B[{trio[1]}] = "{B[trio[1]]}"')
		print(f'DEBUG: (three_equal): B[trio[2]] = B[{trio[2]}] = "{B[trio[2]]}"')
	return B[trio[0]] != ' ' and ( B[trio[0]] == B[trio[1]] == B[trio[2]] )

def check_for_line():
	num	= ['#', 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
	won	= False
	for i in 1,4,7:
		if three_equal(num[i:i+3]):
			won = True
	for i in 1,2,3:
		if three_equal(num[i::3]):
			won = True
	if three_equal([1,5,9]):
		won = True
	if three_equal([3,5,7]):
		won = True
	return won


def display_board(board=EMPTY_BOARD):
	#def display_board():
	scratch_board = board.copy()
	if DEBUG >= 3:
		print(f'DEBUG: (display_board): board: "{board}"')
		print(f'DEBUG: (display_board): scratch_board: "{scratch_board}"')
	row_labels = [ ]
	board_width = (NUM_COLS*CELL_WIDTH)+(NUM_COLS+1)
	if not DEBUG:
		clear()
	set_margin(TITLE)
	print_margin()
	print(TITLE)
	print("")
	set_margin(board_width)
	def print_cell_border():
		set_margin(board_width)
		print_margin()
		print("+", end='')
		for c in range(3):
			for w in range(CELL_WIDTH):
				print("-", end='')
			print("+", end='')
		print("")
	def print_cell_row(vals=[" ", " ", " "]):
		set_margin(board_width)
		print_margin()
		print("|", end='')
		for c in range(NUM_COLS):
			for w in range(int((CELL_WIDTH-1)/2)):
				print(" ", end='')
			print(f"{vals[c]}", end='')
			for w in range(int((CELL_WIDTH-1)/2)):
				if CELL_HEIGHT >= 3 and LABELS_ENABLED and w == int((CELL_WIDTH-1)/2)-1:
					print(row_labels[c], end='')
				else:
					print(" ", end='')
			print("|", end='')
		print("")
	print_cell_border()
	for r in range(NUM_ROWS):
		row_labels = [" ", " ", " "]
		for h in range(int((CELL_HEIGHT-1)/2)):
			print_cell_row()
		print_cell_row(scratch_board[-3:])
		for h in range(int((CELL_HEIGHT-1)/2)):
			if h == int((CELL_HEIGHT-1)/2)-1:
				row_labels = [len(scratch_board)-3,len(scratch_board)-2,len(scratch_board)-1]
			print_cell_row()
		del scratch_board[-3:]
		print_cell_border()
	print("")

## 
## main()
## 

while PLAYING:
	WINNER = False
	EMPTY_BOARD	= ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
	PLAY_BOARD = EMPTY_BOARD.copy()
	if DEBUG >= 3: print(f'DEBUG: (main:PRE-display): PLAY_BOARD: "{PLAY_BOARD}"')
	player = 1
	display_board(PLAY_BOARD)
	set_player_marks()
	if DEBUG >= 3: print(f'DEBUG: (main:POST-display): PLAY_BOARD: "{PLAY_BOARD}"')
	while PLAYING and not WINNER and ' ' in PLAY_BOARD:
		if DEBUG >= 2: 
			print(f'DEBUG: (main:not_winner): player = "{player}"')
			print(f'DEBUG: (main): PLAYING = "{PLAYING}"')
		display_board(PLAY_BOARD)
		if make_move(player):
			if check_for_line():
				WINNER = True
				break
			player = player % 2 + 1
		if DEBUG:
			print(f'DEBUG: (main:post-move)[0]:   PLAYING = "{PLAYING}"')
			print(f'DEBUG: (main:post-move)[0]:   WINNER  = "{WINNER}"')
	if not PLAYING:
		exit()
	display_board(PLAY_BOARD)
	prompt_len = max(map(len,PROMPTS.values()))
	set_margin(prompt_len + 1)
	if WINNER:
		print_margin()
		print(f"Congratulations Player {player} ({PLAYER_MARKS[player]}). You won!")
	else:
		print_margin()
		print(f"It's a draw!")
	print("")
	print_margin()
	if input("Play again? ([Y]|n|q): ").lower() in ["n", "q"]:
		PLAYING = False


