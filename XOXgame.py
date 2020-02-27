
def displayBoard(board):
	print(board[7]+'|'+board[8]+'|'+board[9])
	print("--------")
	print(board[4]+'|'+board[5]+'|'+board[6])
	print("--------")
	print(board[1]+'|'+board[2]+'|'+board[3])

def playerInput():
	marker=''
	while marker!='X' and marker!='O':
		marker=input("Player1:Do you want to be X or O?")
		player1=marker
		if player1=='X':
			player2='O'
		else:
			player2='X'
	return (player1,player2)	

def placeMarker(board,marker,position,finish):
	if position>=1 and position<=9:
		board[position]=marker
		if (board[7] == board[8] == board[9] == marker) or (board[4] == board[5] == board[6] == marker) or (board[1] == board[2] == board[3] == marker) or (board[1] == board[4] == board[7] == marker) or (board[2] == board[5] == board[8] == marker) or (board[3] == board[6] == board[9] == marker) or (board[1] == board[5] == board[9] == marker) or (board[3] == board[5] == board[7] == marker):
			print("Games WİNNER "+marker+" !!")
			finish=0
			return finish
		else:
			finish=1
			return finish
	else:
		print("Please choice between 1 and 9")	
		finish=1
		return finish

firstBoard=['  ']*10
displayBoard(firstBoard)
player1Marker,player2Marker=playerInput()

turn=1
finish=1
while turn<10:
	choice=int(input("Please enter a number for the board position choice:(1,9)"))
	control=turn%2
	if control==1:
		finish=placeMarker(firstBoard,player1Marker,choice,finish)
	else:
		finish=placeMarker(firstBoard,player2Marker,choice,finish)
	turn=turn+1
	displayBoard(firstBoard)
	if finish==0:
		again = input("Do you want to play again??(Yes or No)")
		if again=="Yes":
			firstBoard=['  ']*10
			displayBoard(firstBoard)
			player1Marker,player2Marker=playerInput()
			turn=1
			finish=1
		else:
			print("See you laterr.")
			break
	elif finish==1 and turn==10:
		print("Game draw!!")
		again = input("Do you want to play again??(Yes or No)")
		if again=="Yes":
			firstBoard=['  ']*10
			displayBoard(firstBoard)
			player1Marker,player2Marker=playerInput()
			turn=1
			finish=1
		else:
			print("See you laterr.")
			break 	