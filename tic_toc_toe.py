if __name__ == "__main__":
	import sys
	print('Please do not select any value between 1 - 9')
	symbol1 = input("Enter player 1 symbol:")
	symbol2 = input("Enter player 2 symbol:")

	if(symbol1 in range(1,10) or symbol2 in range(1,10)):
		print('You have entered wrong symbol. Exiting the game')
		sys.exit()

	play_board = [[1,2,3],[4,5,6],[7,8,9]]

	for lists in play_board:
		for item in lists:
			print('{0} |'.format(item), end=" ")
		print('\n','-'*10)

	win = -1

	while(win not in [0,1,2]):
		#win = -1
		position = int(input('First player position:'))
		for i in range(3):
			for j in range(3):
				if play_board[i][j] == position:
					play_board[i][j] = symbol1

		for lists in play_board:
			for item in lists:
				print('{0} |'.format(item), end=" ")
			print('\n','-'*10)

		for i in range(3):
			if(play_board[i][0] == symbol1 and play_board[i][1] == symbol1 and play_board[i][2] == symbol1):
				print('Player 1 won the game')
				sys.exit()

		for i in range(3):
			if(play_board[0][i] == symbol1 and play_board[1][i] == symbol1 and play_board[2][i] == symbol1):
				print('Player 1 won the game')
				sys.exit()

		if(play_board[0][0] == symbol1 and play_board[1][1] == symbol1 and play_board[2][2] == symbol1):
			print('Player 1 won the game')
			sys.exit()


		if(play_board[0][0] == symbol1 and play_board[1][1] == symbol1 and play_board[2][2] == symbol1):
			print('Player 1 won the game')
			sys.exit()

		alive = 0

		for i in range(3):
			for j in range(3):
				if(play_board[i][j] in range(1,10)):
					alive = 1
					break

		print('alive=', alive)

		if(alive != 1):
			print('Game draw');
			sys.exit()


		position = int(input('Second player position:'))
		for i in range(3):
			for j in range(3):
				if play_board[i][j] == position:
					play_board[i][j] = symbol2

		for lists in play_board:
			for item in lists:
				print('{0} |'.format(item), end=" ")
			print('\n','-'*10)

		for i in range(3):
			if(play_board[i][0] == symbol2 and play_board[i][1] == symbol2 and play_board[i][2] == symbol2):
				print('Player 2 won the game')
				sys.exit()

		for i in range(3):
			if(play_board[0][i] == symbol2 and play_board[1][i] == symbol2 and play_board[2][i] == symbol2):
				print('Player 2 won the game')
				sys.exit()

		if(play_board[0][0] == symbol2 and play_board[1][1] == symbol2 and play_board[2][2] == symbol2):
			print('Player 2 won the game')
			sys.exit()


		if(play_board[0][0] == symbol2 and play_board[1][1] == symbol2 and play_board[2][2] == symbol2):
			print('Player 2 won the game')
			sys.exit()

		alive = 0

		for i in range(3):
			for j in range(3):
				if(play_board[i][j] in range(1,10)):
					alive = 1
					break

		print('alive=', alive)

		if(alive != 1):
			print('Game draw');
			sys.exit()
