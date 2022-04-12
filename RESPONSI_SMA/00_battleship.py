import os
import random

setting_up_board = lambda n : [list("X" * n) for i in range(n)]

setting_up_ship_loaction = lambda rows : [random.randint(0, rows-1), random.randint(0, rows-1)]

def printing_board(board):
	os.system("clear")
	for row in board:
		print(" ".join(row))


def check_user_input():
	user_input = list(map(int, input(">> Coordinates : ").split()))
	
	if user_input == my_ship:
		print("You Win")
		return True
	
	my_board[user_input[0]][user_input[1]] = "0"
	return False

win = False
rows = 5
my_board = setting_up_board(rows)
my_ship = setting_up_ship_loaction(rows)

while not win:
	printing_board(my_board)
	win = check_user_input()

