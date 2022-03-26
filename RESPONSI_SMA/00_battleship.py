setting_up_board = lambda n : ["X" * n for i in range(n)]

def printing_board(board):
	for row in board:
		print(" ".join(row))

win = False
rows = 5
my_board = setting_up_board(rows)

while not win:
	printing_board(my_board)
	input()

# lists = [[0, 1, 2], [3, 4, 5]]
# for list in lists:
# 	for item in list:
# 		print(item, end=" ")
# 	print()

# # texts = []
# # text = "X" * 3

# # for i in range(3):
# # 	texts.append(text)

# texts = ["X"  *3 for i in range(3) ]

# # print(texts)
# # texts = ["XXX", "XXX", "XXX"]
# """
# for text in texts:
# 	for char in text:
# 		print(char, end=" ")
# 	print()
# """

# for text in texts:
# 	print(" ".join(text))
