#!/usr/local/bin/python3

import os

CLEAR="clear"
MARGIN_WIDTH = 0
playing=True

TITLE = "Tic Tac Toe (Python3)"
HORIZONTAL_LINE = "+-----+-----+-----+"
EMPTY_BOARD = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
NUMBER_KEYBOARD = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
PLAY_BOARD = EMPTY_BOARD

CELL_HEIGHT = 3
CELL_WIDTH  = 7

def clear():
	os.system(CLEAR)

def get_term_width():
	return os.get_terminal_size().columns

def set_margin(input):
	global MARGIN_WIDTH
	if type(input) is int:
		string_width = input
	else:
		string_width = len(input)
	MARGIN_WIDTH = int((os.get_terminal_size().columns - string_width)/2)

def print_margin():
	for i in range(MARGIN_WIDTH):
		print(" ", end='')

def initialized_board(board):
	return ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]



def mark_board(num, mark, board):
	if board[num] == " ":
		board[num] = mark

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

def three_equal(one, two, three):
	return one == two == three

def check_for_line(board):
	lineFound = False


def display_board(board):
	clear()
	set_margin(TITLE)
	print_margin()
	print(TITLE)
	print("")
	set_margin(len(HORIZONTAL_LINE))
	print_margin()
	print(HORIZONTAL_LINE)
	print_margin()
	for i in range(1,len(board)):
		print(f"|  {board[i]}  ", end='')
		if i % 3 == 0:
			print("|")
			print_margin()
			print(HORIZONTAL_LINE)
			print_margin()
	print("")

def display_board_like_keyboard(board):
	def print_cell_border():
		print("+", end='')
		for c in range(3):
			for w in range(CELL_WIDTH):
				print("-", end='')
			print("+", end='')
		print("")
	def print_cell_row(vals=[" ", " ", " "]):
		print("|", end='')
		for c in range(3):
			for w in range(int((CELL_WIDTH-1)/2)):
				print(" ", end='')
			print(f"{vals[c]}", end='')
			for w in range(int((CELL_WIDTH-1)/2)):
				print(" ", end='')
			print("|", end='')
		print("")
	def print_cell_row(vals=[" ", " ", " "]):
		for h in range(int((CELL_HEIGHT-1)/2)):
			print("|", end='')
			for c in range(3):
				for w in range(int((CELL_WIDTH-1)/2)):
					print(" ", end='')
				print(f"{value}", end='')
				for w in range(int((CELL_WIDTH-1)/2)):
					print(" ", end='')
				print("|", end='')
	clear()
	set_margin(TITLE)
	print_margin()
	print(TITLE)
	print("")
	set_margin(len(HORIZONTAL_LINE))
	print_margin()
	print(HORIZONTAL_LINE)
	print_margin()
	for i in range(7,10):
		print(f"|  {board[i]}  ", end='')
	print("|")
	print_margin()
	print(HORIZONTAL_LINE)
	print_margin()
	for i in range(4,7):
		print(f"|  {board[i]}  ", end='')
	print("|")
	print_margin()
	print(HORIZONTAL_LINE)
	print_margin()
	for i in range(1,4):
		print(f"|  {board[i]}  ", end='')
	print("|")
	print_margin()
	print(HORIZONTAL_LINE)
	print("")

test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)
display_board(EMPTY_BOARD)
print("")
display_board_like_keyboard(NUMBER_KEYBOARD)
