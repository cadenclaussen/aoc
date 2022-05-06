with open("21d25.txt") as f:
	a = f.read().strip().split("\n")
#print(a)

def main():
	board = createBoard(a)
	printBoard(board)
	print(step(board))

def createBoard(a):
	board = []
	for string in a:
		string = list(string)
		board.append(string)
	return board

def printBoard(board):
	print(" ", end="")
	for _ in range(len(board[0])):
		print("_", end="")
	print("")

	for string in board:
		print("|", end="")
		for y in range(len(string)):
			print(string[y], end="")
		print(" ")

def step(board):
	print("Called Function 'STEP'")
	step = 0
	moves = True
	#while moves:
	for i in range(4):
		board, movesEast = eastHerd(board)
		board, movesSouth = southHerd(board)
		moves = movesEast or movesSouth
		printBoard(board)
		step += 1
		print(step)
	return step

def eastHerd(board):
	moves = False
	skip = False
	for y in range(len(board)): # 0 1 2
		for x in range(len(board[0])):

			if skip:
				skip = False
				continue

			if board[y][x] != ">":
				continue

			if x == len(board[0]) - 1:
				if board[y][0] == ".":
					board[y][x] = "."
					board[y][0] = ">"
					moves = True
					skip = True
				continue

			if board[y][x + 1] == ".":
				board[y][x] = "."
				board[y][x + 1] = ">"
				moves = True
				skip = True
	
	return board, moves

def southHerd(board):
	moves = False
	skip = False
	for x in range(len(board[0])): # 0 1 2
		for y in range(len(board)):

			if skip:
				skip = False
				continue

			if board[y][x] != "v":
				continue

			if y == len(board) - 1:
				if board[0][x] == ".":
					board[y][x] = "."
					board[0][x] = "v"
					moves = True
					skip = True
				continue

			if board[y + 1][x] == ".":
				board[y][x] = "."
				board[y + 1][x] = "v"
				moves = True
				skip = True
	
	return board, moves




	
	
main()